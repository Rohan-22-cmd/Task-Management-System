from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/', views.task_details, name='task_details'),
    path('mark_as_completed/<int:task_assignment_id>/', views.mark_as_completed, name='mark_as_completed'), 
    path('leave_management/', views.leave_management, name='Leave_Management'),
    # URL pattern for "Performance Review"
    path('performance_review/', views.performance_review, name='performance_review'),
]
