# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from .models import Employees


# Create your views here.
def home(request):
    employees = Employees.objects.all()
    return render(request, 'home.html', {'employees': employees})


def employee_detail(request, employee_id):
    try:
        employee = Employees.objects.get(id=employee_id)
    except Employees.DoesNotExist:
        raise Http404('Employee not found')
    return HttpResponse(request, 'employee-detail.html', {'employee': employee})
