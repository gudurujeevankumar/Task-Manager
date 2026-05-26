from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='dashboard', permanent=False)),
    
    # Auth urls
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    
    # Task manager urls
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('tasks/create/', views.task_create_view, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_edit_view, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete_view, name='task_delete'),
    path('tasks/<int:pk>/move/<str:direction>/', views.task_move_view, name='task_move'),
]
