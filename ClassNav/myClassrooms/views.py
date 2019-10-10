from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Classes, Classrooms
# Create your views here.

class ClassroomListView(ListView):
	model = Classrooms
	template_name = 'myClassrooms/classroom_list.html'
	context_object_name = 'classroom'
	ordering = ['upVote']

class ClassroomDetailView(DetailView):
	model = Classrooms
	context_object_name = 'classroom'

class ClassroomCreateView(CreateView):
	model = Classrooms
	fields = ['name', 'course', 'upVote', 'location', 'classroomImage']
	success_url = '/classroom/list'

class ClassCreateView(CreateView):
	model = Classes
	fields = ['name']
	success_url = '/classroom/list'