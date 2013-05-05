# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Shout.pubdate'
        db.delete_column(u'bestsell_shout', 'pubdate')

        # Adding field 'Shout.publisher'
        db.add_column(u'bestsell_shout', 'publisher',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Shout.pubdate'
        db.add_column(u'bestsell_shout', 'pubdate',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15, blank=True),
                      keep_default=False)

        # Deleting field 'Shout.publisher'
        db.delete_column(u'bestsell_shout', 'publisher')


    models = {
        u'bestsell.shout': {
            'Meta': {'object_name': 'Shout'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'bldate': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'booklist': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        }
    }

    complete_apps = ['bestsell']