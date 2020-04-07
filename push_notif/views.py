from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

from pyfcm import FCMNotification

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
            except:
                return HttpResponse('Invalid header found or Check your Email')
            return HttpResponse('Email is Sent SuccessFully')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

            
def notif_form(request):
    if request.method == 'POST':
        msg_head = request.POST.get('msg_head')
        msg_body = request.POST.get('msg_body')
        target = request.POST.get('target')

        path_to_fcm = "https://fcm.googleapis.com"
        server_key = settings.SERVER_KEY
        reg_id = 'exwjyZ6XW7Y:APA91bGxme3NPHLrY9oIEz6EcYzwoCAh9fjpFBw2BMflILRm17tSYfRj03FY2rU3g2FW2vsv80eA-S9r2bdOU8yUNiBNpkmQ7cbWNGR3b0gmqGgIc7GOqrAuiD-12DX24JlGvn1uGcU2'

        if msg_head and target and msg_body:
            try:
                result = FCMNotification(api_key=server_key).notify_multiple_devices(registration_ids=[reg_id], message_title=msg_head, message_body=msg_body)
            except:
                return HttpResponse('Error')
            return HttpResponse(result)
        else:
            return HttpResponse('Please Fill all the fields')