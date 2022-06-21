from django.forms import ModelForm
from .models import Faq
from django import forms

class FaqForm(ModelForm):
	class Meta:
		model = Faq
		fields = '__all__'
		labels = {
			'questions': 'enter question',
			'answers': 'enter answer',
			
			
		}