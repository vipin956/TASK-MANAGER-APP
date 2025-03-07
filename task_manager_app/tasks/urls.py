from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.view_all_tasks,name='home'),
    path('time/', views.time,name='time'),
    path('add/',views.add_task,name='add'),
    path('edit/<int:id>',views.edit_task,name='edit'),
    path('delete/<int:id>',views.delete_task,name='delete'),
    path('task_id/<int:id>',views.get_task_by_id,name='task_id'),
    path('filter/<str:priority>',views.filter_task_by_priority,name='filter'),
]