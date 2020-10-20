from django.shortcuts import render
# Include for responding to http requests
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse('Hello, World!')
