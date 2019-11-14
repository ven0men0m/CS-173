from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Classes, Classrooms, Vote
from django.http import HttpResponseRedirect
# Create your views here.

class ClassroomListView(ListView):
	model = Classrooms
	template_name = 'myClassrooms/classroom_list.html'
	context_object_name = 'classroom'
	paginate_by = 10

	def get_queryset(self):
		cName = self.request.GET.get('class_name', '')
		new_context = Classrooms.objects.filter(vote__className__name__contains=cName).order_by('-vote__voteNo')
		print(new_context)
		return new_context

	def get_context_data(self, **kwargs):
		context = super(ClassroomListView, self).get_context_data(**kwargs)
		context['class_name'] = self.request.GET.get('filter', '')
		print(context)
		return context

class ClassroomDetailView(DetailView):
	model = Classrooms
	context_object_name = 'classroom'

class ClassroomCreateView(CreateView):
	model = Classrooms
	fields = ['name', 'course', 'location', 'classroomImage']
	success_url = '/classroom/list'

class ClassCreateView(CreateView):
	model = Classes
	fields = ['name']
	success_url = '/classroom/list'