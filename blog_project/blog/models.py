from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import date
import time


# Create your models here.



class UserProfile(models.Model):
    # Links to User Model Instance
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete= models.CASCADE, blank = True)
    title = models.TextField(help_text="Enter a title")
    entry = models.TextField(help_text="Enter your entry")
    date = models.DateField(auto_now_add=False, default=date.today)

    def __str__(self):
        return self.title




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileForm(forms.ModelForm):
    #Add more Attributes to User such as
    class Meta:
        model = UserProfile
        fields = []


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','entry']

