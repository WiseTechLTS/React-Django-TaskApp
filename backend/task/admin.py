from django.contrib import admin
from .models import Task
# Register your models here.

# create Class for Task admin-model integration
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'task_image')
    
# create Class for TaskImage admin-model integration
    
# register TaskAdmin and TaskImageAdmin

admin.site.register(Task, TaskAdmin)