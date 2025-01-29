from django.test import TestCase

from agency.models import Topic, Redactor, Newspaper


class ModelTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Technology")
        self.redactor = Redactor.objects.create(
            username="test_redactor",
            password="password",
            first_name="Test",
            last_name="Test",
            years_of_experience=5,
        )
        self.newspaper = Newspaper.objects.create(
            title="Latest Tech News",
            content="Content of the latest tech news.",
        )
        self.newspaper.topic.add(self.topic)
        self.newspaper.redactor.add(self.redactor)

    def test_topic_str(self):
        self.assertEqual(str(self.topic), "Technology")

    def test_topic_ordering(self):
        topic1 = Topic.objects.create(name="B")
        topic2 = Topic.objects.create(name="A")
        topics = Topic.objects.all()
        self.assertEqual(list(topics), [topic2, topic1])

    def test_redactor_str(self):
        self.assertEqual(str(self.redactor), "test_redactor (Test Test)")

    def test_newspaper_str(self):
        self.assertEqual(str(self.newspaper), "Latest Tech News")

    def test_relationships(self):
        self.assertIn(self.topic, self.newspaper.topic.all())
        self.assertIn(self.redactor, self.newspaper.redactor.all())
