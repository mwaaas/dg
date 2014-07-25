# Create your views here.

from datetime import datetime
from django.contrib import auth
from django.core import urlresolvers
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

def greeting_view(request):
	callSid = request.QUERY_PARAMS["CallSid"]
	frm = request.QUERY_PARAMS["From"]
	to = request.QUERY_PARAMS["To"]
	response = HttpResponse("https://s3.amazonaws.com/digitalgreen/try2+(1).wav",content_type="text/plain")
	response["CallSid"] = callSid
	response["From"] = frm
	response["To"] = to
	response["DialWhomNumber"] = ""


	return response