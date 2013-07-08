# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Snippet.body_markup_type'
        db.add_column(u'snippets_snippet', 'body_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30),
                      keep_default=False)

        # Adding field 'Snippet._body_rendered'
        db.add_column(u'snippets_snippet', '_body_rendered',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


        # Changing field 'Snippet.body'
        db.alter_column(u'snippets_snippet', 'body', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

        # Changing field 'SnippetImage.image'
        db.alter_column(u'snippets_snippetimage', 'image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

    def backwards(self, orm):
        # Deleting field 'Snippet.body_markup_type'
        db.delete_column(u'snippets_snippet', 'body_markup_type')

        # Deleting field 'Snippet._body_rendered'
        db.delete_column(u'snippets_snippet', '_body_rendered')


        # Changing field 'Snippet.body'
        db.alter_column(u'snippets_snippet', 'body', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SnippetImage.image'
        db.alter_column(u'snippets_snippetimage', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    models = {
        u'snippets.snippet': {
            'Meta': {'object_name': 'Snippet'},
            '_body_rendered': ('django.db.models.fields.TextField', [], {}),
            'body': ('markupfield.fields.MarkupField', [], {'default': "''", 'rendered_field': 'True'}),
            'body_markup_type': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '30'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'snippets.snippetimage': {
            'Meta': {'object_name': 'SnippetImage'},
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['snippets']