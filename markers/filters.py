import django_filters 
from .models import Bookmark

class BookmarkFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label="Name")

    class Meta:
        model = Bookmark
        fields = ['name', 'url', 'folder']