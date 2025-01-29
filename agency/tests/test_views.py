from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Topic

TOPIC_URL = reverse("agency:topic-list")


class PublicTopicTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TOPIC_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="test"
        )
        self.client.force_login(self.user)

    def test_retrieve_topic(self):
        Topic.objects.create(name="Science")
        Topic.objects.create(name="Technology")
        resp = self.client.get(TOPIC_URL)
        self.assertEqual(resp.status_code, 200)

        topics = Topic.objects.all()

        self.assertEqual(list(resp.context["topic_list"]), list(topics))

        self.assertTemplateUsed(resp, "agency/topic_list")
