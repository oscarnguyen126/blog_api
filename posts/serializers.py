from django.http import HttpResponse
from rest_framework import serializers
from .models import Post


class PostSerializer:
    def __init__(self, post):
        self.post = post

    def parse(self):
        return {
            'author': self.post.author.username,
            'title': self.post.title,
            'body': self.post.body,
            'created_at': self.post.created_at,
            }
