from django.contrib.auth.decorators import login_required
from django.test import TestCase, Client
from users.models import User
from django.contrib.auth import get_user_model


class TestResponse(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="admin", password="admin")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    # @login_required(login_url='/admin/login')
    def test_first_step_url(self):
        response = self.authorized_client.get('/api/first-step/')
        self.assertEquals(response.status_code, 200)
