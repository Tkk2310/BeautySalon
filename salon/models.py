# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    dateCreated = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.title



class TreatmentType(models.Model):
    label = models.CharField(max_length=200)

    def __unicode__(self):
        return self.label


class Treatment(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    length = models.IntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=1)
    treatmentType = models.ForeignKey(TreatmentType,on_delete=models.PROTECT, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1500)
    picture = models.ImageField(upload_to = 'images/employees/')

    def __unicode__(self):
        return self.name