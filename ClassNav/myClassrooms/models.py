from django.db import models
from django.contrib.auth.models import User
from datetime import date 

# Create your models here.
class Classes(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 20, verbose_name='Class Name')

	def __str__(self):
		return self.name

class Classrooms(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100, verbose_name='Classroom Name')
	course = models.ManyToManyField(Classes, related_name='classrooms')
	upVote = models.IntegerField(null=True)
	location = models.CharField(max_length=100, verbose_name='Location', null=True)
	classroomImage = models.ImageField(upload_to='Images/%Y/%m/%d', verbose_name='Classroom Image', null=True)

	def __str__(self):
		return self.name