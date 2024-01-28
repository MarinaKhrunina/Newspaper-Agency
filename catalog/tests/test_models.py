from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import Topic, Newspaper


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="test")
        self.assertEqual(str(topic), topic.name)

    def test_redactor_str(self):
        redactor = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.username}: ({redactor.first_name} {redactor.last_name})"
        )

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="test")
        newspaper = Newspaper.objects.create(title="test", topic=topic, published_date="2024-10-22")
        self.assertEqual(
            str(newspaper),
            f"{newspaper.title} (topic: {newspaper.topic.name}, published date: {newspaper.published_date})"
        )

    def test_create_redactor_with_years_of_experience(self):
        username = "test"
        password = "test123"
        years_of_experience = "123"
        author = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(author.username, username)
        self.assertEqual(author.years_of_experience, years_of_experience)
        self.assertTrue(author.check_password(password))