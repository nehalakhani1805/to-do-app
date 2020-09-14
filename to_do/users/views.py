from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, TaskCreateForm, TaskUpdateForm
from django.contrib import messages
from appone.models import Task
from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def register(request):
	if(request.method=='POST'):
		form=UserRegisterForm(request.POST)
		if(form.is_valid()):
			print("is valid")
			form.save()
			messages.success(request,f'Welcome')
			return redirect('login')
		#else:
			#print(form.errors())
	else:
		form=UserRegisterForm()
	return render(request, 'users/register.html',{'form':form})

@login_required
def tasks(request):
	u=request.user
	tasks=u.task_set.all()
	#tasks=Task.objects.all();
	if request.method=='POST':
		form=TaskCreateForm(request.POST)
		form.instance.owner=request.user
		if form.is_valid():
			form.save()
			return redirect('tasks')
	else:
		form=TaskCreateForm()
	return render(request,'users/tasks.html',{'tasks':tasks,'form':form})
@login_required
def profile(request):
	if(request.method=='POST'):
		form=UserUpdateForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request,f'Updated')
			return redirect('profile')			
	else:
		form=UserUpdateForm(instance=request.user)
	return render(request,'users/profile.html',{'form':form})

@login_required
def cross(request, id):
	task=Task.objects.get(id=id)
	print(task.todo)
	print(task.done)
	if task.done==True:
		task.done=False
	else:
		task.done=True
	print(task.done)
	task.save()
	return redirect ('tasks')

@login_required
def delete(request, id):
	task=Task.objects.get(id=id)
	task.delete()
	return redirect ('tasks')

@login_required
def edit(request, id):
	task=Task.objects.get(id=id)
	if request.method=='POST':
		print("hi1")
		form=TaskUpdateForm(request.POST,instance=task)
		print("hi2")
		form.instance.owner=request.user
		print("hi3")
		if form.is_valid():
			print("hi4")
			#form.save()
			task.todo=form.instance.todo
			task.save()
			return redirect('tasks')
	else:
		print("hi5")
		form=TaskUpdateForm(instance=task)
	return render(request,'appone/task_form.html',{'tasks':tasks,'form':form})

class TaskUpdateView(LoginRequiredMixin, UpdateView):
	model=Task
	fields=['todo']

	def form_valid(self,form):
		form.instance.owner=self.request.user
		return super().form_valid(form)



