from django.db import models

from sorl.thumbnail import ImageField
from markupfield.fields import MarkupField

class Snippet(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=200, default="")
    body = MarkupField(default="", default_markup_type='markdown')

    def __unicode__(self):
        return "Snippet '%s'" % (self.title,)


class SnippetImage(models.Model):
    title = models.CharField(max_length=128, unique=True)
    image = ImageField(upload_to='snippets', null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=256, blank=True, null=True)

    @property
    def width_css(self):
        if self.width is not None:
            return str(self.width) + 'px'
        else:
            return 'inherit'

    @property
    def height_css(self):
        if self.height is not None:
            return str(self.height) + 'px'
        else:
            return 'inherit'

    def __unicode__(self):
        return "Snippet Image '%s'" % (self.title,)

