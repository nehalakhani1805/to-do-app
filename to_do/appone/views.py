from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.
def home(request):
	tasks=Task.objects.all()
	return render(request,'appone/home.html',{'title':'Home Page','tasks':tasks})

def about(request):
	return render(request,'appone/about.html',{'title':'About Page'})
