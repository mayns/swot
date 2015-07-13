from django.db import models
from django.contrib.postgres.fields import ArrayField


# class User(models.Model):
#     google_token = models.TextField()


class Diagram(models.Model):
    # user_id = models.ForeignKey(User)
    title = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    strengths = ArrayField(models.TextField(max_length=200))
    weaknesses = ArrayField(models.TextField(max_length=200))
    opportunities = ArrayField(models.TextField(max_length=200))
    threats = ArrayField(models.TextField(max_length=200))
