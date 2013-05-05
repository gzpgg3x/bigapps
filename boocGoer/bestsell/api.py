from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from bestsell.models import *

import json
from datetime import datetime

import urllib2
#from urllib2 import urlopen
from json import loads
import codecs, sys
import os 
sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

@csrf_exempt
@require_POST
def new_shout(request):
    Shout.objects.all().delete()
    lat = request.POST['lat']
    lng = request.POST['lng']
    booklist = request.POST['booklist']
    bldate = request.POST['bldate']
    url = "http://api.nytimes.com/svc/books/v2/lists/" + bldate + "/" + booklist + "?&offset=&sortby=&sortorder=&api-key=1ddfd825a1084dbe50334ad25dd5ddfa:2:67632807"
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    articles = json.loads(f.read())
    # print articles
    g=""
    pubdate=""
    for story in articles["results"]:
        b = 0
        for book in story["isbns"]:
            if b == 0: 
                try:
                    isbn = book["isbn10"]
                    # pubdate = book["published_date"]
                    g = g + book["isbn10"] + "\n"
                    b = b + 1
                except:
                    isbn = ""
                    g = g + " \n"       
        for book in story["book_details"]: 
            try:
                title = book["title"]
                author = book["author"]
                description = book["description"]
                publisher = book["publisher"]
                g = g + book["title"] + "\n"
            except:
                g = g + " \n"

        shout = Shout.objects.create(lat=lat,lng=lng,booklist=booklist,bldate=bldate,isbn=isbn,title=title,author=author,description=description,publisher=publisher)

        response = {
            'date_created': shout.date_created.strftime("%b %d at %I:%M:%S%p"),
            'lat': str(shout.lat),
            'lng': str(shout.lng),
            'booklist': booklist,
            'bldate': bldate,
            'isbn': isbn,
            'title': title,
            'author': author,
            'description': description,
            'publisher': publisher
        }

    # print g

    # shout = Shout.objects.create(lat=lat,lng=lng,booklist=booklist,bldate=bldate)

    # response = {
    #     'date_created': shout.date_created.strftime("%b %d at %I:%M:%S%p"),
    #     'lat': str(shout.lat),
    #     'lng': str(shout.lng),
    #     'booklist': booklist,
    #     'bldate': bldate
    # }
    
    return HttpResponse(json.dumps(response))

def get_shouts(request):

    

    lat = float(request.GET['lat'])
    lng = float(request.GET['lng'])
    radius = float(request.GET['radius'])

    lat_low = str(lat - radius)
    lat_high = str(lat + radius)
    lng_low = str(lng - radius)
    lng_high = str(lng + radius)
    
    shouts = Shout.objects.filter(lat__gte=lat_low,lat__lte=lat_high,lng__gte=lng_low,lng__lte=lng_high)[:10000]
    
    response = []
    for shout in shouts:
        response.append({
            'date_created': shout.date_created.strftime("%b %d at %I:%M:%S%p"),
            'lat': str(shout.lat),
            'lng': str(shout.lng),
            'booklist': shout.booklist,
            'bldate': shout.bldate,
            'isbn': shout.isbn,
            'title': shout.title            
        })
    
    return HttpResponse(json.dumps(response))