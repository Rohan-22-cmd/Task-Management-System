# task_management/forms.py
from django import forms
from .models import Task, TaskAssignment  # Import models only when necessary

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_description', 'task_priority', 'start_date', 'end_date', 'task_type']
class TaskAssignmentForm(forms.ModelForm):
    class Meta:
        model = TaskAssignment
        fields = ['employee', 'status', 'assigned_by', 'completed_at']
