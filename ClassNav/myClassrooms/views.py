from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Classes, Classrooms, Vote
from django.http import HttpResponseRedirect
from django.db.models import F
# Create your views here.

class ClassroomListView(ListView):
	model = Classrooms
	template_name = 'myClassrooms/classroom_list.html'
	context_object_name = 'classroom'
	paginate_by = 10

	def get_queryset(self):
		cName = self.request.GET.get('class_name', '')
		if not cName or cName == None:
			new_context = Classrooms.objects.all()
		else:
			new_context = Classrooms.objects.filter(vote__className__name__icontains=cName).order_by('-vote__voteNo')
		print(cName)
		print(new_context)
		print('')
		return new_context

	def get_context_data(self, **kwargs):
		context = super(ClassroomListView, self).get_context_data(**kwargs)
		cName = self.request.GET.get('filter', '')
		context['classes'] = Classes.objects.filter(vote__className__name__icontains=cName)
		print(context)
		return context

class ClassroomDetailView(DetailView):
	model = Classrooms
	context_object_name = 'classroom'

	def get_context_data(self, **kwargs):
		context = super(ClassroomDetailView, self).get_context_data(**kwargs)
		obj = context['object']
		print("yowp")
		print(obj.location)
		clName = obj.name
		context['classes'] = Classes.objects.filter(vote__classroomName__name__icontains=clName)
		context['vote'] = Vote.objects.filter(classroomName__name__icontains=clName)
		print(context)
		return context

class ClassroomCreateView(CreateView):
	model = Classrooms
	fields = ['name', 'location', 'classroomImage']
	success_url = '/classroom/list'

class ClassCreateView(CreateView):
	model = Classes
	fields = ['name']
	success_url = '/classroom/list'

class VoteCreateView(CreateView):
	model = Vote
	context_object_name = 'vote'
	fields = ['voteNo', 'semester', 'classroomName', 'className']
	success_url = '/classroom/list'

	def get_context_data(self, **kwargs):
		context = super(VoteCreateView, self).get_context_data(**kwargs)
		print(context)
		return context