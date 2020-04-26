from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import *

from pyfcm import FCMNotification

# Create your views here.

def home(request):
    template = 'home.html'
    return render(request,template)

def send_email(request):
    if request.method == 'POST':
        to_email = [request.POST.get('email')]
        msg = request.POST.get('msg')
        subject = request.POST.get('sbj')
        from_email = settings.EMAIL_HOST_USER
        html_message = render_to_string('mail_template.html', {'body': msg,'name':'Gaurav','email':from_email,'contact':'+911234567890'})
        message = strip_tags(html_message)

        if subject and msg and from_email and to_email:
            try:
                email = EmailMultiAlternatives(subject,message,from_email,to_email)
                email.attach_alternative(html_message, "text/html")
                email.attach_file('debug.log')
                email.send(fail_silently=False)
                EmailUsers.objects.create(to_email=to_email,from_email=from_email,message = msg, subject=subject)
            except:
                return HttpResponse('Invalid header found or Check your Email')
            return HttpResponse('Email is Sent SuccessFully')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

def fcm_insert(request): 
    token = request.GET.get("fcm_token")
    FCMToken.objects.create(fcm_token=token)
    return JsonResponse("Success")
            
def send_notif(request):
    if request.method == 'POST':
        msg_head = request.POST.get('msg_head')
        msg_body = request.POST.get('msg_body')
        target_id = request.POST.get('target_id')

        server_key = settings.SERVER_KEY
        reg_id = FCMToken.objects.filter(pk=target_id).values()[0]

        if msg_head and reg_id and msg_body:
            try:
                pusher = FCMNotification(api_key=server_key)
                result = pusher.notify_multiple_devices(registration_ids=[reg_id], message_title=msg_head, message_body=msg_body)
            except:
                return JsonResponse('Failed')
            return JsonResponse('Success')
        else:
            return JsonResponse('Please Fill all the fields')