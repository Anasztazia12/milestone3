from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Cafe


class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser', password='testpass123'
        )
        self.cafe = Cafe.objects.create(
            name='Test Cafe',
            address='1 Test St',
            city='Testville',
            submitted_by=self.user,
        )

    def test_homepage_loads(self):
        """Homepage should load successfully for anyone"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'WorkCafe', response.content)

    def test_signup_creates_user(self):
        """Signing up should create a new user and log them in"""
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'avatar_seed': 'Storm',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertIn(b'Your account has been created', response.content)

    def test_login_wrong_password_shows_error(self):
        """Logging in with the wrong password should show an error"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Wrong username or password', response.content)

    def test_add_cafe_requires_login(self):
        """Logged out users should be sent to the login page"""
        response = self.client.get(reverse('add_cafe'))
        self.assertRedirects(response, reverse('login'))

    def test_add_cafe_creates_cafe(self):
        """A logged in user can add a new cafe"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('add_cafe'), {
            'name': 'New Cafe',
            'address': '2 Test St',
            'city': 'Testville',
            'wifi': 'yes',
            'quiet': 'yes',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Cafe.objects.filter(name='New Cafe').exists())
        self.assertIn(b'has been added', response.content)

    def test_only_owner_can_edit_cafe(self):
        """A user should not be able to edit someone else's cafe"""
        self.client.login(username='otheruser', password='testpass123')
        response = self.client.get(reverse('edit_cafe', args=[self.cafe.id]))
        self.assertEqual(response.status_code, 404)

    def test_favourite_toggle_adds_and_removes(self):
        """Favouriting a cafe should add it, favouriting again should remove it"""
        self.client.login(username='testuser', password='testpass123')
        self.client.post(reverse('toggle_favourite', args=[self.cafe.id]))
        self.assertIn(self.user, self.cafe.favourited_by.all())

        self.client.post(reverse('toggle_favourite', args=[self.cafe.id]))
        self.assertNotIn(self.user, self.cafe.favourited_by.all())

    def test_delete_cafe_removes_it(self):
        """Deleting a cafe should remove it from the database"""
        self.client.login(username='testuser', password='testpass123')
        self.client.post(reverse('delete_cafe', args=[self.cafe.id]))
        self.assertFalse(Cafe.objects.filter(id=self.cafe.id).exists())
