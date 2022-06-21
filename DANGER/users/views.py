from django.shortcuts import render, redirect
from flask import Response
from .forms import UserForm
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.

from .models import *
def add_user(request):
	submitted = False
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_user?submitted=True')
	else:
		form = UserForm
		if 'submitted' in request.GET:
			submitted = True
		
	form = UserForm
	return render(request, 'pages/add_user.html', {'form':form,'submitted':submitted})


def list_user(request):
     user_list = User.objects.all()
     return render(request, 'pages/show-users.html', {'user_list':user_list}) 


def delete_user(request, user_id):
	user = User.objects.get(pk=user_id)
	user.delete()
	return redirect('/list_user')	



def update_user(request, user_id):
	user = User.objects.get(pk=user_id)
	form = UserForm(request.POST or None, request.FILES or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('/list_user')

	return render(request, 'pages/update_user.html', 
		{'user': user,
		'form':form})




		