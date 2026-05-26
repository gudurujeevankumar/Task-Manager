from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Task
from .forms import UserRegisterForm, TaskForm

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, f"Welcome back, {form.cleaned_data['username']}!")
        return super().form_valid(form)

def custom_logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome to TaskFlow.")
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = UserRegisterForm()
        
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard_view(request):
    user_tasks = Task.objects.filter(user=request.user)
    
    todo = user_tasks.filter(stage='todo')
    in_progress = user_tasks.filter(stage='in_progress')
    done = user_tasks.filter(stage='done')
    
    context = {
        'todo_tasks': todo,
        'in_progress_tasks': in_progress,
        'done_tasks': done,
        'total_count': user_tasks.count()
    }
    return render(request, 'dashboard.html', context)

@login_required
def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task created successfully!")
            return redirect('dashboard')
    else:
        form = TaskForm()
        
    return render(request, 'task_form.html', {'form': form, 'title': 'Add New Task'})

@login_required
def task_edit_view(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
        
    return render(request, 'task_form.html', {'form': form, 'title': 'Edit Task', 'task': task})

@login_required
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task_title = task.title
        task.delete()
        messages.success(request, f'Task "{task_title}" was deleted.')
    return redirect('dashboard')

@login_required
def task_move_view(request, pk, direction):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    stages = ['todo', 'in_progress', 'done']
    current_index = stages.index(task.stage)
    
    if direction == 'right' and current_index < len(stages) - 1:
        task.stage = stages[current_index + 1]
        task.save()
        messages.success(request, f'Task moved to {task.get_stage_display()}.')
    elif direction == 'left' and current_index > 0:
        task.stage = stages[current_index - 1]
        task.save()
        messages.success(request, f'Task moved to {task.get_stage_display()}.')
        
    return redirect('dashboard')
