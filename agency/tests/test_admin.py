from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Redactor, Newspaper, Topic

User = get_user_model()


class AdminTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin", password="password"
        )
        self.client.force_login(self.superuser)

        self.topic = Topic.objects.create(name="Test Topic")
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper", published_date="2023-01-01", topic=self.topic
        )
        self.redactor = Redactor.objects.create(
            username="test_redactor",
            first_name="Test",
            last_name="Test",
            years_of_experience=5,
            password="password",
        )

    def test_redactor_admin_list_display(self):
        response = self.client.get(reverse("admin:agency_redactor_changelist"))
        self.assertContains(response, "years_of_experience")

    def test_redactor_admin_fieldsets(self):
        response = self.client.get(reverse("admin:agency_redactor_add"))
        self.assertContains(response, "Additional info")
        self.assertContains(response, "years_of_experience")

    def test_newspaper_admin_list_display(self):
        response = self.client.get(reverse("admin:agency_newspaper_changelist"))
        self.assertContains(response, "Test Newspaper")
        self.assertContains(response, "Test Topic")

    def test_newspaper_admin_search(self):
        response = self.client.get(
            reverse("admin:agency_newspaper_changelist"), {"q": "Test Newspaper"}
        )
        self.assertContains(response, "Test Newspaper")

    def test_newspaper_admin_list_filter(self):
        response = self.client.get(reverse("admin:agency_newspaper_changelist"))
        self.assertContains(response, "topic")
