from django.db import models

from cms.models import CMSPlugin


class SearchBoxPlugin(CMSPlugin):

    result_page = models.ForeignKey('cms.Page', related_name='opst_plugin_searchbox')
