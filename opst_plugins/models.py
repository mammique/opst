# -*- coding: utf-8 -*-
from datetime import date

from django.db import models
from django.template.defaultfilters import slugify

from cms.models import CMSPlugin


class TagCloudPluginModel(CMSPlugin):

    result_page = models.ForeignKey('cms.Page', related_name='opst_plugin_tagcloud')
    items_min   = models.PositiveIntegerField(default=3)


class SearchBoxPluginModel(CMSPlugin):

    result_page = models.ForeignKey('cms.Page', related_name='opst_plugin_searchbox')


class SearchResultPluginModel(CMSPlugin):

    ressource_page = models.ForeignKey('cms.Page', related_name='opst_plugin_searchresult')


class RessourcePluginPluginModel(CMSPlugin):

    result_page = models.ForeignKey('cms.Page', related_name='opst_plugin_ressource')


class NewsFeedEntry(models.Model):

    title            = models.CharField(max_length=128)
    url              = models.URLField()
    publication_date = models.DateTimeField(db_index=True, blank=True, null=True)

    def __unicode__(self): return self.title


class NewsFeedPluginModel(CMSPlugin):

    title    = models.CharField(max_length=128)
    list_max = models.PositiveIntegerField(default=8)
    news     = models.ManyToManyField(NewsFeedEntry)


class NewsFeedExtPluginModel(CMSPlugin):

    title    = models.CharField(max_length=128)
    list_max = models.PositiveIntegerField(default=8)
    url      = models.URLField(max_length=1024)


class NewsFeedPagePluginModel(CMSPlugin):

    title       = models.CharField(max_length=128)
    list_max    = models.PositiveIntegerField(default=8)
    url         = models.URLField(max_length=1024)
    update_last = models.DateTimeField(blank=True, null=True)
    pages       = models.ManyToManyField('cms.Page', blank=True, null=True)
    parent_page = models.ForeignKey('cms.Page', blank=True, null=True, related_name='parent_of_newsfeed')

    def update(self):

        import feedparser

        from time import mktime
        from datetime import datetime
        from slugify import slugify

        from django.contrib.sites.models import Site

        from cms.models import Page, Title
        from cms.plugins.text.models import Text

        try: p_last = self.pages.latest('publication_date')
        except Page.DoesNotExist: p_last = None

        try:

            for e in feedparser.parse(self.url)['entries']:

                date  = e.get('published_parsed')
                title = e.get('title')
                body  = e.get('summary')
                url   = e.get('link')

                if date and title and body:

                    date = datetime.fromtimestamp(mktime(date))

                    if p_last and date <= p_last.publication_date: continue

                    p=Page(site=Site.objects.all()[0], in_navigation=False, published=True, template='page-full.html')
                    p.publication_date = date

                    if self.parent_page: p.parent = self.parent_page
            
                    p.save()

                    self.pages.add(p)
                    self.save()

                    t=Title(language='en', title=title, slug='%s-%s' % (slugify(title), p.pk), page=p)
                    t.save()
        
                    pl=p.placeholders.get(slot='page')

                    if url: body = u'%s<p><a href="%s">Lire la suite de l\'article…</a></p>' % (body, url)
                    txt=Text(body=body, language='en', plugin_type='TextPlugin')
                    txt.save()

                    pl.cmsplugin_set.add(txt)
                    pl.save()

        except: pass

        self.update_last = datetime.now()
        self.save()


class Auteur(models.Model):

    nom    = models.CharField(db_index=True, max_length=90)
    prenom = models.CharField(db_index=True, max_length=90)

    def __unicode__(self): return self.nom + ' ' + self.prenom 

    class Meta:
        ordering = ['nom']


class Categorie(models.Model):

    nom  = models.CharField(db_index=True, max_length=120)
    slug = models.SlugField(max_length=150)

    def __unicode__(self): return self.nom

    class Meta:
        ordering = ['nom']


class Revue(models.Model):

    nom           = models.CharField(db_index=True, max_length=600)
    nb_num_revues = models.IntegerField(null=True, blank=True, verbose_name="Nombre de numéros de revues")

    def __unicode__(self): return self.nom

    class Meta:
        ordering = ['nom']


