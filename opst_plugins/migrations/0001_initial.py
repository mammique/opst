# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TagCloudPluginModel'
        db.create_table('cmsplugin_tagcloudpluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('result_page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='opst_plugin_tagcloud', to=orm['cms.Page'])),
            ('items_min', self.gf('django.db.models.fields.PositiveIntegerField')(default=3)),
        ))
        db.send_create_signal('opst_plugins', ['TagCloudPluginModel'])

        # Adding model 'SearchBoxPluginModel'
        db.create_table('cmsplugin_searchboxpluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('result_page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='opst_plugin_searchbox', to=orm['cms.Page'])),
        ))
        db.send_create_signal('opst_plugins', ['SearchBoxPluginModel'])

        # Adding model 'NewsFeedEntry'
        db.create_table('opst_plugins_newsfeedentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('publication_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('opst_plugins', ['NewsFeedEntry'])

        # Adding model 'NewsFeedPluginModel'
        db.create_table('cmsplugin_newsfeedpluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('list_max', self.gf('django.db.models.fields.PositiveIntegerField')(default=8)),
        ))
        db.send_create_signal('opst_plugins', ['NewsFeedPluginModel'])

        # Adding M2M table for field news on 'NewsFeedPluginModel'
        db.create_table('opst_plugins_newsfeedpluginmodel_news', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsfeedpluginmodel', models.ForeignKey(orm['opst_plugins.newsfeedpluginmodel'], null=False)),
            ('newsfeedentry', models.ForeignKey(orm['opst_plugins.newsfeedentry'], null=False))
        ))
        db.create_unique('opst_plugins_newsfeedpluginmodel_news', ['newsfeedpluginmodel_id', 'newsfeedentry_id'])

        # Adding model 'NewsFeedExtPluginModel'
        db.create_table('cmsplugin_newsfeedextpluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('list_max', self.gf('django.db.models.fields.PositiveIntegerField')(default=8)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=1024)),
        ))
        db.send_create_signal('opst_plugins', ['NewsFeedExtPluginModel'])

        # Adding model 'NewsFeedPagePluginModel'
        db.create_table('cmsplugin_newsfeedpagepluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('list_max', self.gf('django.db.models.fields.PositiveIntegerField')(default=8)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=1024)),
            ('update_last', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('parent_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='parent_of_newsfeed', null=True, to=orm['cms.Page'])),
        ))
        db.send_create_signal('opst_plugins', ['NewsFeedPagePluginModel'])

        # Adding M2M table for field pages on 'NewsFeedPagePluginModel'
        db.create_table('opst_plugins_newsfeedpagepluginmodel_pages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsfeedpagepluginmodel', models.ForeignKey(orm['opst_plugins.newsfeedpagepluginmodel'], null=False)),
            ('page', models.ForeignKey(orm['cms.page'], null=False))
        ))
        db.create_unique('opst_plugins_newsfeedpagepluginmodel_pages', ['newsfeedpagepluginmodel_id', 'page_id'])

        # Adding model 'Auteur'
        db.create_table(u'auteur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=90)),
        ))
        db.send_create_signal('opst_plugins', ['Auteur'])

        # Adding model 'Categorie'
        db.create_table(u'categorie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150)),
        ))
        db.send_create_signal('opst_plugins', ['Categorie'])

        # Adding model 'Revue'
        db.create_table(u'revue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('nb_num_revues', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('opst_plugins', ['Revue'])

        # Adding model 'Tag'
        db.create_table(u'tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150)),
        ))
        db.send_create_signal('opst_plugins', ['Tag'])

        # Adding model 'SousCategorie'
        db.create_table(u'sous_categorie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150, blank=True)),
        ))
        db.send_create_signal('opst_plugins', ['SousCategorie'])

        # Adding model 'Ressource'
        db.create_table(u'ressource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=900)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=900, blank=True)),
            ('texte', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lien_texte', self.gf('django.db.models.fields.CharField')(max_length=1800, blank=True)),
            ('annee', self.gf('django.db.models.fields.IntegerField')()),
            ('mois', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('lieu', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('page_deb', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('page_fin', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date_debut', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_fin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('editeur', self.gf('django.db.models.fields.CharField')(max_length=450, blank=True)),
            ('formation', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('universite', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('discipline', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('type_production', self.gf('django.db.models.fields.CharField')(max_length=900, blank=True)),
            ('type_rapport', self.gf('django.db.models.fields.CharField')(max_length=900, blank=True)),
            ('id_revue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opst_plugins.Revue'], null=True, db_column='id_revue', blank=True)),
        ))
        db.send_create_signal('opst_plugins', ['Ressource'])

        # Adding M2M table for field tags on 'Ressource'
        db.create_table(u'ressource_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ressource', models.ForeignKey(orm['opst_plugins.ressource'], null=False)),
            ('tag', models.ForeignKey(orm['opst_plugins.tag'], null=False))
        ))
        db.create_unique(u'ressource_tags', ['ressource_id', 'tag_id'])

        # Adding M2M table for field auteurs on 'Ressource'
        db.create_table(u'ressource_auteurs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ressource', models.ForeignKey(orm['opst_plugins.ressource'], null=False)),
            ('auteur', models.ForeignKey(orm['opst_plugins.auteur'], null=False))
        ))
        db.create_unique(u'ressource_auteurs', ['ressource_id', 'auteur_id'])

        # Adding model 'RessourceCatSsCat'
        db.create_table(u'ressource_cat_ss_cat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_ressource', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ressourcecatsscat', db_column='id_ressource', to=orm['opst_plugins.Ressource'])),
            ('id_categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opst_plugins.Categorie'], db_column='id_categorie')),
            ('id_sous_cat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opst_plugins.SousCategorie'], db_column='id_sous_cat')),
        ))
        db.send_create_signal('opst_plugins', ['RessourceCatSsCat'])

        # Adding model 'RessourcePluginModel'
        db.create_table('cmsplugin_ressourcepluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('ressource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opst_plugins.Ressource'])),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opst_plugins.Categorie'])),
            ('sous_categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opst_plugins.SousCategorie'])),
        ))
        db.send_create_signal('opst_plugins', ['RessourcePluginModel'])

        # Adding model 'MultipleSearchBoxPluginModel'
        db.create_table('cmsplugin_multiplesearchboxpluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('result_page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='opst_plugin_multiplesearchbox', to=orm['cms.Page'])),
        ))
        db.send_create_signal('opst_plugins', ['MultipleSearchBoxPluginModel'])


    def backwards(self, orm):
        # Deleting model 'TagCloudPluginModel'
        db.delete_table('cmsplugin_tagcloudpluginmodel')

        # Deleting model 'SearchBoxPluginModel'
        db.delete_table('cmsplugin_searchboxpluginmodel')

        # Deleting model 'NewsFeedEntry'
        db.delete_table('opst_plugins_newsfeedentry')

        # Deleting model 'NewsFeedPluginModel'
        db.delete_table('cmsplugin_newsfeedpluginmodel')

        # Removing M2M table for field news on 'NewsFeedPluginModel'
        db.delete_table('opst_plugins_newsfeedpluginmodel_news')

        # Deleting model 'NewsFeedExtPluginModel'
        db.delete_table('cmsplugin_newsfeedextpluginmodel')

        # Deleting model 'NewsFeedPagePluginModel'
        db.delete_table('cmsplugin_newsfeedpagepluginmodel')

        # Removing M2M table for field pages on 'NewsFeedPagePluginModel'
        db.delete_table('opst_plugins_newsfeedpagepluginmodel_pages')

        # Deleting model 'Auteur'
        db.delete_table(u'auteur')

        # Deleting model 'Categorie'
        db.delete_table(u'categorie')

        # Deleting model 'Revue'
        db.delete_table(u'revue')

        # Deleting model 'Tag'
        db.delete_table(u'tag')

        # Deleting model 'SousCategorie'
        db.delete_table(u'sous_categorie')

        # Deleting model 'Ressource'
        db.delete_table(u'ressource')

        # Removing M2M table for field tags on 'Ressource'
        db.delete_table('ressource_tags')

        # Removing M2M table for field auteurs on 'Ressource'
        db.delete_table('ressource_auteurs')

        # Deleting model 'RessourceCatSsCat'
        db.delete_table(u'ressource_cat_ss_cat')

        # Deleting model 'RessourcePluginModel'
        db.delete_table('cmsplugin_ressourcepluginmodel')

        # Deleting model 'MultipleSearchBoxPluginModel'
        db.delete_table('cmsplugin_multiplesearchboxpluginmodel')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 19, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.page': {
            'Meta': {'ordering': "('site', 'tree_id', 'lft')", 'object_name': 'Page'},
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'moderator_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'opst_plugins.auteur': {
            'Meta': {'object_name': 'Auteur', 'db_table': "u'auteur'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        },
        'opst_plugins.categorie': {
            'Meta': {'object_name': 'Categorie', 'db_table': "u'categorie'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'})
        },
        'opst_plugins.multiplesearchboxpluginmodel': {
            'Meta': {'object_name': 'MultipleSearchBoxPluginModel', 'db_table': "'cmsplugin_multiplesearchboxpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'result_page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opst_plugin_multiplesearchbox'", 'to': "orm['cms.Page']"})
        },
        'opst_plugins.newsfeedentry': {
            'Meta': {'object_name': 'NewsFeedEntry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'opst_plugins.newsfeedextpluginmodel': {
            'Meta': {'object_name': 'NewsFeedExtPluginModel', 'db_table': "'cmsplugin_newsfeedextpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'list_max': ('django.db.models.fields.PositiveIntegerField', [], {'default': '8'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1024'})
        },
        'opst_plugins.newsfeedpagepluginmodel': {
            'Meta': {'object_name': 'NewsFeedPagePluginModel', 'db_table': "'cmsplugin_newsfeedpagepluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'list_max': ('django.db.models.fields.PositiveIntegerField', [], {'default': '8'}),
            'pages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['cms.Page']", 'null': 'True', 'blank': 'True'}),
            'parent_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parent_of_newsfeed'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'update_last': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1024'})
        },
        'opst_plugins.newsfeedpluginmodel': {
            'Meta': {'object_name': 'NewsFeedPluginModel', 'db_table': "'cmsplugin_newsfeedpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'list_max': ('django.db.models.fields.PositiveIntegerField', [], {'default': '8'}),
            'news': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opst_plugins.NewsFeedEntry']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'opst_plugins.ressource': {
            'Meta': {'object_name': 'Ressource', 'db_table': "u'ressource'"},
            'annee': ('django.db.models.fields.IntegerField', [], {}),
            'auteurs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opst_plugins.Auteur']", 'symmetrical': 'False'}),
            'date_debut': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'discipline': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'editeur': ('django.db.models.fields.CharField', [], {'max_length': '450', 'blank': 'True'}),
            'formation': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_revue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opst_plugins.Revue']", 'null': 'True', 'db_column': "'id_revue'", 'blank': 'True'}),
            'lien_texte': ('django.db.models.fields.CharField', [], {'max_length': '1800', 'blank': 'True'}),
            'lieu': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'mois': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'page_deb': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_fin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '900', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opst_plugins.Tag']", 'symmetrical': 'False'}),
            'texte': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '900'}),
            'type_production': ('django.db.models.fields.CharField', [], {'max_length': '900', 'blank': 'True'}),
            'type_rapport': ('django.db.models.fields.CharField', [], {'max_length': '900', 'blank': 'True'}),
            'universite': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        'opst_plugins.ressourcecatsscat': {
            'Meta': {'object_name': 'RessourceCatSsCat', 'db_table': "u'ressource_cat_ss_cat'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opst_plugins.Categorie']", 'db_column': "'id_categorie'"}),
            'id_ressource': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ressourcecatsscat'", 'db_column': "'id_ressource'", 'to': "orm['opst_plugins.Ressource']"}),
            'id_sous_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opst_plugins.SousCategorie']", 'db_column': "'id_sous_cat'"})
        },
        'opst_plugins.ressourcepluginmodel': {
            'Meta': {'object_name': 'RessourcePluginModel', 'db_table': "'cmsplugin_ressourcepluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opst_plugins.Categorie']"}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'ressource': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opst_plugins.Ressource']"}),
            'sous_categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opst_plugins.SousCategorie']"})
        },
        'opst_plugins.revue': {
            'Meta': {'object_name': 'Revue', 'db_table': "u'revue'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nb_num_revues': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        'opst_plugins.searchboxpluginmodel': {
            'Meta': {'object_name': 'SearchBoxPluginModel', 'db_table': "'cmsplugin_searchboxpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'result_page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opst_plugin_searchbox'", 'to': "orm['cms.Page']"})
        },
        'opst_plugins.souscategorie': {
            'Meta': {'object_name': 'SousCategorie', 'db_table': "u'sous_categorie'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'blank': 'True'})
        },
        'opst_plugins.tag': {
            'Meta': {'object_name': 'Tag', 'db_table': "u'tag'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'})
        },
        'opst_plugins.tagcloudpluginmodel': {
            'Meta': {'object_name': 'TagCloudPluginModel', 'db_table': "'cmsplugin_tagcloudpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'items_min': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3'}),
            'result_page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opst_plugin_tagcloud'", 'to': "orm['cms.Page']"})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['opst_plugins']