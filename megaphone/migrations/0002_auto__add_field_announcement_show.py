# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Announcement.show'
        db.add_column('megaphone_announcement', 'show',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['broadcast.Show'], null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Announcement.show'
        db.delete_column('megaphone_announcement', 'show_id')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'broadcast.market': {
            'Meta': {'ordering': "['name']", 'object_name': 'Market'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'broadcast.radioformat': {
            'Meta': {'ordering': "['name']", 'object_name': 'RadioFormat'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'broadcast.show': {
            'Meta': {'ordering': "['title']", 'object_name': 'Show'},
            'default_announcement': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1500'}),
            'hosts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life_stream': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['broadcast.Station']"}),
            'syndicated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_friendly_time': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        'broadcast.station': {
            'Meta': {'unique_together': "(['call_letters', 'band'],)", 'object_name': 'Station'},
            'band': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'band_secondary': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'brand_name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'broadcast_power_watts': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'broadcast_power_watts_secondary': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'call_letters': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'frequency_secondary': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'has_stream': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'location_secondary': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'market': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['broadcast.Market']"}),
            'positioning_statement': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'radio_format': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['broadcast.RadioFormat']"}),
            'secret_nowplaying_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stations'", 'to': "orm['sites.Site']"}),
            'studio_line_main': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'studio_line_secondary': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'megaphone.announcement': {
            'Meta': {'object_name': 'Announcement'},
            'celery_task_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_text': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['broadcast.Show']", 'null': 'True', 'blank': 'True'}),
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