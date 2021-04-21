from django.urls import path
from . import views

app_name = 'markers'

urlpatterns = [
    path('bookmarks/', views.BookmarkListView.as_view(), name='bookmark-list'),
    path('bookmark/<int:pk>/', views.BookmarkDetailView.as_view(), name='bookmark-detail'),
    path('add_bookmark/', views.add_bookmark, name='add-bookmark'),
    path('edit_bookmark/<int:pk>/', views.edit_bookmark, name='edit-bookmark'),
    path('delete_bookmark/<int:pk>/', views.delete_bookmark, name='delete-bookmark'),
]