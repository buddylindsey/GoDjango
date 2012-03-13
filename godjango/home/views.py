from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator

from home.models import Video
from datetime import datetime

def index(request):
    videos_list = Video.objects.filter(publish_date__lte=datetime.now()).order_by('-publish_date')

    paginator = Paginator(videos_list, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        videos = paginator.page(page)
    except(EmptyPage, InvalidPage):
        videos = paginator.page(paginator.num_pages)

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
