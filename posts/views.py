# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages


def posts_home(request):
    return HttpResponse("<h1>Hello</h1>")


def posts_create(request):

    form = PostForm(request.POST or None)

    # print request.POST.get("content")
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()
        messages.success(request, "Post 101 Created successfully")
        return HttpResponseRedirect(instance.get_post_url())
    else:
        messages.error(request, "Message 102 could not be created")

    context = {
        "form": form
    }

    return render(request, "post_form.html", context)


def posts_list(request):

    queryset = Post.objects.all()
    context = {
        "list": queryset
    }
    return render(request, "list.html", context)


def posts_detail(request, pk=None):

    instance = get_object_or_404(Post, id=pk)
    context = {
        "instance": instance,
        "title": "Detail"
    }
    return render(request, "index.html", context)


def posts_update(request, pk=None):

    instance = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST or None, instance=instance)   # instance = instance displays that post we get
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Blog Updated")
        # messages.success(request, "Blog Updated", extra_tags='html_safe')

        return HttpResponseRedirect(instance.get_post_url())

    context = {
        "form": form
    }

    return render(request, "post_form.html", context)


def posts_delete(request, pk=None):
    instance = get_object_or_404(Post, id=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("/posts/list")















