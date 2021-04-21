from django import forms
from .models import Bookmark, Folder

class BookmarkForm(forms.ModelForm):
    
    class Meta:
        model = Bookmark
        fields = ('name', 'url', 'description', 'tags', 'folder')


class FolderForm(forms.ModelForm):

    class Meta:
        model = Folder
        fields = ('name',)