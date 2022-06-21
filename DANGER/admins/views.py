from django.shortcuts import render, redirect
from flask import Response
from .forms import AdminForm
from .models import Admin
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
# Create your views here.

from .models import *
def add_admin(request):
	submitted = False
	if request.method == 'POST':
		form = AdminForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_admin?submitted=True')
	else:
		form = AdminForm
		if 'submitted' in request.GET:
			submitted = True
		
	form = AdminForm
	return render(request, 'pages/add_admin.html', {'form':form,'submitted':submitted})




def list_Admin(request):
     admin_list = Admin.objects.all()
     return render(request, 'pages/show.html', {'admin_list':admin_list}) 


def delete_admin(request, admin_id):
	admin = Admin.objects.get(pk=admin_id)
	admin.delete()
	return redirect('/list_admin')	



def update_admin(request, admin_id):
	admin = Admin.objects.get(pk=admin_id)
	form = AdminForm(request.POST or None, request.FILES or None, instance=admin)
	if form.is_valid():
		form.save()
		return redirect('/list_admin')

	return render(request, 'pages/update_admin.html', 
		{'admin': admin,
		'form':form})


def count_admin(request):
    admin_count = Admin.objects.count()
    return render(
        request, 'pages/index.html', {'admin_count': admin_count}
    )

	
        
	    