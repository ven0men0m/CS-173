from django.contrib import admin
from .models import Classes, Classrooms, Vote
# Register your models here.

admin.site.register(Classes)
admin.site.register(Classrooms)
admin.site.register(Vote)
