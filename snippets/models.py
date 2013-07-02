from django.db import models

class Snippet(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=200, default="")
    body = models.TextField(default="")

    def __unicode__(self):
        return "Snippet '%s'" % (self.title,)


class SnippetImage(models.Model):
    title = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='snippets', null=True)
    link = models.CharField(max_length=256, blank=True, null=True)

    def __unicode__(self):
        return "SnippetImage '%s'" % (self.title,)

