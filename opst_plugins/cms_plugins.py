import re, copy

from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.safestring import mark_safe

from tagging.models import Tag

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin as CMSPluginModel
from cms.plugins.inherit.cms_plugins import InheritPagePlaceholderPlugin
#from cms.plugins.inherit.models import InheritPagePlaceholder
from cms.plugins.text.models import Text
from cms.models import Title, Page
from cms.utils import get_language_from_request
from cms.utils.moderator import get_cmsplugin_queryset

from .models import SearchBoxPluginModel, NewsFeedPluginModel, NewsFeedExtPluginModel
from .forms import SearchBoxForm


re_blanks = re.compile('\s+')


class TagCloudPlugin(CMSPluginBase):

    model = SearchBoxPluginModel
    name = _("Tag Cloud")
    render_template = "cms_plugins/tagcloud.html"

    def render(self, context, instance, placeholder):

        context.update({'instance': instance,
                        'tags': map(lambda t: (t, 10 + t.items.all().count() * 3),
                            Tag.objects.exclude(name='footer'))})

        return context

plugin_pool.register_plugin(TagCloudPlugin)


class SearchBoxPlugin(CMSPluginBase):

    model = SearchBoxPluginModel
    name = _("Search Box")
    render_template = "cms_plugins/searchbox.html"

    def render(self, context, instance, placeholder):

        f = SearchBoxForm(context['request'].GET)
        context.update({'instance': instance,
                        'form': f})

        return context

plugin_pool.register_plugin(SearchBoxPlugin)


class SearchResultPlugin(CMSPluginBase):

    model = CMSPluginModel
    name = _("Search Result")
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

    model = CMSPluginModel
    name = _("Sitemap")
    render_template = "cms_plugins/sitemap.html"

    def render(self, context, instance, placeholder):

        return context

plugin_pool.register_plugin(SitemapPlugin)


class BranchMapPlugin(CMSPluginBase):

    model = CMSPluginModel
    name = _("Branch map")
    render_template = "cms_plugins/branchmap.html"

    def render(self, context, instance, placeholder):

        return context

plugin_pool.register_plugin(BranchMapPlugin)


#class ChildPagesPlugin(CMSPluginBase):

#    model = CMSPluginModel
#    name = _("Child Pages")
#    render_template = "cms_plugins/childpages.html"

#    def render(self, context, instance, placeholder):

#        return context

#plugin_pool.register_plugin(ChildPagesPlugin)


class FocusPlugin(InheritPagePlaceholderPlugin):

    render_template = "cms_plugins/focus.html"
    name = _("Focus")

    def render(self, context, instance, placeholder):

        context = super(FocusPlugin, self).render(context, instance, placeholder)
        context.update({'focus_page': instance.from_page})

        return context

plugin_pool.register_plugin(FocusPlugin)


class NewsFeedPlugin(CMSPluginBase):

    model = NewsFeedPluginModel
    render_template = "cms_plugins/newsfeed.html"
    name = _("News Feed")
    filter_horizontal = ('news',)

    def render(self, context, instance, placeholder):

#        context = super(NewsFeedPluginModel, self).render(context, instance, placeholder)
        context.update({
            'newsfeed': instance.news.filter(
                publication_date__isnull=False)
                .order_by('-publication_date')[0:instance.list_max],
            'instance': instance})

        return context

plugin_pool.register_plugin(NewsFeedPlugin)


class NewsFeedExtPlugin(CMSPluginBase):

    model = NewsFeedExtPluginModel
    render_template = "cms_plugins/newsfeedext.html"
    name = _("News Feed External")
    filter_horizontal = ('news',)

    def render(self, context, instance, placeholder):

        import feedparser

        try: 
            context.update({
                'newsfeedext': feedparser.parse(instance.url)['entries'][0:instance.list_max],
                'instance': instance})
        except: pass

        return context


plugin_pool.register_plugin(NewsFeedExtPlugin)


class CarouslideRecentPagesPlugin(CMSPluginBase): #InheritPagePlaceholderPlugin):

#    model = CMSPluginModel
    render_template = "cms_plugins/carouslide.html"
    name = _("Carouslide Recent Pages")

    def render(self, context, instance, placeholder):

        # https://github.com/divio/django-cms/blob/develop/cms/plugins/inherit/cms_plugins.py

        template_vars = {
            'placeholder': placeholder,
        }
        template_vars['object'] = instance
        request = context.get('request', None)
        if context.has_key('request'):
            lang = get_language_from_request(request)
        else:
            lang = settings.LANGUAGE_CODE
        page = instance.placeholder.page
        divs = []

        from_pages = Page.objects.published().exclude(pk=page.pk).order_by('-publication_date')[0:5]

        for from_page in from_pages:

            if page.publisher_is_draft:
                from_page = from_page.get_draft_object()
            else:
                from_page = from_page.get_public_object()

            plugins = get_cmsplugin_queryset(request).filter(
                placeholder__page=from_page,
                language=lang,
                placeholder__slot__iexact='page', #placeholder,
                parent__isnull=True
            ).order_by('position').select_related()
            plugin_output = ['<h1>%s</h1>' % from_page.get_title()]
            template_vars['parent_plugins'] = plugins 
            for plg in plugins:
                tmpctx = copy.copy(context)
                tmpctx.update(template_vars)
                inst, name = plg.get_plugin_instance()
                if inst is None:
                    continue
                outstr = inst.render_plugin(tmpctx, placeholder)
                plugin_output.append(outstr)
            if from_page == from_pages[0]:
                el_attrs = 'class="button carouslide-focus"'
            else:
                el_attrs = 'class="button carouslide-blur"'
            divs.append('<div onclick="document.location=\'%s\'" %s>%s</div>' % \
                (from_page.get_absolute_url(), el_attrs, ''.join(plugin_output)))
#        template_vars['carouslide_content'] = mark_safe('<div>%s</div>' % \
#            '</div><div>'.join(divs))
        template_vars['carouslide_content'] = mark_safe(''.join(divs))
        context.update(template_vars)
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CarouslideRecentPagesPlugin)
