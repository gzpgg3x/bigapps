# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Shout.title'
        db.add_column(u'bestsell_shout', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=80, blank=True),
                      keep_default=False)

        # Adding field 'Shout.isbn'
        db.add_column(u'bestsell_shout', 'isbn',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15, blank=True),
                      keep_default=False)


        # Changing field 'Shout.author'
        db.alter_column(u'bestsell_shout', 'author', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Deleting field 'Shout.title'
        db.delete_column(u'bestsell_shout', 'title')

        # Deleting field 'Shout.isbn'
        db.delete_column(u'bestsell_shout', 'isbn')


        # Changing field 'Shout.author'
        db.alter_column(u'bestsell_shout', 'author', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'bestsell.shout': {
            'Meta': {'object_name': 'Shout'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        }
    }

    complete_apps = ['bestsell']