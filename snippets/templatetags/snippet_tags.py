from markdown import markdown
import re

from django import template
from django.conf import settings
from django.template.loader import render_to_string

from snippets.models import Snippet, SnippetImage

register = template.Library()


@register.tag
def snippet(parser, token):
    chunks = token.split_contents()
    name = chunks[1].strip("'\"")
    keys = ('markup', 'content')
    params = {}
    for chunk in chunks[2:]:
        match = re.match(r"(\w+)=(.*)", chunk)
        if match:
            key = match.group(1)
            val = match.group(2)
            if key in keys:
                params[key] = val.strip("'\"")
    if 'content' in params.keys():
        nodelist = None
    else:
        nodelist = parser.parse(('endsnippet',))
        parser.delete_first_token()

    return SnippetNode(name, params, nodelist)

class SnippetNode(template.Node):

    def __init__(self, name, params, nodelist):
        self.nodelist = nodelist
        self.name = name
        self.params = params

    def render(self, context):
        slug = template.defaultfilters.slugify(self.name)

        try:
            snippet, created = Snippet.objects.get_or_create(title=slug)
        except Snippet.MultipleObjectsReturned:
            snippet = Snippet.objects.filter(title=slug).latest('pk')
            created = False

        if created:
            snippet.title = slug
            snippet.description = self.name
            snippet.body = self.params.get('content') or self.nodelist.render(context)
            snippet.body_markup_type = self.params.get('markup') or 'markdown'
            snippet.save()

        return render_to_string("snippets/snippet.html", {
            'snippet': snippet,
        }, context)


@register.inclusion_tag('snippets/snippet_image.html', takes_context=True)
def snippet_image(context, name, allow_delete=True):
    slug = template.defaultfilters.slugify(name)
    try:
        snippet, created = SnippetImage.objects.get_or_create(title=slug)
    except Snippet.MultipleObjectsReturned:
        snippet = Snippet.objects.filter(title=slug).latest('pk')
        created = False

    if created:
        snippet.title = slug
        snippet.save()

    context['snippet'] = snippet
    return context


@register.inclusion_tag('snippets/snippet.html', takes_context=True)
def snippet_simple(context, name, allow_delete=True):
    slug = template.defaultfilters.slugify(name)
    try:
        snippet, created = Snippet.objects.get_or_create(title=slug)
    except Snippet.MultipleObjectsReturned:
        snippet = Snippet.objects.filter(title=slug).latest('pk')
        created = False

    if created:
        snippet.title = slug
        snippet.description = name
        snippet.body = "[{0}]".format(name)
        snippet.save()

    context['snippet'] = snippet
    return context
