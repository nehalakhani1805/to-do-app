from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
	todo=models.CharField(max_length=100)
	owner=models.ForeignKey(User, on_delete=models.CASCADE)
	done=models.BooleanField(default=False)
	def __str__(self):
		return self.todo + '|'+ str(self.done)

	def get_absolute_url(self):
		return reverse('tasks')

# Create your models here.
