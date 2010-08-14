# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404,Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django import forms

from django.core.management import call_command


def install(request):
    call_command('syncdb', verbosity=0, interactive=False)
    return HttpResponseRedirect("/")
                

def create(request):
    pass

def edit(request):
    pass

def destroy(request):
    pass

