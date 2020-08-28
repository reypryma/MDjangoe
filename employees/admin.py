# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Employees, AvailableJobs


# Register your models here.
@admin.register(Employees, AvailableJobs)
class EmployeeAdmin(admin.ModelAdmin):
    pass
