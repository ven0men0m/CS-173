from django.urls import include, path
from .views import (
	ClassroomListView,
	ClassroomDetailView,
	ClassroomCreateView,
	ClassCreateView,
	)
from . import views

urlpatterns = [
	path('classroom/list/', ClassroomListView.as_view(), name='list'),
	path('classroom/<int:pk>/', ClassroomDetailView.as_view(), name='detail'),
	path('classroom/new/', ClassroomCreateView.as_view(), name='classroom-create'),
	path('class/new/', ClassCreateView.as_view(), name='class-create')
]