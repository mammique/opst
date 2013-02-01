from django.db import models

from cms.models import CMSPlugin


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

