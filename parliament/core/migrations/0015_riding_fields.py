# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Riding.name_fr'
        db.add_column(u'core_riding', 'name_fr', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True), keep_default=False)

        # Adding field 'Riding.current'
        db.add_column(u'core_riding', 'current', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Changing field 'Riding.name'
        db.alter_column(u'core_riding', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))


    def backwards(self, orm):
        
        # Deleting field 'Riding.name_fr'
        db.delete_column(u'core_riding', 'name_fr')

        # Deleting field 'Riding.current'
        db.delete_column(u'core_riding', 'current')

        # Changing field 'Riding.name'
        db.alter_column(u'core_riding', 'name', self.gf('django.db.models.fields.CharField')(max_length=60))


    models = {
        u'core.electedmember': {
            'Meta': {'object_name': 'ElectedMember'},
            'end_date': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Party']"}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Politician']"}),
            'riding': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Riding']"}),
            'sessions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Session']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {'db_index': 'True'})
        },
        u'core.internalxref': {
            'Meta': {'object_name': 'InternalXref'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'int_value': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'schema': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'target_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'text_value': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'})
        },
        u'core.party': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Party'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'core.politician': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Politician'},
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_family': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name_given': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30', 'blank': 'True'})
        },
        u'core.politicianinfo': {
            'Meta': {'object_name': 'PoliticianInfo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Politician']"}),
            'schema': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'core.riding': {
            'Meta': {'ordering': "('province', 'name')", 'object_name': 'Riding'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'edid': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60', 'db_index': 'True'})
        },
        u'core.session': {
            'Meta': {'ordering': "('-start',)", 'object_name': 'Session'},
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parliamentnum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sessnum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        u'core.sitenews': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'SiteNews'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']
