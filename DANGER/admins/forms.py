from django.forms import ModelForm
from .models import Admin
from django import forms

class AdminForm(ModelForm):
	class Meta:
		model = Admin
		fields = '__all__'
		labels = {
			'username': 'enter username',
			'password': 'enter password',
			'email': 'enter email',
			
		}




		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}),
			'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			
		}