# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from opst_plugins.models import Ressource
from django.template import *
from django.shortcuts import render
from django.utils import timezone
from ressource_lib import *

def ressource(request, slug):

    """ Affiche une ressource complete comprenant
        les tags, les auteurs, les categories """
    edit = request.GET.get('edit')
    # Récupération de la ressource
    ressource = Ressource.objects.get(slug=slug)
    # Récupération de la revue
    try:
        revue = Revue.objects.get(pk=ressource.revue.pk)
    except AttributeError:
        pass
    # Récupération des auteurs
    auteurs = ressource.auteurs.all()
    # Récupération des tags
    tags = ressource.tags.all()

    return render(request, 'recherche/affichage_page.html', locals())
