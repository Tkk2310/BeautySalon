# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import News, TreatmentType, Treatment, Employee

admin.site.register(News)
admin.site.register(TreatmentType)
admin.site.register(Treatment)
admin.site.register(Employee)


# Register your models here.
