# Create your views here.
import logging
from datetime import datetime
from django.contrib import auth
from django.core import urlresolvers
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests
from IVR.models import VideosAdopted


sid = "digitalgreen2"
token = "421c11b1235067ca30ca87590c80c31eadc46af0"
        # agent_no="9718935868",
        #customerNo="9718935868",
customerNo="9910338592"
callerid="04030911139"
url='http://my.exotel.in/exoml/start/27038'
timelimit="500"  # This is optional
timeout="500" # This is also optional
calltype="trans" # Can be "trans" for transactional and "promo" for promotional content
videoId="395"

def greeting_view(request):
	callSid = request.GET["CallSid"]
	frm = request.GET["From"]
	to = request.GET["To"]
	response = HttpResponse("https://s3.amazonaws.com/digitalgreen/try2+(1).wav",content_type="text/plain")
	response["CallSid"] = callSid
	response["From"] = frm
	response["To"] = to
	response["DialWhomNumber"] = ""
	#response["CustomField"] =  videoId


	return response

def list_page(request):
	qs = VideosAdopted.objects.all()
	paginator = Paginator(qs, 1) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		list_elements = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		list_elements = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		list_elements = paginator.page(paginator.num_pages)

	return render_to_response('list_page.html', {"list_elements": list_elements})

def call_exotel(request):
	req_id = request.GET.get("id")
	vals = VideosAdopted.objects.get(id__exact=req_id)
	r = requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.json'.format(sid=sid),
        auth=(sid, token),
        data={
            'From': int(vals.mobile_no),
            'CallerId': callerid,
            'TimeLimit': timelimit,
            'Url': url,
            'TimeOut': timeout,
            'CallType': calltype,
            'CustomField': vals.video_id
        })
	print r.status_code
	return r

def has_not_seen(request):
	video_id = request.GET['CustomField']
	mobile_no = request.GET['From'][1:]
	logger = logging.getLogger('social_website')
	logger.info("Mobile number computed : " + mobile_no)
	logger.info("Video ID computed : " + video_id)
	try:
		video_view = VideosAdopted.objects.get(id=2)
		video_view.has_seen = False
		video_view.has_adopted = False
		video_view.save()
		logger.info("video view saved")
		logger.info(video_view.has_seen)
		logger.info("Person : " + video_view.person)
	except Exception as ex:
		logger.info(ex)
	
	
def has_not_adopted(request):
	video_id = request.GET['CustomField']
	mobile_no = request.GET['From'][1:]
	video_view = VideosAdopted.objects.get(video_id=video_id, mobile_no=mobile_no)
	video_view.has_adopted = False
	video_view.save()



