# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import gettext as _


# Create your models here.


class Truck(models.Model):
    truck_id = models.CharField(max_length=10)
    insurance_id = models.CharField(max_length=10, null=True,blank=True)
    insurance_expiry = models.DateField(null=True,blank=True)
    def __str__(self):
        title = _('The insurance of truck %(truck)s with insurance number %(insurance)s is going to expire on %(date)s')
        return title % {'truck': self.truck_id, 'insurance': self.insurance_id, 'date':self.insurance_expiry}

class Notification(models.Model):
    truck_id = models.ForeignKey(Truck)
    user_id= models.ForeignKey(User, null=True,blank=True)
    is_read = models.BooleanField(_('Is read?'), default=False)
    def __str__(self):
        title = _('%(truck)s! Please renew it.')
        return title % {'truck': self.truck_id}


