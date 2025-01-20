from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from agency.forms import TopicSearchForm, NewspaperTitleSearchForm, RedactorUsernameSearchForm, NewspaperForm, \
    RedactorCreationForm, RedactorForm
from agency.models import Redactor, Topic, Newspaper


@login_required
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


class TopicListView(LoginRequiredMixin, generic.ListView):
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


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
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


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
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


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("agency:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorForm
    success_url = reverse_lazy("agency:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")
