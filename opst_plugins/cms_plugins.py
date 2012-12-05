from django.utils.translation import ugettext_lazy as _

from tagging.models import Tag

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin


class TagCloudPlugin(CMSPluginBase):

    model = CMSPlugin
    name = _("Tag Cloud Plugin")
    render_template = "cms_plugins/tagcloud.html"

    def render(self, context, instance, placeholder):

        context.update({'tags': map(lambda t: (t, 10 + t.items.all().count() * 3),
            Tag.objects.all())})

        return context

plugin_pool.register_plugin(TagCloudPlugin)
