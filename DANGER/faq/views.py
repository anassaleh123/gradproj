from django.shortcuts import render, redirect
from flask import Response
from .forms import FaqForm
from .models import Faq
from django.http import HttpResponseRedirect


# Create your views here.
def add_faq(request):
	submitted = False
	if request.method == 'POST':
		form = FaqForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_faq?submitted=True')
	else:
		form = FaqForm
		if 'submitted' in request.GET:
			submitted = True
		
	form = FaqForm
	return render(request, 'pages/add_faq.html', {'form':form,'submitted':submitted})




def list_faq(request):
     faq_list = Faq.objects.all()
     return render(request, 'pages/show-faq.html', {'faq_list':faq_list}) 