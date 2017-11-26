# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render


from django.http import HttpResponse, JsonResponse

from .models import News, TreatmentType, Treatment, Employee



def index(request):
    
    news = News.objects.order_by('-id')[:4]
    context = {
        'news' : news
    }
    return render(request, 'salon/index.html', context)

def newsDetail(request, News_id):
    story = get_object_or_404(News, pk=News_id)

    context = {
        'story' : story
    }

    return render(request, 'salon/newsDetail.html', context)



def treatmentView(request):

    if request.is_ajax():
        treatmentType = request.GET.get('treatmentType')
        
        if int(treatmentType) == 0:
            treatments = Treatment.objects.all().order_by('length')
        else:
            treatments = Treatment.objects.filter(treatmentType_id=treatmentType)
        
        context = {
            'treatments' : treatments
        }

        return render(request, 'salon/treatmentList.html', context)


    treatmentTypes = TreatmentType.objects.all()
    treatments = Treatment.objects.all().order_by('length')

    context = {
        'treatmentTypes' : treatmentTypes,
        'treatments' : treatments
    }
    return render(request, 'salon/treatments.html', context)


def employeeView(request):

    employees = Employee.objects.all()

    context = {
        'employees' : employees
    }

    return render(request,'salon/employees.html', context)