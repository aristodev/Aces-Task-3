# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms


# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def __str__(self):
        return self.username

class question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)

    def __str__(self):
        return self.question

class test(models.Model):
    User = models.ForeignKey(user)
    Question = models.ForeignKey(question)
    answer = models.CharField(max_length=150)

    def __str__(self):
        return "username : {} | Question : {}".format(self.User, self.Question)



