# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Snippet'
        db.create_table(u'snippets_snippet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'snippets', ['Snippet'])

        # Adding model 'SnippetImage'
        db.create_table(u'snippets_snippetimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'snippets', ['SnippetImage'])


    def backwards(self, orm):
        # Deleting model 'Snippet'
        db.delete_table(u'snippets_snippet')

        # Deleting model 'SnippetImage'
        db.delete_table(u'snippets_snippetimage')


    models = {
        u'snippets.snippet': {
            'Meta': {'object_name': 'Snippet'},
            'body': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'snippets.snippetimage': {
            'Meta': {'object_name': 'SnippetImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['snippets']