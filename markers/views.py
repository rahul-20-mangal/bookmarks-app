from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkDetailView(DetailView):
    model = Bookmark

