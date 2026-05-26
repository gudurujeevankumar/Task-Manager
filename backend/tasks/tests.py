from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task

class TaskManagerTemplateTests(TestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.dashboard_url = reverse('dashboard')
        self.create_url = reverse('task_create')
        
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword123',
            'confirmPassword': 'testpassword123'
        }
        self.user2_data = {
            'username': 'testuser2',
            'email': 'test2@example.com',
            'password': 'testpassword123',
            'confirmPassword': 'testpassword123'
        }

    def test_unauthenticated_redirects(self):
        # Unauthenticated users should be redirected to login when visiting dashboard
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.login_url, response.url)

    def test_user_registration_flow(self):
        # The UserCreationForm username validation requires username, pwd1, pwd2.
        # Django UserRegisterForm inherits from UserCreationForm.
        # Let's post fields matching UserCreationForm.
        post_data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }
        response = self.client.post(self.register_url, post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.dashboard_url)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login_flow(self):
        # Create user
        User.objects.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password']
        )
        
        # Post login credentials
        post_data = {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        }
        response = self.client.post(self.login_url, post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.dashboard_url)

    def test_task_crud_flows(self):
        # Create user and log in
        user = User.objects.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password']
        )
        self.client.force_login(user)
        
        # Create a task
        task_post_data = {
            'title': 'Test Task',
            'description': 'Test description',
            'stage': 'todo'
        }
        response = self.client.post(self.create_url, task_post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.dashboard_url)
        self.assertTrue(Task.objects.filter(title='Test Task', user=user).exists())
        
        task = Task.objects.get(title='Test Task', user=user)
        
        # Move task to In Progress (right)
        move_url = reverse('task_move', args=[task.pk, 'right'])
        response = self.client.get(move_url)
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertEqual(task.stage, 'in_progress')
        
        # Edit task
        edit_url = reverse('task_edit', args=[task.pk])
        edit_post_data = {
            'title': 'Updated Task Title',
            'description': 'Updated description',
            'stage': 'done'
        }
        response = self.client.post(edit_url, edit_post_data)
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated Task Title')
        self.assertEqual(task.stage, 'done')
        
        # Delete task
        delete_url = reverse('task_delete', args=[task.pk])
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())

    def test_task_isolation(self):
        # Create two users
        user1 = User.objects.create_user(username='u1', password='pwd')
        user2 = User.objects.create_user(username='u2', password='pwd')
        
        # Create a task for user1
        task = Task.objects.create(title='U1 Task', stage='todo', user=user1)
        
        # Login as user2 and try to edit user1's task
        self.client.force_login(user2)
        edit_url = reverse('task_edit', args=[task.pk])
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 404) # Should return 404 Not Found
        
        # Try to move user1's task
        move_url = reverse('task_move', args=[task.pk, 'right'])
        response = self.client.get(move_url)
        self.assertEqual(response.status_code, 404)
