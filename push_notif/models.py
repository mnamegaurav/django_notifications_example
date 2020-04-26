from django.db import models

# Create your models here.

class FCMToken(models.Model):
    target_id = models.AutoField(primary_key=True)
    fcm_token = models.CharField(max_length=100)

    def __str__(self):
        return str(self.target_id)

class EmailUsers(models.Model):

    to_email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=60)
    from_email = models.EmailField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Notifications(models.Model):
    
    target_id = models.OneToOneField(FCMToken, on_delete=models.CASCADE, primary_key=True)
    msg_head = models.CharField(max_length=60)
    msg_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.msg_head