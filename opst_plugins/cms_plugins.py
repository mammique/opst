import re

from django.utils.translation import ugettext_lazy as _

from tagging.models import Tag

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from cms.plugins.inherit.cms_plugins import InheritPagePlaceholderPlugin
from cms.plugins.text.models import Text
from cms.models import Title

from .models import SearchBoxPlugin
from .forms import SearchBoxForm


re_blanks = re.compile('\s+')


class TagCloudPlugin(CMSPluginBase):

    model = SearchBoxPlugin
    name = _("Tag Cloud Plugin")
    render_template = "cms_plugins/tagcloud.html"

    def render(self, context, instance, placeholder):

        context.update({'instance': instance,
                        'tags': map(lambda t: (t, 10 + t.items.all().count() * 3),
                            Tag.objects.exclude(name='footer'))})

        return context

plugin_pool.register_plugin(TagCloudPlugin)


class SearchBoxPlugin(CMSPluginBase):

    model = SearchBoxPlugin
    name = _("Search Box Plugin")
    render_template = "cms_plugins/searchbox.html"

    def render(self, context, instance, placeholder):

        f = SearchBoxForm(context['request'].GET)
        context.update({'instance': instance,
                        'form': f})

        return context

plugin_pool.register_plugin(SearchBoxPlugin)


class SearchResultPlugin(CMSPluginBase):

    model = CMSPlugin
    name = _("Search Result Plugin")
    render_template = "cms_plugins/searchresult.html"

    def render(self, context, instance, placeholder):

        results = {}

        f = SearchBoxForm(context['request'].GET)

        if f.is_valid():

            q = f.cleaned_data.get('q')
            q_re = '(%s)' % '|'.join(re_blanks.split(q))

            for i in list(Title.objects.filter(title__iregex=q_re)):
                if not i.page in results: results[i.page] = i.title

            for i in list(Text.objects.filter(body__iregex=q_re)):
                if not i.page in results: results[i.page] = i.body

        context.update({'results': results, 'results_n': len(results)})

        return context

plugin_pool.register_plugin(SearchResultPlugin)


class SitemapPlugin(CMSPluginBase):

    model = CMSPlugin
    name = _("Sitemap Plugin")
    render_template = "cms_plugins/sitemap.html"

    def render(self, context, instance, placeholder):

        return context

plugin_pool.register_plugin(SitemapPlugin)


#class ChildPagesPlugin(CMSPluginBase):

#    model = CMSPlugin
#    name = _("Child Pages Plugin")
#    render_template = "cms_plugins/childpages.html"

#    def render(self, context, instance, placeholder):

#        return context

#plugin_pool.register_plugin(ChildPagesPlugin)


class FocusPlugin(InheritPagePlaceholderPlugin):

    render_template = "cms_plugins/focus.html"
    name = _("Focus Plugin")

    def render(self, context, instance, placeholder):

        context = super(FocusPlugin, self).render(context, instance, placeholder)
        context.update({'focus_page': instance.from_page})

        return context


plugin_pool.register_plugin(FocusPlugin)

