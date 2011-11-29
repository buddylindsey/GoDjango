# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Video'
        db.create_table('home_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, db_index=True)),
            ('thumbnail_image', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('preview_image', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('video_ogv', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('video_mp4', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('video_vp8', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('length', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('episode', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('home', ['Video'])


    def backwards(self, orm):
        
        # Deleting model 'Video'
        db.delete_table('home_video')


    models = {
        'home.video': {
            'Meta': {'object_name': 'Video'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'episode': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'preview_image': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'db_index': 'True'}),
            'thumbnail_image': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'video_mp4': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'video_ogv': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'video_vp8': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['home']
