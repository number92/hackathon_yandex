from django.test import TestCase, Client
from users.models import User


class TestResponse(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="vasia")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    # @login_required(login_url='/admin/login')
    def test_first_step_url(self):
        response = self.authorized_client.get("/api/first-step/")
        self.assertEquals(response.status_code, 200)
