#coding:utf8
from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=256)
    notes = models.CharField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return self.title

class Album(models.Model):
    collection = models.ForeignKey('Collection', null=True, blank=True)
    label = models.ForeignKey('Label', null=True, blank=True)
    title = models.CharField(max_length=256)
    alt_title = models.CharField(max_length=256, null=True, blank=True)
    label_issue_number = models.CharField(max_length=256, null=True, blank=True)
    date_event = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=256, null=True, blank=True)

    def __unicode__(self):
        return self.title

SPEEDS = [(0,"33⅓ rpm"), (1,"45 rpm"), (2, "78 rpm")]
SIZES = [(0,"12 in. / 30 cm"), (1,"10 in. / 25 cm"), (2, "7 in. / 17.5 cm")]
TYPES = [(0,"LP"), (1,"EP"), (2, "Single"), (3, "Maxi Single")]


class Disk(models.Model):
    album = models.ForeignKey('Album')
    disk_num = models.IntegerField(default=1)
    disk_speed = models.IntegerField(choices=SPEEDS)
    disk_size  = models.IntegerField(choices=SIZES)
    disk_type  = models.IntegerField(choices=TYPES)
    notes = models.CharField(max_length=256, null=True, blank=True)
    
    def __unicode__(self):
        return u"disk %s"% self.disk_num

SIDES = [(0,"Side A"), (1,"Side B")]

class Track(models.Model):
    disk = models.ForeignKey('Disk')
    title = models.CharField(max_length=256)
    track_num = models.IntegerField(null=True, blank=True)
    disk_side = models.IntegerField(choices=SIDES)
    duration = models.IntegerField(null=True, blank=True)
    date_recording = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=256, null=True, blank=True)

    def __unicode__(self):
        return self.title

class Credit(models.Model):
    track = models.ForeignKey('Track')
    person = models.ForeignKey('Person')
    role = models.ForeignKey('Role')
    notes = models.CharField(max_length=256, null=True, blank=True)

class Person(models.Model):
    name = models.CharField(max_length=256)
    birthdate = models.DateField(null=True, blank=True)
    deathdate = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=256)
    notes = models.CharField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=256)
    notes = models.CharField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return self.name

