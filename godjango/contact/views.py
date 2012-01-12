from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail

from contact.forms import FeedbackForm

def feedback(request):
    if(request.method == "POST"):
        form = FeedbackForm(request.POST)

        if(form.is_valid()):
            send_mail('[GoDjango Feedback Form]', request.POST['body'], request.POST['email'], ['buddy@buddylindsey.com'], fail_silently=False)
            message = "Thank you for the email"
        else:
            message = "Please be sure to use an email address and have a message in the body."
    else:
        message = ""
    

    return render_to_response('contact/feedback.html',
            { 'form':FeedbackForm(), 'message':message },
            context_instance=RequestContext(request))
