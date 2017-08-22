# -*- coding: utf-8 -*-
# Create your views here.
"""users VIEWS.py"""
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import User
import bcrypt
# Create your views here.


def index(request):
    if 'id' in request.session:
        request.session.clear()
    return render(request, 'users/index.html')


def register(request):
    # if request.method == "POST":
    #     #Validate
    #     errors = User.objects.basic_validator(request.POST)
    #     if len(errors) != 0:
    #         for tag, error in errors.iteritems():  # flash messages
    #             messages.error(request, error, extra_tags=tag)
    #         #context name alias
    #         context = {
    #             'name': request.POST['name'],
    #             'alias': request.POST['alias'],
    #             'email': request.POST['email']
    #         }
    #         return render(request, 'users/index.html', context)
    #     else:
    #         #Hash password
    #         hash1 = bcrypt.hashpw(
    #             request.POST['password'].encode(), bcrypt.gensalt())
    #         #Create User(key=request.POST['key'])
    #         newUser = User(
    #             name=request.POST['name'],
    #             alias=request.POST['alias'],
    #             email=request.POST['email'],
    #             password=hash1)
    #         newUser.save()
    #         request.session['id'] = User.objects.get(
    #             email=request.POST['email']).id
    #         return redirect('/books')
    # else:
    #     return redirect('/')
    return HttpResponse("Placeholder for Register!!")


def login(request):
    # if request.method == "POST":
    #     #Validate
    #     errors = User.objects.login_validator(request.POST)
    #     if len(errors) != 0:
    #         for tag, error in errors.iteritems():  # flash messages
    #             messages.error(request, error, extra_tags=tag)
    #         context = {
    #             'lemail': request.POST['email']
    #         }
    #         return render(request, 'users/index.html', context)
    #     else:
    #         request.session['id'] = User.objects.get(
    #             email=request.POST['email']).id
    #         return redirect('/books')
    # else:
    #     return redirect('/')
    return HttpResponse("Placeholder for Login!!")

def show(request, user_id):
    # #Find name of user with
    # user = User.objects.get(id=request.session['id'])
    # context = {
    #     'name': user.name,
    #     'alias': user.alias,
    #     'email': user.email,
    #     'reviews': user.reviews.all()
    # }
    # Book.objects.filter(reviews__user=user)
    # return render(request, '/users/view.html', context)
    return HttpResponse("Placeholder for Viewing User Profile!!")
