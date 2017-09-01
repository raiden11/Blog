# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ["title", "added", "updated"]
    list_filter = ["updated", "added", "title"]
    list_editable = ["title"]
    list_display_links = ["updated"]
    search_fields = ["title"]
    class Meta:
        model = Post


admin.site.register(Post,PostAdmin)
