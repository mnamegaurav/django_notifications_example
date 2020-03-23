from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def home(request):
    template = 'home.html'
    return render(request,template)

def email_form(request):
    if request.method == 'POST':
        to_email = [request.POST.get('email')]
        message = request.POST.get('msg')
        subject = request.POST.get('sbj')
        from_email = settings.EMAIL_HOST_USER

        if subject and message and from_email and to_email:
            try:
                email = EmailMessage(subject,message,from_email,to_email)
                email.send(fail_silently=False)
            except (BadHeaderError,ValueError):
                return HttpResponse('Invalid header found or Check your Email')
            return HttpResponse('Email is Sent SuccessFully')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

            
def notif_form(request):
    if request.method == 'POST':
        return HttpResponse('Success')