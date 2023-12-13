from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):

    return HttpResponse("Welcome to the MobileApp API Home <br /> if you are seeing this, the MobileApp Webservice is Online")

def features(request):
    obj={
       "data":[
        {
        'title':"Product",
        'description':"<li>Tracking</li><li>Haulage</li><li>Clearing</li><li>Fast Track</li><li>End-To-End Logistics</li><li>Warehousing</li>",
        'writer':"Me",
        'firstCreated':"2023-12-13 14:14",
        'modified':"2023-12-13 14:14"
    },
     {
        'title':"Product",
        'description':"<li>Tracking</li><li>Haulage</li><li>Clearing</li><li>Fast Track</li><li>End-To-End Logistics</li><li>Warehousing</li>",
        'writer':"Me",
        'firstCreated':"2023-12-13 14:14",
        'modified':"2023-12-13 14:14"
    },
     {
        'title':"Product",
        'description':"<li>Tracking</li><li>Haulage</li><li>Clearing</li><li>Fast Track</li><li>End-To-End Logistics</li><li>Warehousing</li>",
        'writer':"Me",
        'firstCreated':"2023-12-13 14:14",
        'modified':"2023-12-13 14:14"
    },
     {
        'title':"Product",
        'description':"<li>Tracking</li><li>Haulage</li><li>Clearing</li><li>Fast Track</li><li>End-To-End Logistics</li><li>Warehousing</li>",
        'writer':"Me",
        'firstCreated':"2023-12-13 14:14",
        'modified':"2023-12-13 14:14"
    }
       ]
       }

    response=JsonResponse(obj,status=200)
    return response