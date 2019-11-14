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
	location = models.CharField(max_length=100, verbose_name='Location', null=True)
	classroomImage = models.ImageField(upload_to='Images/%Y/%m/%d', verbose_name='Classroom Image', null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.id})

class Vote(models.Model):
	voteNo = models.IntegerField(null=True)
	semester = models.CharField(max_length=5, verbose_name='Semester (eg. 1920A)')
	classroomName = models.ForeignKey(Classrooms, on_delete=models.CASCADE, verbose_name='Classroom')
	className = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name='Class')

	def __str__(self):
		return self.className.name + '_' + self.classroomName.name