class Tag(models.Model):

    nom  = models.CharField(db_index=True, max_length=120)
    slug = models.SlugField(max_length=150)

    def __unicode__(self): return self.nom

    def nb_tags(self): return self.items.count()

    nb_tags.short_description = 'Nombre d\'utilisations du tag'

    class Meta:
        ordering = ['nom']

class SousCategorie(models.Model):

    nom  = models.CharField(db_index=True, max_length=120)
    slug = models.SlugField(max_length=150, blank=True)

    def __unicode__(self): return self.nom

    class Meta:
        ordering = ['nom']


ressource_mois_choices = (
                          ('01',    'janvier'),
                          ('02',    'février'),
                          ('03',    'mars'),
                          ('04',    'avril'),
                          ('05',    'mai'),
                          ('06',    'juin'),
                          ('07',    'juillet'),
                          ('08',    'août'),
                          ('09',    'septembre'),
                          ('10',    'octobre'),
                          ('11',    'novembre'),
                          ('12',    'décembre'),

                          ('01-02', 'janvier-février'),
                          ('02-03', 'février-mars'),
                          ('03-04', 'mars-avril'),
                          ('04-05', 'avril-mai'),
                          ('05-06', 'mai-juin'),
                          ('06-07', 'juin-juillet'),
                          ('07-08', 'juillet-août'),
                          ('08-09', 'août-septembre'),
                          ('09-10', 'septembre-octobre'),
                          ('10-11', 'octobre-novembre'),
                          ('11-12', 'novembre-décembre'),
                          ('12-01', 'décembre-janvier'),

                          ('09-12', 'automne'),
                          ('12-03', 'hiver'),
                          ('03-06', 'printemps'),
                          ('06-09', 'été'),
                         )

ressource_year_choices = map(lambda x: (x, '%s'%x), range(1950, (date.today().year+2)))
ressource_year_choices.reverse()

class Ressource(models.Model):

    titre           = models.CharField(db_index=True, max_length=767)
    slug            = models.SlugField(max_length=767, blank=True)
    texte           = models.TextField(db_index=True, blank=True)
    lien_texte      = models.CharField(max_length=767, blank=True)
    annee           = models.IntegerField(db_index=True, choices=ressource_year_choices)
    mois            = models.SlugField(max_length=30, blank=True, choices=ressource_mois_choices)
    lieu            = models.CharField(db_index=True, max_length=300, blank=True)
    page_deb        = models.IntegerField(null=True, blank=True, verbose_name='Page de début')
    page_fin        = models.IntegerField(null=True, blank=True, verbose_name='Page de fin')
    date_debut      = models.DateField(null=True, blank=True, verbose_name='Date de début')
    date_fin        = models.DateField(null=True, blank=True, verbose_name='Date de fin')
    editeur         = models.CharField(db_index=True, max_length=450, blank=True)
    formation       = models.CharField(db_index=True, max_length=300, blank=True)
    universite      = models.CharField(db_index=True, max_length=300, blank=True, verbose_name='Université')
    discipline      = models.CharField(db_index=True, max_length=300, blank=True)
    type_production = models.CharField(db_index=True, max_length=767, blank=True)
    type_rapport    = models.CharField(db_index=True, max_length=767, blank=True)
    revue           = models.ForeignKey(Revue, verbose_name= 'Nom de la revue attribuée', null=True, blank=True)
    tags            = models.ManyToManyField(Tag)
    auteurs         = models.ManyToManyField(Auteur)
    categories      = models.ManyToManyField(Categorie, verbose_name=u'Catégorie', null=True, blank=True)
    subcats         = models.ManyToManyField(SousCategorie, verbose_name=u'Sous-Catégorie', null=True, blank=True)

    def __unicode__(self): return self.titre

    class Meta:
        ordering = ['annee', 'titre']


class RessourcePluginModel(CMSPlugin):
    
    ressource      = models.ForeignKey(Ressource, verbose_name='Ressource')
    categorie      = models.ForeignKey(Categorie, verbose_name='Catégorie')
    sous_categorie = models.ForeignKey(SousCategorie, verbose_name='Sous-Catégorie')


class MultipleSearchBoxPluginModel(CMSPlugin):
	
    result_page = models.ForeignKey('cms.Page', related_name="opst_plugin_multiplesearchbox")
