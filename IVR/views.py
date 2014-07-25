# Create your views here.

from datetime import datetime
from django.contrib import auth
from django.core import urlresolvers
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

def greeting_view(request):
	return HttpResponse("https://s3.amazonaws.com/digitalgreen/try2+(1).wav")