from django.db import models

# Create your models here.

NOTIFICATION_TARGET = (
('1', 'Teacher'),
('2', 'HM'),
('3', 'Block Admin'),
('4', 'District Admin'),
('5', 'State Admin'),
)

class Users(models.Model):

    name = models.CharField(max_length=40)
    role = models.CharField(max_length=1,choices=NOTIFICATION_TARGET,default='1')
    email = models.EmailField()
    age = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Notifications(models.Model):
    
    target = models.CharField(max_length=1,choices=NOTIFICATION_TARGET,default='1')
    msg_head = models.CharField(max_length=30)
    msg_body = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.target

class FCMToken(models.Model):
    fcm_token = models.CharField(max_length=100)

    def __str__(self):
        return self.fcm_token