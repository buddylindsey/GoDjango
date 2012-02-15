from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')

@login_required
def dashboard(request):
    return render_to_response('users/dashboard.html', 
            { },
            context_instance=RequestContext(request))
