# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Screening'
        db.create_table(u'activities_screening', (
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'activities_screening_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'activities_screening_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('old_coco_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('target_person_attendance', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('target_audience_interest', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('target_adoptions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('village', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geographies.Village'])),
            ('animator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Animator'])),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programs.Partner'])),
        ))
        db.send_create_signal(u'activities', ['Screening'])

        # Adding unique constraint on 'Screening', fields ['date', 'start_time', 'end_time', 'animator', 'village']
        db.create_unique(u'activities_screening', ['date', 'start_time', 'end_time', 'animator_id', 'village_id'])

        # Adding M2M table for field farmer_groups_targeted on 'Screening'
        db.create_table(u'activities_screening_farmer_groups_targeted', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('screening', models.ForeignKey(orm[u'activities.screening'], null=False)),
            ('persongroup', models.ForeignKey(orm[u'people.persongroup'], null=False))
        ))
        db.create_unique(u'activities_screening_farmer_groups_targeted', ['screening_id', 'persongroup_id'])

        # Adding M2M table for field videoes_screened on 'Screening'
        db.create_table(u'activities_screening_videoes_screened', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('screening', models.ForeignKey(orm[u'activities.screening'], null=False)),
            ('video', models.ForeignKey(orm[u'videos.video'], null=False))
        ))
        db.create_unique(u'activities_screening_videoes_screened', ['screening_id', 'video_id'])

        # Adding model 'PersonMeetingAttendance'
        db.create_table(u'activities_personmeetingattendance', (
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'activities_personmeetingattendance_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'activities_personmeetingattendance_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('old_coco_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('screening', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activities.Screening'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('interested', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('expressed_question', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('expressed_adoption_video', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='expressed_adoption_video', null=True, to=orm['videos.Video'])),
        ))
        db.send_create_signal(u'activities', ['PersonMeetingAttendance'])

        # Adding model 'PersonAdoptPractice'
        db.create_table(u'activities_personadoptpractice', (
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'activities_personadoptpractice_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'activities_personadoptpractice_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('old_coco_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['videos.Video'])),
            ('prior_adoption_flag', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('date_of_adoption', self.gf('django.db.models.fields.DateField')()),
            ('quality', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quantity_unit', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('time_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programs.Partner'])),
        ))
        db.send_create_signal(u'activities', ['PersonAdoptPractice'])

        # Adding unique constraint on 'PersonAdoptPractice', fields ['person', 'video', 'date_of_adoption']
        db.create_unique(u'activities_personadoptpractice', ['person_id', 'video_id', 'date_of_adoption'])


    def backwards(self, orm):
        # Removing unique constraint on 'PersonAdoptPractice', fields ['person', 'video', 'date_of_adoption']
        db.delete_unique(u'activities_personadoptpractice', ['person_id', 'video_id', 'date_of_adoption'])

        # Removing unique constraint on 'Screening', fields ['date', 'start_time', 'end_time', 'animator', 'village']
        db.delete_unique(u'activities_screening', ['date', 'start_time', 'end_time', 'animator_id', 'village_id'])

        # Deleting model 'Screening'
        db.delete_table(u'activities_screening')

        # Removing M2M table for field farmer_groups_targeted on 'Screening'
        db.delete_table('activities_screening_farmer_groups_targeted')

        # Removing M2M table for field videoes_screened on 'Screening'
        db.delete_table('activities_screening_videoes_screened')

        # Deleting model 'PersonMeetingAttendance'
        db.delete_table(u'activities_personmeetingattendance')

        # Deleting model 'PersonAdoptPractice'
        db.delete_table(u'activities_personadoptpractice')


    models = {
        u'activities.personadoptpractice': {
            'Meta': {'unique_together': "(('person', 'video', 'date_of_adoption'),)", 'object_name': 'PersonAdoptPractice'},
            'date_of_adoption': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'prior_adoption_flag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantity_unit': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'time_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'activities_personadoptpractice_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'activities_personadoptpractice_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.Video']"})
        },
        u'activities.personmeetingattendance': {
            'Meta': {'object_name': 'PersonMeetingAttendance'},
            'expressed_adoption_video': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'expressed_adoption_video'", 'null': 'True', 'to': u"orm['videos.Video']"}),
            'expressed_question': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interested': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'screening': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['activities.Screening']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'activities_personmeetingattendance_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'activities_personmeetingattendance_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'activities.screening': {
            'Meta': {'unique_together': "(('date', 'start_time', 'end_time', 'animator', 'village'),)", 'object_name': 'Screening'},
            'animator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Animator']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'farmer_groups_targeted': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['people.PersonGroup']", 'symmetrical': 'False'}),
            'farmers_attendance': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['people.Person']", 'null': "'False'", 'through': u"orm['activities.PersonMeetingAttendance']", 'blank': "'False'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'target_adoptions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'target_audience_interest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'target_person_attendance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'activities_screening_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'activities_screening_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'videoes_screened': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['videos.Video']", 'symmetrical': 'False'}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']"})
        },
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
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
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
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
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
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
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
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
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
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
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
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'road_connectivity': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_village_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_village_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'people.animator': {
            'Meta': {'unique_together': "(('name', 'gender', 'partner', 'district'),)", 'object_name': 'Animator'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'assigned_villages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'assigned_villages'", 'to': u"orm['geographies.Village']", 'through': u"orm['people.AnimatorAssignedVillage']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'camera_operator_flag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'csp_flag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.District']", 'null': 'True', 'blank': 'True'}),
            'facilitator_flag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'total_adoptions': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_animator_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_animator_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']", 'null': 'True', 'blank': 'True'})
        },
        u'people.animatorassignedvillage': {
            'Meta': {'object_name': 'AnimatorAssignedVillage'},
            'animator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Animator']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_animatorassignedvillage_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_animatorassignedvillage_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']"})
        },
        u'people.person': {
            'Meta': {'unique_together': "(('person_name', 'father_name', 'village'),)", 'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'date_of_joining': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.PersonGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_exists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'land_holdings': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_person_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_person_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']"})
        },
        u'people.persongroup': {
            'Meta': {'unique_together': "(('group_name', 'village'),)", 'object_name': 'PersonGroup'},
            'days': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'time_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'timings': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_persongroup_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_persongroup_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']"})
        },
        u'programs.partner': {
            'Meta': {'object_name': 'Partner'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'date_of_association': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'}),
            'partner_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'programs_partner_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'programs_partner_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_language_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_language_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practice': {
            'Meta': {'unique_together': "(('practice_sector', 'practice_subsector', 'practice_topic', 'practice_subtopic', 'practice_subject'),)", 'object_name': 'Practice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'practice_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'practice_sector': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['videos.PracticeSector']"}),
            'practice_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.PracticeSubject']", 'null': 'True', 'blank': 'True'}),
            'practice_subsector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.PracticeSubSector']", 'null': 'True', 'blank': 'True'}),
            'practice_subtopic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.PracticeSubtopic']", 'null': 'True', 'blank': 'True'}),
            'practice_topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.PracticeTopic']", 'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practice_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practice_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practicesector': {
            'Meta': {'object_name': 'PracticeSector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesector_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesector_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practicesubject': {
            'Meta': {'object_name': 'PracticeSubject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubject_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubject_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practicesubsector': {
            'Meta': {'object_name': 'PracticeSubSector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubsector_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubsector_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practicesubtopic': {
            'Meta': {'object_name': 'PracticeSubtopic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubtopic_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubtopic_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practicetopic': {
            'Meta': {'object_name': 'PracticeTopic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicetopic_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicetopic_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.video': {
            'Meta': {'unique_together': "(('title', 'video_production_start_date', 'video_production_end_date', 'village'),)", 'object_name': 'Video'},
            'actors': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'approval_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'audio_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cameraoperator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cameraoperator'", 'to': u"orm['people.Animator']"}),
            'duration': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'edit_finish_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'edit_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'editing_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'facilitator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facilitator'", 'to': u"orm['people.Animator']"}),
            'farmers_shown': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['people.Person']", 'symmetrical': 'False'}),
            'final_edited_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.Language']"}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'movie_maker_project_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'picture_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'raw_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'related_practice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.Practice']", 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'storybase': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'storyboard_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'supplementary_video_produced': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.Video']", 'null': 'True', 'blank': 'True'}),
            'thematic_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_video_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_video_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'video_production_end_date': ('django.db.models.fields.DateField', [], {}),
            'video_production_start_date': ('django.db.models.fields.DateField', [], {}),
            'video_suitable_for': ('django.db.models.fields.IntegerField', [], {}),
            'video_type': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'viewers': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']"}),
            'youtubeid': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['activities']