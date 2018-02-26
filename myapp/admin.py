# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Truck, Notification

admin.site.register(Truck)
admin.site.register(Notification)