from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Form(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    
    
class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    text = models.TextField()
    is_required = models.BooleanField(default=False)
    question_type = models.CharField(max_length=300,choices = [
    ("test", "test"),
    ("Descriptive", "Descriptive"),
    ],null = True, blank = True)
    
    def __str__(self):
        return self.text
    
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    # answer_type = models.CharField(max_length=300)
    order = models.IntegerField(default=0) 
    
    
    def __str__(self):
        return self.text

    
    
class Applicant(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    
    
    def __str__(self):
        return self.first_name
    


class ApplicantAnswer(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    

class ApplicantForm(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField()
    raise_token = models.CharField(max_length=16)
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)