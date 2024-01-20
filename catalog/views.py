from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from catalog.models import Newspaper, Redactor, Topic


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


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    queryset = Redactor.objects.prefetch_related("newspapers")
