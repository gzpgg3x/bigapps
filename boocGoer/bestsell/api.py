from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from bestsell.models import *

import json
from datetime import datetime

@csrf_exempt
@require_POST
def new_shout(request):
    lat = request.POST['lat']
    lng = request.POST['lng']
    booklist = request.POST['booklist']
    bldate = request.POST['bldate']

    shout = Shout.objects.create(lat=lat,lng=lng,booklist=booklist,bldate=bldate)

    response = {
        'date_created': shout.date_created.strftime("%b %d at %I:%M:%S%p"),
        'lat': str(shout.lat),
        'lng': str(shout.lng),
        'booklist': booklist,
        'bldate': bldate
    }
    
    return HttpResponse(json.dumps(response))

def get_shouts(request):
    lat = float(request.GET['lat'])
    lng = float(request.GET['lng'])
    radius = float(request.GET['radius'])

    lat_low = str(lat - radius)
    lat_high = str(lat + radius)
    lng_low = str(lng - radius)
    lng_high = str(lng + radius)
    
    shouts = Shout.objects.filter(lat__gte=lat_low,lat__lte=lat_high,lng__gte=lng_low,lng__lte=lng_high)[:100]
    
    response = []
    for shout in shouts:
        response.append({
            'date_created': shout.date_created.strftime("%b %d at %I:%M:%S%p"),
            'lat': str(shout.lat),
            'lng': str(shout.lng),
            'booklist': shout.booklist,
            'bldate': shout.bldate
        })
    
    return HttpResponse(json.dumps(response))