from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Newspaper, Redactor, Topic


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    context = {
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
    }

    return render(request, "catalog/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "catalog/topic_list.html"
    context_object_name = "topic_list"


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")
    template_name = "catalog/topic_form.html"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")
    template_name = "catalog/topic_form.html"


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("catalog:topic-list")
    template_name = "catalog/topic_confirm_delete.html"


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("catalog:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("catalog:newspaper-list")
    template_name = "catalog/newspaper_form.html"


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("catalog:newspaper-list")
    template_name = "catalog/newspaper_confirm_delete.html"


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    queryset = Redactor.objects.prefetch_related("newspapers")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("catalog:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("catalog:redactor-list")
    template_name = "catalog/redactor_form.html"


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("catalog:redactor-list")
    template_name = "catalog/redactor_confirm_delete.html"

