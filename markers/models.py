from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Bookmark(models.Model):
    name = models.CharField(max_length=512)
    url = models.URLField(null=True, blank=True)
    description = models.TextField()
    tags = TaggableManager()
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE)

    def __str__(self):
        return '{} in folder {}'.format(self.name, self.folder)

class Folder(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name