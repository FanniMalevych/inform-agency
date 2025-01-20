from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from agency.models import Topic, Newspaper, Redactor


class RedactorUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        ),
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        ),
    )


class NewspaperTitleSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by title"}
        ),
    )


class NewspaperForm(forms.ModelForm):
    redactor = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    topic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class RedactorForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = (
            "username",
            "years_of_experience",
            "first_name",
            "last_name",
        )