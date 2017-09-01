# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    added = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    def get_post_url(self):
        return '/posts/%s/' % self.id

