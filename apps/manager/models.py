# -*- coding: utf-8 -*-
"""Models - Everything Else"""
from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
# Create your models here.
#Address


class AddressManager(models.Manager):
    def address_val(self, postData):
        errors = {}

class Address(models.Model):
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    apt_num = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)#KEY IN VALIDATION
    zip = models.CharField(max_length=5)#digits ONLY REGEX
    objects = AddressManager()
    
#Source Type(admin)
#Source
#Currency
#Source's Property Types
#Property
#PropVals
#Account
#Account_Points
#Usable_Points Status
#Usable_Points
