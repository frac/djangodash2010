# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404,Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django import forms
from django.template import RequestContext

from gramophorn.records.models import Collection
from gramophorn.records.models import Album
from gramophorn.records.models import Person

def list(request):
    collections = Collection.objects.all()[:5]
    albums = Album.objects.all()[:5]
    people = Person.objects.all()[:5]

    return render_to_response("records/list.html", {'collections': collections, 'albums':albums, 'people':people}, RequestContext(request))

def create(request):
    pass

def edit(request):
    pass

def destroy(request):
    pass

