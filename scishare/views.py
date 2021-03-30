# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    context_dict = {'boldmessage': 'context dictionary'}
    return render(request, 'scishare/home.html', context=context_dict)


def register(request):
    return HttpResponse("Register page.")


def login(request):
    return HttpResponse("Login page.")


#visible only after log in
@login_required
def search_results(request):
    return HttpResponse("show search results")


@login_required
def categories(request):
    context_dict = {'boldmessage': 'context dictionary'}
    return render(request, 'scishare/categories.html', context=context_dict)


@login_required
def add_category(request):
    return HttpResponse("add category form")


@login_required
def show_category(request):
    return HttpResponse("show category studies")


@login_required
def add_study(request):
    return HttpResponse("add study")


@login_required
def most_liked(request):
    context_dict = {'boldmessage': 'context dictionary'}
    return render(request, 'scishare/most_liked.html', context=context_dict)


@login_required
def groups(request):
    return HttpResponse("list of groups")


@login_required
def create_group(request):
    return HttpResponse("create a group")


@login_required
def show_group(request):
    return HttpResponse("show list of pages of the group")

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('scishare:home'))





