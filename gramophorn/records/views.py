# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404,Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django import forms
from django.template import RequestContext

from gramophorn.records.models import Collection
from gramophorn.records.models import Album
from gramophorn.records.models import Person
from gramophorn.records.models import Label

from gramophorn.util.extra_add import SelectWithPop
from gramophorn.util.extra_add import handle_pop_add

def list(request):
    collections = Collection.objects.all()[:5]
    albums = Album.objects.all()[:5]
    people = Person.objects.all()[:5]

    return render_to_response("records/list.html", {'collections': collections, 'albums':albums, 'people':people}, RequestContext(request))


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        widgets= {
            'collection':SelectWithPop,
            'label': SelectWithPop,
            'notes': forms.Textarea
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        widgets= {
            'collection':SelectWithPop,
            'label': SelectWithPop,
            'notes': forms.Textarea
        }

class PersonForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = Person
        widgets= {
            'notes': forms.Textarea
        }

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        widgets= {
            'notes': forms.Textarea
        }

MODELS = ['collection', 'album', 'person', 'label']
def get_form(model):
    if not model in MODELS:
        return None
    return [CollectionForm,AlbumForm,PersonForm, LabelForm][MODELS.index(model)] 

def new(request, model):
    ok = request.GET.get("ok",0)
    if request.method == "POST":
        form = get_form(model)(request.POST)
        if form.is_valid():
            try:
                newObject = form.save()
            except forms.ValidationError, error:
                newObject = None
            if newObject:
                return HttpResponseRedirect("/records/%s/new/?ok=1"%model)

    else:
        form = get_form(model)()
    
    return render_to_response("records/new.html", {'form': form, 'model':model, 'ok':ok}, RequestContext(request))

def add(request, model):
    return handle_pop_add(request,get_form(model), model)



def edit(request):
    pass

def destroy(request):
    pass

