from django.shortcuts import *
from django.http import Http404, HttpResponse
from dg.dashboard.models import *
from calendar import week
import datetime
from dg.output  import database
from dg.output.database import run_query, run_query_dict, construct_query

def test_output(request):
    
    return render_to_response('amline.html')


def overview(request,geog,id):
    
    if('village' in request.GET and request.GET['village'] and request.GET['village']!='-1'):
        geog = 'village'
        id = int(request.GET['village'])
    elif('block' in request.GET and request.GET['block'] and request.GET['block']!='-1'):
        geog = 'block'
        id = int(request.GET['block'])
    elif('district' in request.GET and request.GET['district'] and request.GET['district']!='-1'):
        geog = 'district'
        id = int(request.GET['district'])        
    elif('state' in request.GET and request.GET['state'] and request.GET['state']!='-1'):
        geog = 'state'
        id = int(request.GET['state'])    
         
    geog_list = ['country','state','district','block','village']
    if(geog == 'village' or geog not in geog_list):
        raise Http404()
    flash_geog = geog
    geog = geog_list[geog_list.index(geog)+1]
    
    if 'from_date' in request.GET and request.GET['from_date'] \
    and 'to_date' in request.GET and request.GET['to_date']:
        date_range = 1
        from_date = request.GET['from_date']
        to_date = request.GET['to_date']
        vid_prod = run_query(construct_query(database.overview,dict(type='production',geography=geog,from_date=from_date,to_date=to_date,id=id)));
        vid_screening = run_query(construct_query(database.overview,dict(type='screening',geography=geog,from_date=from_date,to_date=to_date,id=id)));
        adoption = run_query(construct_query(database.overview,dict(type='adoption',geography=geog,from_date=from_date,to_date=to_date,id=id)));
        tot_prac = run_query(construct_query(database.overview,dict(type='practice',geography=geog,from_date=from_date,to_date=to_date,id=id)));
        tot_per = run_query(construct_query(database.overview,dict(type='person',geography=geog,from_date=from_date,to_date=to_date,id=id)));
    else:
        date_range = 0
        vid_prod = run_query(construct_query(database.overview,dict(type='production',geography=geog,id=id)));
        vid_screening = run_query(construct_query(database.overview,dict(type='screening',geography=geog,id=id)));
        adoption = run_query(construct_query(database.overview,dict(type='adoption',geography=geog,id=id)));
        tot_prac = run_query(construct_query(database.overview,dict(type='practice',geography=geog,id=id)));
        tot_per = run_query(construct_query(database.overview,dict(type='person',geography=geog,id=id)));
    
    return_val = vid_prod
    if (len(vid_screening) != len(return_val)) or (len(return_val)!=len(adoption))or \
    (len(return_val)!=len(tot_per)) or (len(return_val)!=len(tot_prac)):
        raise Exception,"Query return list not of same size"
    for i in range(len(vid_screening)):
        if (vid_screening[i]['name'] != return_val[i]['name']) or \
        (adoption[i]['name'] != return_val[i]['name']) or (tot_per[i]['name'] != return_val[i]['name']) or \
        (tot_prac[i]['name'] != return_val[i]['name']):
            raise Exception,"Query return list do not match"
        
        return_val[i]['tot_ado'] = adoption[i]['tot_ado']
        return_val[i]['tot_scr'] = vid_screening[i]['tot_scr']
        return_val[i]['tot_pra'] = tot_prac[i]['tot_pra']
        return_val[i]['tot_per'] = tot_per[i]['tot_per'] 
        
    return render_to_response('viewtable1.html',{'item_list':return_val,'geography':geog,'flash_geog':flash_geog,'id':id})
    
