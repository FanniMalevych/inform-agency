from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 5


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 10


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("agency:newspaper-list")


class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    fields = "__all__"


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-list")
