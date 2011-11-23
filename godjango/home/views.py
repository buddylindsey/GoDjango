from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify
from home.models import Video
from datetime import datetime

def index(request):
    videos = Video.objects.filter(publish_date__lte=datetime.now()).order_by('-publish_date')[:10]
    return render_to_response('home/index.html', 
            { 'videos': videos },
            context_instance=RequestContext(request))

def video(request, video_id, slug):
    video = Video.objects.get(pk=video_id)
    return render_to_response('home/video.html', 
            { 'video': video },
            context_instance=RequestContext(request))

def about(request):
    return render_to_response('home/about.html', 
            { },
            context_instance=RequestContext(request))

def feedback(request):
    return render_to_response('home/feedback.html', 
            { },
            context_instance=RequestContext(request))
