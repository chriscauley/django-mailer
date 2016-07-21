# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MessageLog.message_id'
        db.add_column('mailer_messagelog', 'message_id',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


        # Changing field 'DontSendEntry.to_address'
        db.alter_column('mailer_dontsendentry', 'to_address', self.gf('django.db.models.fields.EmailField')(max_length=254))

    def backwards(self, orm):
        # Deleting field 'MessageLog.message_id'
        db.delete_column('mailer_messagelog', 'message_id')


        # Changing field 'DontSendEntry.to_address'
        db.alter_column('mailer_dontsendentry', 'to_address', self.gf('django.db.models.fields.EmailField')(max_length=123))

    models = {
        'mailer.dontsendentry': {
            'Meta': {'object_name': 'DontSendEntry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_address': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {})
        },
        'mailer.message': {
            'Meta': {'object_name': 'Message'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_data': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "u'2'", 'max_length': '1'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'mailer.messagelog': {
            'Meta': {'object_name': 'MessageLog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_message': ('django.db.models.fields.TextField', [], {}),
            'message_data': ('django.db.models.fields.TextField', [], {}),
            'message_id': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_index': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'when_attempted': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['mailer']