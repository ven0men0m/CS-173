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