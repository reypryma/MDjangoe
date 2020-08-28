# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('Welcome Home')


def employee_detail(request, employee_id):
    return HttpResponse(f'Employee ID: {employee_id}')
