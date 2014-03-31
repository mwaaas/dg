# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trainer'
        db.create_table(u'trainings_trainer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'trainings', ['Trainer'])

        # Adding model 'Trainee'
        db.create_table(u'trainings_trainee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('village', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geographies.Village'])),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programs.Partner'])),
        ))
        db.send_create_signal(u'trainings', ['Trainee'])

        # Adding unique constraint on 'Trainee', fields ['name', 'village']
        db.create_unique(u'trainings_trainee', ['name', 'village_id'])

        # Adding model 'Donor'
        db.create_table(u'trainings_donor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'trainings', ['Donor'])

        # Adding model 'Module'
        db.create_table(u'trainings_module', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'trainings', ['Module'])

        # Adding model 'Training'
        db.create_table(u'trainings_training', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geographies.Block'])),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trainings.Donor'])),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programs.Partner'])),
            ('module', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trainings.Module'])),
            ('days', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'trainings', ['Training'])

        # Adding M2M table for field trainers on 'Training'
        db.create_table(u'trainings_training_trainers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('training', models.ForeignKey(orm[u'trainings.training'], null=False)),
            ('trainer', models.ForeignKey(orm[u'trainings.trainer'], null=False))
        ))
        db.create_unique(u'trainings_training_trainers', ['training_id', 'trainer_id'])

        # Adding model 'TraineeTrained'
        db.create_table(u'trainings_traineetrained', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('training', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trainings.Training'])),
            ('trainee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trainings.Trainee'])),
            ('environmen_creation_grade', self.gf('django.db.models.fields.FloatField')()),
            ('facilitation_grade', self.gf('django.db.models.fields.FloatField')()),
            ('pico_handling_documentation_grade', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'trainings', ['TraineeTrained'])


    def backwards(self, orm):
        # Removing unique constraint on 'Trainee', fields ['name', 'village']
        db.delete_unique(u'trainings_trainee', ['name', 'village_id'])

        # Deleting model 'Trainer'
        db.delete_table(u'trainings_trainer')

        # Deleting model 'Trainee'
        db.delete_table(u'trainings_trainee')

        # Deleting model 'Donor'
        db.delete_table(u'trainings_donor')

        # Deleting model 'Module'
        db.delete_table(u'trainings_module')

        # Deleting model 'Training'
        db.delete_table(u'trainings_training')

        # Removing M2M table for field trainers on 'Training'
        db.delete_table('trainings_training_trainers')

        # Deleting model 'TraineeTrained'
        db.delete_table(u'trainings_traineetrained')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'geographies.block': {
            'Meta': {'object_name': 'Block'},
            'block_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_block_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_block_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'geographies.country': {
            'Meta': {'object_name': 'Country'},
            'country_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_country_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_country_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'geographies.district': {
            'Meta': {'object_name': 'District'},
            'district_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '31', 'decimal_places': '28', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '32', 'decimal_places': '28', 'blank': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.State']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_district_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_district_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'geographies.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'region_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_region_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_region_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'geographies.state': {
            'Meta': {'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Region']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_state_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_state_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'geographies.village': {
            'Meta': {'unique_together': "(('village_name', 'block'),)", 'object_name': 'Village'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Block']"}),
            'control': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'no_of_households': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'road_connectivity': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_village_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_village_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'programs.partner': {
            'Meta': {'object_name': 'Partner'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'date_of_association': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'partner_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'programs_partner_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'programs_partner_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'trainings.donor': {
            'Meta': {'object_name': 'Donor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'trainings.module': {
            'Meta': {'object_name': 'Module'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'trainings.trainee': {
            'Meta': {'unique_together': "(('name', 'village'),)", 'object_name': 'Trainee'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']"})
        },
        u'trainings.traineetrained': {
            'Meta': {'object_name': 'TraineeTrained'},
            'environmen_creation_grade': ('django.db.models.fields.FloatField', [], {}),
            'facilitation_grade': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pico_handling_documentation_grade': ('django.db.models.fields.FloatField', [], {}),
            'trainee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trainings.Trainee']"}),
            'training': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trainings.Training']"})
        },
        u'trainings.trainer': {
            'Meta': {'object_name': 'Trainer'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'trainings.training': {
            'Meta': {'object_name': 'Training'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Block']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'days': ('django.db.models.fields.FloatField', [], {}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trainings.Donor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trainings.Module']"}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'trainees': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['trainings.Trainee']", 'through': u"orm['trainings.TraineeTrained']", 'symmetrical': 'False'}),
            'trainers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['trainings.Trainer']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['trainings']