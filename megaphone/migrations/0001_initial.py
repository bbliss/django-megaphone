# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Announcement'
        db.create_table('megaphone_announcement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('main_text', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('celery_task_id', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('megaphone', ['Announcement'])

        # Adding M2M table for field sites on 'Announcement'
        db.create_table('megaphone_announcement_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('announcement', models.ForeignKey(orm['megaphone.announcement'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('megaphone_announcement_sites', ['announcement_id', 'site_id'])

    def backwards(self, orm):
        # Deleting model 'Announcement'
        db.delete_table('megaphone_announcement')

        # Removing M2M table for field sites on 'Announcement'
        db.delete_table('megaphone_announcement_sites')

    models = {
        'megaphone.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'celery_task_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_text': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['megaphone']