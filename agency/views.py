from django.shortcuts import render

from agency.models import Redactor, Topic, Newspaper


def index(request):
    """View function for the home page of the site."""

    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    num_newspapers = Newspaper.objects.count()


    context = {
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_newspapers": num_newspapers,
    }

    return render(request, "agency/index.html", context=context)
