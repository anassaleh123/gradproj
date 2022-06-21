from django.forms import ModelForm
from .models import User
from django import forms

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'
		labels = {
			'username': 'enter username',
			'email': 'enter email',
            'address': 'enter address',
            'password': 'enter password',
            'confirm_password': 'conirm_password',
		}




		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}),
            'confirm_password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password'}),
            
		}