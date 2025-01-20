from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from agency.forms import TopicSearchForm, NewspaperTitleSearchForm, RedactorUsernameSearchForm, NewspaperForm
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        context["search_form"] = TopicSearchForm(
            initial={"name": self.request.GET.get("name", "")}
        )
        return context

    def get_queryset(self):
        form = TopicSearchForm(self.request.GET)
        if form.is_valid():
            return Topic.objects.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return Topic.objects.all()


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        context["search_form"] = NewspaperTitleSearchForm(
            initial={"title": self.request.GET.get("title", "")}
        )
        return context

    def get_queryset(self):
        form = NewspaperTitleSearchForm(self.request.GET)
        if form.is_valid():
            return Newspaper.objects.filter(
                title__icontains=form.cleaned_data["title"]
            )
        return Newspaper.objects.all()


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-list")


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        context["search_form"] = RedactorUsernameSearchForm(
            initial={"username": self.request.GET.get("username", "")}
        )
        return context

    def get_queryset(self):
        form = RedactorUsernameSearchForm(self.request.GET)
        if form.is_valid():
            return Redactor.objects.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return Redactor.objects.all()


class RedactorDetailView(generic.DetailView):
    model = Redactor


class RedactorCreateView(generic.CreateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("agency:redactor-list")


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    fields = "__all__"


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")
