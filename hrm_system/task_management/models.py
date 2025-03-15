from django.db import models
from django.contrib.auth.models import User

# Task Model
class Task(models.Model):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]
    
    INDIVIDUAL = 'Individual'
    TEAM = 'Team'
    
    TASK_TYPE_CHOICES = [
        (INDIVIDUAL, 'Individual'),
        (TEAM, 'Team'),
    ]
    
    task_title = models.CharField(max_length=100)
    task_description = models.CharField(max_length=300)
    task_priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    task_type = models.CharField(max_length=50, choices=TASK_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_title

# Task Assignment Model
class TaskAssignment(models.Model):
    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming 'User' model for employees
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_by')
    assigned_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Task: {self.task.task_title} assigned to {self.employee.username}"
