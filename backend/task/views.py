from django.shortcuts import render
# import Views sets from REST framework
from rest_framework import viewsets

# import the TaskSerializer
from .serializers import TaskSerializer

# import the Task model
from .models import Task

# create a class for the Task model viewsets
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
# Create your views here.