def overview_drop_down(request):
    if 'geog' in request.GET and request.GET['geog'] \
     and 'id' in request.GET and request.GET['id']:
         geog = request.GET['geog']
         id = request.GET['id']
         id = int(id)
    else:
        raise Http404()
    
    return_val = []
    if (geog=='state'):
      #return_val.append("<select class='select' name='state' id = 'statesId' onChange=\"dochange('district', this.value)\">");
      return_val.append("<option value='-1'>Select State</option>");
      rs = run_query(construct_query(database.search_drop_down_list,dict(geog='state')));
      for row in rs:       
          return_val.append("<option value="+str(row['id'])+" >"+row['name']+"</option>" );
     
    elif (geog=='district'):
      #return_val.append("<select class='select' name='district' id = 'districtId' onChange=\"dochange('block', this.value)\">");
      return_val.append("<option value='-1'>Select District</option>");                  
      rs = run_query(construct_query(database.search_drop_down_list,dict(geog=geog,geog_parent='state',id=id)));
      for row in rs:       
          return_val.append("<option value="+str(row['id'])+" >"+row['name']+"</option>" );
      
    elif (geog=='block'):
      #return_val.append("<select class='select' name='block' id = 'blockId' onChange=\"dochange('village', this.value)\">>");
      return_val.append("<option value='-1'>Select Block</option>");                  
      rs = run_query(construct_query(database.search_drop_down_list,dict(geog=geog,geog_parent='district',id=id)));
      for row in rs:       
          return_val.append("<option value="+str(row['id'])+" >"+row['name']+"</option>" );

    elif (geog=='village'):
      #return_val.append("<select class='select' name='village' id = 'villageId' >");
      return_val.append("<option value='-1'>Select Village</option>");                  
      rs = run_query(construct_query(database.search_drop_down_list,dict(geog=geog,geog_parent='block',id=id)));
      for row in rs:       
          return_val.append("<option value="+str(row['id'])+" >"+row['name']+"</option>" );
      
    #return_val.append("</select>");
    
    return HttpResponse('\n'.join(return_val))     
    
         
def overview_line_graph(request,geog,id):
    id = int(id)
    vid_prod_rs = run_query_dict(construct_query(database.overview_line_chart,dict(type='production',geography=geog,id=id)),'date');
    sc_rs = run_query_dict(construct_query(database.overview_line_chart,dict(type='screening',geography=geog,id=id)),'date');
    adopt_rs = run_query_dict(construct_query(database.overview_line_chart,dict(type='adoption',geography=geog,id=id)),'date');
    prac_rs = run_query_dict(construct_query(database.overview_line_chart,dict(type='practice',geography=geog,id=id)),'date');
    person_rs = run_query_dict(construct_query(database.overview_line_chart,dict(type='person',geography=geog,id=id)),'date');
        
    start_date = today = datetime.date.today()
    if vid_prod_rs:
        start_date = min(start_date, *(vid_prod_rs.keys()))
    if sc_rs:
        start_date = min(start_date,*(sc_rs.keys()))
    if adopt_rs:
        start_date = min(start_date,*(adopt_rs.keys()))
    if prac_rs:
        start_date = min(start_date,*(prac_rs.keys()))
    if person_rs:
        start_date = min(start_date,*(person_rs.keys()))
          
    diff = (today - start_date).days
    
    str_list = []
    sum_vid = sum_sc = sum_adopt =sum_prac = sum_person = 0
    for i in range(0,diff+1):
        iter_date = start_date + datetime.timedelta(days=i)
                
        if iter_date in vid_prod_rs:
            sum_vid += vid_prod_rs[iter_date][0]
        if iter_date in sc_rs:
            sum_sc += sc_rs[iter_date][0]
        if iter_date in adopt_rs:
            sum_adopt += adopt_rs[iter_date][0]
        if iter_date in prac_rs:
            sum_prac += prac_rs[iter_date][0]
        if iter_date in person_rs:
            sum_person += person_rs[iter_date][0]
        str_list.append(iter_date.__str__() +';'+ sum_vid.__str__()+';'+ sum_sc.__str__()+';'+ sum_adopt.__str__() \
                        +';'+ sum_prac.__str__()+';'+ sum_person.__str__())
        
    return HttpResponse('\n'.join(str_list))
    

    
    
    
    