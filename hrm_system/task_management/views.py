from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, TaskAssignment
from .forms import TaskForm, TaskAssignmentForm
from django.db.models import Q

# Dashboard View
@login_required
def dashboard(request):
    tasks = TaskAssignment.objects.filter(assigned_by=request.user)
    
    # Handle filters
    employee_filter = request.GET.get('employee', None)
    status_filter = request.GET.get('status', None)
    date_from = request.GET.get('from', None)
    date_to = request.GET.get('to', None)

    # Filter tasks by employee
    if employee_filter:
        tasks = tasks.filter(employee__id=employee_filter)
    
    # Filter tasks by status
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    
    # Filter tasks by date range
    if date_from and date_to:
        tasks = tasks.filter(assigned_date__range=[date_from, date_to])
    elif date_from:
        tasks = tasks.filter(assigned_date__gte=date_from)
    elif date_to:
        tasks = tasks.filter(assigned_date__lte=date_to)

    # Count statistics for tasks
    completed_tasks = tasks.filter(status=TaskAssignment.COMPLETED).count()
    pending_tasks = tasks.filter(status=TaskAssignment.PENDING).count()
    in_progress_tasks = tasks.filter(status=TaskAssignment.IN_PROGRESS).count()

    # Calculate total tasks based on the filters
    total_tasks = tasks.count()

    return render(request, 'task_management/dashboard.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
        'total_tasks': total_tasks,  # Pass total tasks to the template
    })


# Create Task View
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'task_management/create_task.html', {'form': form})

# Update Task View
@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_management/update_task.html', {'form': form})

# Delete Task View
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')

    return render(request, 'task_management/delete_task.html', {'task': task})

# task_management/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TaskAssignment
from .forms import TaskForm, TaskAssignmentForm
from django.contrib.auth.decorators import login_required

@login_required
def assign_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskAssignmentForm(request.POST, user=request.user)  # Pass the current user
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.task = task
            assignment.save()
            return redirect('dashboard')  # Redirect to dashboard after assignment
    else:
        form = TaskAssignmentForm(user=request.user)  # Pass the current user
    
    return render(request, 'assign_task.html', {'form': form, 'task': task})
from django.shortcuts import render, get_object_or_404
from .models import Task

# Task Details View
@login_required
def task_details(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_management/task_details.html', {'task': task})
from django.shortcuts import get_object_or_404, redirect
from .models import TaskAssignment

# View to mark a task as completed
def mark_as_completed(request, task_assignment_id):
    task_assignment = get_object_or_404(TaskAssignment, id=task_assignment_id)
    
    # Update the task's status to "Completed"
    task_assignment.status = 'Completed'  # Ensure the status is updated
    task_assignment.save()

    # Redirect back to the task dashboard
    return redirect('dashboard')  # Ensure this matches your URL pattern name for the dashboard
def leave_management(request):
    # Logic for leave management
    return render(request, 'task_management/leave_management.html')  # Use your template here

# View for Performance Review
def performance_review(request):
    # Logic for performance review
    return render(request, 'task_management/performance_review.html')  



