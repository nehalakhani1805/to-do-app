from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from appone.models import Task
class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
	#email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email']

class TaskCreateForm(forms.ModelForm):
	#todo=forms.CharField()
	class Meta:
		model=Task
		fields=['todo']
class TaskUpdateForm(forms.ModelForm):
	#todo=forms.CharField()
	class Meta:
		model=Task
		fields=['todo']
