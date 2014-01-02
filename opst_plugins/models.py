# -*- coding: utf-8 -*-
from django.db import models

from cms.models import CMSPlugin


class TagCloudPluginModel(CMSPlugin):

    result_page = models.ForeignKey('cms.Page', related_name='opst_plugin_tagcloud')
    items_min = models.PositiveIntegerField(default=3)


class SearchBoxPluginModel(CMSPlugin):

    result_page = models.ForeignKey('cms.Page', related_name='opst_plugin_searchbox')

class NewsFeedEntry(models.Model):

    title            = models.CharField(max_length=128)
    url              = models.URLField()
    publication_date = models.DateTimeField(blank=True, null=True)

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
