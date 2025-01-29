from unittest import TestCase

from agency.forms import RedactorUsernameSearchForm, NewspaperForm
from agency.models import Topic


class FormTest(TestCase):
    def test_redactor_username_search_form_valid(self):
        form_data = {"username": "testuser"}
        form = RedactorUsernameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "testuser")

    def test_newspaper_form_valid(self):
        topic = Topic.objects.create(name="Test Topic")
        form_data = {
            "title": "Test Newspaper",
            "content": "Test newspaper content.",
            "topic": [topic.id],
            "redactor": [],
        }
        form = NewspaperForm(data=form_data)
        self.assertTrue(form.is_valid())
        newspaper = form.save()
        self.assertEqual(newspaper.title, "Test Newspaper")
        self.assertEqual(newspaper.content, "Test newspaper content.")
