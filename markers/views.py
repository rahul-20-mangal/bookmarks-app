from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from markers.models import Bookmark
from markers.filters import BookmarkFilter
from markers.forms import BookmarkForm 
from django.db import transaction

class BookmarkListView(ListView):
    model = Bookmark

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BookmarkFilter(self.request.GET, queryset=self.get_queryset())
        return context

class BookmarkDetailView(DetailView):
    model = Bookmark

@transaction.atomic
def add_bookmark(request):
    bookmark_form = BookmarkForm(request.POST or None)

    if bookmark_form.is_valid():
        bookmark = bookmark_form.save()
        return redirect('markers:bookmark-list')

    context = {
        "bookmark_form": bookmark_form,
    }
    return render(request, 'markers/add_bookmark.html', context)