from django.http import HttpResponse
from django.shortcuts import render_to_response
from bestsell.models import Shout

def shout(request):
    shouts = Shout.objects.all()
    return render_to_response("shout.html", {'shouts': shouts})