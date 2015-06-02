# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        if not db.dry_run:
            for r in orm.Ressource.objects.all():
                r.slug = r.slug[0:255]
                r.save()

        # Changing field 'Ressource.slug'
        db.alter_column('opst_plugins_ressource', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255))
        # Adding unique constraint on 'Ressource', fields ['slug']
        db.create_unique('opst_plugins_ressource', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Ressource', fields ['slug']
        db.delete_unique('opst_plugins_ressource', ['slug'])

        # Changing field 'Ressource.slug'
        db.alter_column('opst_plugins_ressource', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=767))

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 6, 2, 0, 0)'}),
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
            'Meta': {'ordering': "['nom']", 'object_name': 'Auteur'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '90', 'db_index': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '90', 'db_index': 'True'})
        },
        'opst_plugins.categorie': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Categorie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '120', 'db_index': 'True'}),
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
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
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
            'Meta': {'ordering': "['annee', 'titre']", 'object_name': 'Ressource'},
            'annee': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'auteurs': ('sortedm2m.fields.SortedManyToManyField', [], {'to': "orm['opst_plugins.Auteur']", 'symmetrical': 'False'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['opst_plugins.Categorie']", 'null': 'True', 'blank': 'True'}),
            'date_debut': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'discipline': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '300', 'blank': 'True'}),
            'editeur': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '450', 'blank': 'True'}),
            'formation': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '300', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lien_texte': ('django.db.models.fields.CharField', [], {'max_length': '767', 'blank': 'True'}),
            'lieu': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '300', 'blank': 'True'}),
            'mois': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'blank': 'True'}),
            'page_deb': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_fin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'revue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opst_plugins.Revue']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'subcats': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['opst_plugins.SousCategorie']", 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['opst_plugins.Tag']", 'symmetrical': 'False'}),
            'texte': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '767', 'db_index': 'True'}),
            'type_production': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '767', 'blank': 'True'}),
            'type_rapport': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '767', 'blank': 'True'}),
            'universite': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '300', 'blank': 'True'})
        },
        'opst_plugins.ressourcelistpluginpluginmodel': {
            'Meta': {'object_name': 'RessourceListPluginPluginModel', 'db_table': "'cmsplugin_ressourcelistpluginpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'result_page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opst_plugin_ressource_list'", 'to': "orm['cms.Page']"})
        },
        'opst_plugins.ressourcepluginmodel': {
            'Meta': {'object_name': 'RessourcePluginModel', 'db_table': "'cmsplugin_ressourcepluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opst_plugins.Categorie']"}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'ressource': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opst_plugins.Ressource']"}),
            'sous_categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opst_plugins.SousCategorie']"})
        },
        'opst_plugins.ressourcepluginpluginmodel': {
            'Meta': {'object_name': 'RessourcePluginPluginModel', 'db_table': "'cmsplugin_ressourcepluginpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'result_page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opst_plugin_ressource'", 'to': "orm['cms.Page']"})
        },
        'opst_plugins.revue': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Revue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nb_num_revues': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '600', 'db_index': 'True'})
        },
        'opst_plugins.searchboxpluginmodel': {
            'Meta': {'object_name': 'SearchBoxPluginModel', 'db_table': "'cmsplugin_searchboxpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'result_page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opst_plugin_searchbox'", 'to': "orm['cms.Page']"})
        },
        'opst_plugins.searchresultpluginmodel': {
            'Meta': {'object_name': 'SearchResultPluginModel', 'db_table': "'cmsplugin_searchresultpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'ressource_page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opst_plugin_searchresult'", 'to': "orm['cms.Page']"})
        },
        'opst_plugins.souscategorie': {
            'Meta': {'ordering': "['nom']", 'object_name': 'SousCategorie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '120', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'blank': 'True'})
        },
        'opst_plugins.tag': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '120', 'db_index': 'True'}),
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
