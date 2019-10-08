from django.urls import include, path
from .views import (
	ClassroomListView,
	)
from . import views

urlpatterns = [
	path('', ClassroomListView.as_view(), name='list'),
]