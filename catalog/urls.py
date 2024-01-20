from django.urls import path

from catalog.views import (
    index,
    TopicListView,
    NewspaperListView,
    RedactorListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topics-list"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
]


app_name = "catalog"
