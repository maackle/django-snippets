from markdown import markdown

from django import template
from django.conf import settings
from django.template.loader import render_to_string

from snippets.models import Snippet

register = template.Library()


@register.inclusion_tag('snippets/snippet.html', takes_context=True)
def snippet(context, name, allow_delete=True):
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


# @register.tag
# def snippet_complex(parser, token):
#     chunks = token.split_contents()
#     print chunks
#     name = chunks[1].strip("'")
#     return SnippetNode(name)

# class SnippetNode(template.Node):

#     def __init__(self, name):
#         slug = template.defaultfilters.slugify(name)
#         try:
#             snippet, created = Snippet.objects.get_or_create(title=slug)
#         except Snippet.MultipleObjectsReturned:
#             snippet = Snippet.objects.filter(title=slug).latest('pk')
#             created = False

#         if created:
#             snippet.title = slug
#             snippet.description = name
#             snippet.body = "[{0}]".format(name)
#             snippet.save()
#         self.snippet = snippet

#     def render(self, context):
#         return render_to_string("snippets/snippet.html", {
#             'snippet': self.snippet,
#         }, context)


# @register.simple_tag
# def snippet_old(name):

#     slug = template.defaultfilters.slugify(name)
#     try:
#         snippet, created = Snippet.objects.get_or_create(title=slug)
#     except Snippet.MultipleObjectsReturned:
#         snippet = Snippet.objects.filter(title=slug).latest('pk')
#         created = False

#     if created:
#         snippet.title = slug
#         snippet.description = name
#         snippet.body = "[{0}]".format(name)
#         snippet.save()

#     return render_to_string('snippets/snippet.html', {
#         'snippet': snippet,
#     })
