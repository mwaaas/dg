import site, sys
from django.core.management import setup_environ
import dg.settings
setup_environ(dg.settings)

from pyes import *
from social_website.models import Collection
from django.core import serializers
from django.forms.models import model_to_dict
import datetime
from time import mktime
import json, urllib2


conn = ES(['127.0.0.1:9200'])
try:
    conn.delete_index("test2")
    print "Previous index deleted"
except Exception, ex:
    print "No Previous index"

mappings ={
          "test2":{
                 "properties":{
                               "subcategory" : {
                                                "type" : "string",
                                                "analyzer" : "keyword"
                                                },
                               "category" : {
                                                "type" : "string",
                                                "analyzer" : "keyword"
                                                },
                               "topic" : {
                                                "type" : "string",
                                                "analyzer" : "keyword"
                                                },
                               "subject" : {
                                                "type" : "string",
                                                "analyzer" : "keyword"
                                                },
                               
                               "language" : {
                                                "type" : "string",
                                                "analyzer" : "keyword"
                                                },
                               "partner" : {
                                                "type" : "string",
                                                "analyzer" : "keyword"
                                                },
                               "state" : {
                                                "type" : "string",
                                                "analyzer" : "keyword"
                                                },
                               "videos" : {
                                                "type" : "nested",
                                                },
                   }
           }
        }

             
conn.indices.create_index("test2")

conn.indices.put_mapping(doc_type = "test2", mapping = mappings, indices = ["test2"])

# putting in the data
i = 0
print Collection.objects.all().count()
for obj in Collection.objects.all():
    vid_data = []
    time = 0
    for index, vid in enumerate(obj.videos.all()):
        vid_id = index+1 
        url = "/social/collections/?id=" + str(obj.uid) + "&video=" + str(vid_id)
        vid_data.append({"title" : vid.title, 
                         "subcategory" : vid.subcategory, 
                         "description" : vid.description,
                         "duration" : vid.duration, 
                         "thumbnailURL" : vid.thumbnailURL16by9, 
                         "youtubeID" : vid.youtubeID,
                         "videoURL" : url})
        time += vid.duration
    partner = model_to_dict(obj.partner, fields = ['name'])
#    partner["joinDate"] = partner["joinDate"].strftime("%Y-%m-%d %H:%M:%S")
    
    video = json.dumps(vid_data)
    data = json.dumps({"title" : obj.title,
                       "url" : "", 
                       "language" : obj.language,
                       "partner" : obj.partner.name,
                       "state" : obj.state,
                       "category" : obj.category,
                       "subcategory" : obj.subcategory, 
                       "topic": obj.topic, 
                       "subject" : obj.subject, 
                       "likes" : obj.likes, 
                       "views" : obj.views, 
                       "adoptions" : obj.adoptions,
                       "thumbnailURL" : obj.thumbnailURL,
                       "uid" : obj.uid,
                       "videos" : vid_data,
                       "duration" : time
                       })    
    conn.index(data, "test2","test2",i+1)
    i+= 1
#conn.default_indices="test2"
#conn.refresh("test2")
#query = {"query": 
#                        {
#                         "nested" : {
#                                     "path" : "videos",
#                                     "videos.title"  :{
#                                                      "query" : "tomato",
#                                                      "analyzer" : "pattern",
#                                              "max_query_terms" : 12
#                                              }
#                                    }
#                         },
#                        "facets" : {"facet" : {
#                                               "terms": {
#                                                         "fields" : ["language_name", "partner_name", "state", "category", "subcategory" , "topic", "subject"], 
#                                                         "size" : 500
#                                                         }
#                                               }
#                                    },
#                 "size" : 500
#                 }
#query = json.dumps(query)
#response = urllib2.urlopen('http://localhost:9200/test2/_search',query)
#result = json.loads(response.read())
#print result
#data = json.dumps({"facets" : result['facets']['facet']['terms']})

    