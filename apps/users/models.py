# -*- coding: utf-8 -*-
"""Users Models - Users"""
from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #Name and alias min. 3 chars
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name must have min. 3 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name must have min. 3 characters"
        if not EMAIL_REGEX.match(postData['email']) and len(postData['email']) < 7:
            errors["email"] = "Please enter a valid email"
        else:
            findUsers = User.objects.filter(email=postData['email'])
            if len(findUsers) != 0:
                errors["email"] = "Email is already in the system"
        #Password
        if len(postData['password']) < 8:
            errors["password"] = "Password min. 8 chars"
        elif postData['pw_confirm'] != postData['password']:
            errors["pw_confirm"] = "Password must match"
        return errors

    def login_validator(self, postData):
        errors = {}
        #Valid Email
        if not EMAIL_REGEX.match(postData['email']) and len(postData['email']) > 7:
            errors["email"] = "Please enter a valid email"
        else:  # Matched Email
            findUsers = User.objects.filter(email=postData['email'])
            if len(findUsers) == 0:
                errors["email"] = "Email not registered"
            else:
                #Check Password
                if not bcrypt.checkpw(postData['password'].encode("utf8"), findUsers[0].password.encode("utf8")):
                    errors["password"] = "Password min. 8 chars"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return "<User object: {}>".format(self.alias)