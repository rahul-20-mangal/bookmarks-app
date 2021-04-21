from django.urls import path
from . import views

app_name = 'markers'

urlpatterns = [
    path('bookmarks/', views.BookmarkListView.as_view(), name='bookmark-list'),
    path('bookmark/<int:pk>/', views.BookmarkDetailView.as_view(), name='bookmark-detail'),
    path('add_bookmark/', views.add_bookmark, name='add-bookmark'),
]