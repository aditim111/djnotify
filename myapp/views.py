from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import settings
from django.contrib import auth
from .models import Truck,Notification
import datetime

@login_required
def home(request):    

    def sendnotifications(self):
        trucks = Truck.objects.all()
        
        for truck in trucks:
            number=truck.truck_id
            insurance=truck.insurance_id
            insurance_expiry_date = truck.insurance_expiry
            current_user = auth.get_user(request)
            now = datetime.datetime.now()
            mdate=truck.insurance_expiry.strftime('%Y-%m-%d')
            rdate = now.strftime('%Y-%m-%d')
            mdate1 = datetime.datetime.strptime(mdate, "%Y-%m-%d").date()
            rdate1 = datetime.datetime.strptime(rdate, "%Y-%m-%d").date()
            delta =  (mdate1 - rdate1).days
            if delta == 30 or 15 or 7:
            	obj,notification=Notification.objects.get_or_create(user_id=current_user, truck_id=truck)
            	if notification is True:
                	obj.save()

    sendnotifications(request)
    context = {
        'trucks':Truck.objects.all,
        'notifications':Notification.objects.all(),
        }
    return render(request,"index.html",context)



@login_required
def mark_as_read(request):
    notifications=Notification.objects.all()
    for notification in notifications:
        truck=notification.truck_id
        obj1=Notification.objects.get(truck_id=truck)
        obj1.is_read=True
        obj1.save()

    return HttpResponseRedirect(reverse('home'))