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
from gramophorn.records.models import Disk
from gramophorn.records.models import Track
from gramophorn.records.models import Role
from gramophorn.records.models import Credit

from gramophorn.util.extra_add import SelectWithPop
from gramophorn.util.extra_add import handle_pop_add

def list(request):
    collections = Collection.objects.all().order_by('-id')[:5]
    albums = Album.objects.all().order_by("-id")[:5]

    return render_to_response("records/list.html", {'collections': collections, 'albums':albums, }, RequestContext(request))


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        widgets= {
            'collection':SelectWithPop,
            'label': SelectWithPop,
            'notes': forms.Textarea
        }

class AlbumForm(forms.ModelForm):
    num_disk = forms.IntegerField(label="Number of disks on this album")
    class Meta:
        model = Album
        widgets= {
            'collection':SelectWithPop,
            'label': SelectWithPop,
            'notes': forms.Textarea
        }

class DiskForm(forms.ModelForm):
    class Meta:
        model = Disk
        widgets= {
            'album':SelectWithPop,
            'notes': forms.Textarea,
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        widgets= {
            'notes': forms.Textarea,
        }

class TrackForm(forms.ModelForm):
    lead = forms.ModelChoiceField(Person.objects.all(), widget=SelectWithPop ,required=False, label="Lead Musician")
    class Meta:
        model = Track
        exclude =['notes',]

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

MODELS = ['collection', 'album', 'person', 'label', 'role']
def get_form(model):
    if not model in MODELS:
        return PersonForm
    return [CollectionForm,AlbumForm,PersonForm, LabelForm][MODELS.index(model)] 

def get_related_url(model,instance):
    if model == "collection":
        return "/records/album/new/?collection=%d"% instance.id
    if model == "album":
        return "/records/disk/new/%d/"% instance.id

def new(request, model):
    ok = request.GET.get("ok",0)
    related = request.POST.get("related",False)
    if request.method == "POST":
        form = get_form(model)(request.POST)
        if form.is_valid():
            try:
                new_object = form.save()
            except forms.ValidationError, error:
                new_object = None
            if new_object:
                if model == "album":
                    for i in range(form.cleaned_data['num_disk']):
                        disk = Disk()
                        disk.num_disk = i + 1
                        disk.album = new_object
                        disk.save()
                    return HttpResponseRedirect(get_related_url(model, new_object))
                if related: 
                    return HttpResponseRedirect(get_related_url(model, new_object))
                return HttpResponseRedirect("/records/%s/new/?ok=1"%model)
                

    else:
        form = get_form(model)(request.GET)
    
    return render_to_response("records/new.html", {'form': form, 'model':model, 'ok':ok}, RequestContext(request))

from django.forms.models import inlineformset_factory
def new_disk(request, album_id):
    album = Album.objects.get(id=album_id)
    DiskInlineFormSet = inlineformset_factory(Album, Disk, extra=0)
    if request.method == "POST":
        formset = DiskInlineFormSet(request.POST, request.FILES, instance=album)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/records/disk/new/%d/"% album.id)
    else:
        formset = DiskInlineFormSet(instance=album)
    return render_to_response("records/new_disk.html", {
        "formset": formset,
        "album": album,
    }, RequestContext(request))


def new_tracks(request, disk_id):
    disk = Disk.objects.get(id=disk_id)
    TrackInlineFormSet = inlineformset_factory(Disk, Track, form=TrackForm, extra=4)
    if request.method == "POST":
        formset = TrackInlineFormSet(request.POST, request.FILES, instance=disk)
        if formset.is_valid():
            formset.save()
            lead_role = Role.objects.get(id=1)
            for form in formset.forms:
                if form.instance.id:
                    credit = Credit()   
                    credit.track = form.instance
                    credit.person = form.fields["lead"]
                    credit.role = lead_role
                    credit.save()
                    form.cleaned_data['lead'] = None
                   
    else:
        formset = TrackInlineFormSet(instance=disk)
    return render_to_response("records/new_tracks.html", {
        "formset": formset,
        "disk": disk,
    }, RequestContext(request))

def add(request, model):
    return handle_pop_add(request,get_form(model), model)



def edit(request):
    pass

def destroy(request):
    pass

