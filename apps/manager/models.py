# -*- coding: utf-8 -*-
"""Models - Everything Else"""
from __future__ import unicode_literals
from django.db import models
from ..users.models import *
import bcrypt
import re
# Create your models here.
#Address


class AddressManager(models.Manager):
    def address_val(self, postData):
        errors = {}
        #Address1 can't be empty
        #City can't be empty
        #State must be part one of the state abbreviations
        #zip MUST be length 5 AND digits
        return errors

class Address(models.Model):
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    apt_num = models.CharField(max_length=25)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)#KEY IN VALIDATION
    zip = models.CharField(max_length=5)#digits ONLY REGEX
    objects = AddressManager()


class SourceManager(models.Manager):
    def type_val(self, postData):
        errors = {}
        #name and desc can't be null
        return errors

    def source_val(self, postData):
        errors = {}
        #name, desc, type can't be null
        #If type's hasProperty==false, trade_by and bank_by MUST BE NULL
        #If type's hasProperty==true, then trade_by and bank_by don't have to be null
        return errors

    def currency_val(self, postData):
        errors = {}
        #abbrev has to be >1
        #name can't by < 5
        #duration CAN be NULL
        #source CAN'T be NULL
        #Must be 0,1,2
        return errors

    def propType_val(self, postData):
        errors = {}
        #name, rules_url, source, 
        return errors
#Source Type(admin)
class SourceType(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    hasProperty = models.BooleanField(default=True)# Boolean on whether source has property
    objects = SourceManager()

#Source
class Source(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    login_url = models.CharField(max_length=255)
    source_type = models.ForeignKey(SourceType, realted_name="sources")
    exp_Rules = models.TextField()
    trade_by = models.DateTimeField()#Default dates if trade/bank an option for this source
    bank_by = models.DateTimeField()#Default dates if trade/bank an option for this source
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SourceManager()


#Currency
class Currency(models.Model):
    abbrev = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()#months that the points stay valid
    source = models.ForeignKey(Source, realted_name="currencies")
    trade_bank = models.IntegerField()#can only be 0,1,2, see readme
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SourceManager()

#Source's Property Types
class PropType(models.Model):
    name = models.CharField(max_length=100)
    rules = models.TextField()
    rules_url = models.CharField(max_length=100)
    source = models.ForeignKey(Source, realted_name="prop_types")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SourceManager()

#Validator Manager
class PropertyManager(models.Manager):
    def property_val(self, postData):
        errors = {}
        #name,address,prop_type,frequency
        return errors
#Property - user_id
class Property(models.Model):
    user = models.ForeignKey(User, realted_name="properties")
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, realted_name="properties")
    prop_type = models.ForeignKey(PropType, realted_name="properties")
    frequency = models.IntegerField()#only 1:annual or 2: biannual
    isEven = models.BooleanField(default=False)#Only visible if frequency==2
    hasLockoff = models.BooleanField(default=False)
    trade_val = models.DecimalField(max_digits=None, decimal_places=2)
    bank_val = models.DecimalField(max_digits=None, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PropertyManager()

#PropVals
class PropValue(models.Model):
    value = models.DecimalField(max_digits=None, decimal_places=2)
    currency = models.ForeignKey(Currency, realted_name="prop_vals")
    prop = models.ForeignKey(Property, realted_name="prop_vals")
    isLockoff = models.BooleanField(default=False)
    objects = PropertyManager()
    #Created/Updated at on property
    

class AccountManager(models.Manager):
    def account_val(self, postData):
        errors = {}
        #name,address,prop_type,frequency
        return errors
#Account
class Account(models.Model):
    nick = models.CharField(max_length=100)
    username = models.CharField(max_length=100)####encrypt
    source = models.ForeignKey(Source, realted_name="accounts")
    login_url = models.CharField(max_length=100)
    total_pts = models.IntegerField()
    hasChanged = models.BooleanField(default=False)##If account tied to properties, then
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AccountManager()

#Account_Points
class AccountPoint(models.Model):
    points = models.IntegerField()
    currency = models.ForeignKey(Currency, realted_name="available points")

#Usable_Points Status(admin)
#Usable_Points
