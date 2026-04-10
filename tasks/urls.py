from django.urls import path
from .views import health_check,task_list,task_detail

urlpatterns = [
    path('health/',health_check),
    path('tasks/',task_list),
    path('tasks/<int:pk>/',task_detail),
]
