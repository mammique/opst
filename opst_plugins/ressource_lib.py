#-*- coding:utf-8 -*-
import operator

from django.db.models import Q
from django.template.defaultfilters import slugify

from .models import *


CRITERES_POSSIBLES = (
	('TITRE', 'Titre'),
	('TEXTE', 'Texte'),
	('FORMATION', 'Formation'),
	('UNIVERSITE', 'Universite'), 
	('DISCIPLINE', 'Discipline'),
	('TYPE_RAPPORT', 'Type de rapport'),
	('ANNEE', 'Annee de publication'),
	('AUTEUR_NOM', 'Auteur(nom)'),
	('AUTEUR', 'Auteur(nom prenom)'),
	('CATEGORIE', 'Catégorie'),
	('SOUS_CATEGORIE', 'Sous Catégorie'),
	('REVUE', 'Revue'),
	('TAG', 'Tag')
)

COMPARATEURS_POSSIBLES = (
	('CONTIENT', 'contient'),
	('EXACT', 'est exactement'),
	('COMMENCE', 'commence par'),
	('FINIT', 'finit par'),
	('SUP', 'supérieure à'),
	('SUP_EQ', 'supérieure ou égale à'),
	('INF', 'inférieure à'),
	('INF_EQ', 'inférieure ou égale à')
)

OPERATEURS_LOGIQUES = (
	('ET', 'et'),
	('OU', 'ou'),
	('SAUF', 'sauf'),
)

comp = {
	'CONTIENT': '__icontains',
	'EXACT': '__iexact',
	'COMMENCE': '__istartswith',
	'FINIT': '__iendswith',
	'SUP': '__gt',
	'SUP_EQ': '__gte',
	'INF': '__lt',
	'INF_EQ': '__lte'
}

op = {
	'OU': operator.or_,
	'ET': operator.and_,
	'SAUF': operator.and_
}

fields = {
	'TITRE': 'titre',
	'TEXTE': 'texte',
	'AUTEUR_NOM': 'auteurs__nom',
	#'CATEGORIE': 'ressourcecatsscat__id_categorie__nom',
	#'SOUS_CATEGORIE': 'ressourcecatsscat__id_sous_cat__nom',
	'CATEGORIE': 'categories__nom',
	'SOUS_CATEGORIE': 'subcats__nom',
	'REVUE': 'revue',
	'FORMATION': 'formation',
	'UNIVERSITE': 'universite', 
	'DISCIPLINE': 'discipline',
	'TYPE_RAPPORT': 'type_rapport',
	'ANNEE': 'annee',
	'TAG' : 'tags__nom'
}


class ListeRequete(list):
	def __init__(self):
		list.__init__(self)
		
	def item_exists(self, item):
		return item in self

	def traitement_requete(self, chaine):
		""" Traite le résultat d'une requete sur la table "table"
			sur les attributs "*att"
			à partir de la chaine donnée """
		req = ListeRequete()
		""" POUR UN TAG """
		# On récupère tous les éléments correspondant dans la table
		try:
			req + Tag.objects.filter(slug__startswith=slugify(chaine))
		except KeyError:
			pass
		# Si on obtient des résultats
		if req:
			# On récupère les id ressources associées à la table
			for elem in req:
				# On récupère toutes les id_ressources en rapport ave un id_tag
				for un_tag in elem.items.all():
					try:
						self + Ressource.objects.filter(id=un_tag.id_ressource.id)
					except KeyError:
						pass
		else:
			""" POUR UN AUTEUR """
			# On récupère tous les éléments correspondant dans la table
			try:
				req + Auteur.objects.filter(nom__contains=chaine.capitalize())
			except KeyError:
				pass
			try:
				req + Auteur.objects.filter(prenom__contains=chaine.capitalize())
			except KeyError:
				pass
			# Si on obtient des résultats
			if req:
				# On récupère les id ressources associées à la table
				for elem in req:
					# On récupère toutes les id_ressources en rapport avec un id_tag
					for un_auteur in elem.ressourceauteur_set.all():
						try:
							self + Ressource.objects.filter(id=un_auteur.id_ressource.id)
						except KeyError:
							pass
			else:
				""" POUR UNE REVUE """
				# On récupère tous les éléments correspondant dans la table
				try:
					req + Revue.objects.filter(nom__contains=chaine.capitalize())
				except KeyError:
					pass
				# Si on obtient des résultats
				if req:
					# On récupère les id ressources associées à la table
					for elem in req:
						# On récupère toutes les id_ressources en rapport avec un id_tag
						for une_ressource in elem.ressource_set.all():
							try:
								self + Ressource.objects.filter(id=une_ressource.id)
							except KeyError:
								pass
				else:
					""" POUR UNE SOUS-CATEGORIE """
					# On récupère tous les éléments correspondant dans la table
					try:
						req + SousCategorie.objects.filter(slug__contains=chaine)
					except KeyError:
						pass
					# Si on obtient des résultats
					if req:
						# On récupère les id ressources associées à la table
						for elem in req:
							# On récupère toutes les id_ressources en rapport avec un id_tag
							for une_ressource in elem.ressourcecatsscat_set.all(): # FIXME: WTF!?
								try:
									self + Ressource.objects.filter(id=une_ressource.id_ressource.id)
								except KeyError:
									pass
					else:
						""" POUR UNE CATEGORIE """
						# On récupère tous les éléments correspondant dans la table
						try:
							req + Categorie.objects.filter(slug__contains=chaine)
						except KeyError:
							pass
						# Si on obtient des résultats
						if req:
							# On récupère les id ressources associées à la table
							for elem in req:
								# On récupère toutes les id_ressources en rapport avec un id_tag
								for une_ressource in elem.ressourcecatsscat_set.all(): # FIXME: WTF!?
									try:
										self + Ressource.objects.filter(id=une_ressource.id_ressource.id)
									except KeyError:
										pass
		""" POUR UNE RESSOURCE """
		# On récupère tous les éléments correspondant dans la table
		try:
			self + Ressource.objects.filter(titre__contains=chaine)
		except KeyError:
			pass
		try:
			self + Ressource.objects.filter(slug__contains=slugify(chaine))
		except KeyError:
			pass
		try:
			self + Ressource.objects.filter(texte__contains=chaine)
		except KeyError:
			pass
		try:
			if is_number(chaine):
				self + Ressource.objects.filter(annee=chaine)
		except KeyError:
			pass
		
		return self

	def __add__(self, une_liste):
		""" Ajoute une liste à notre liste """
		for un_item in une_liste:
			if un_item in self:
				raise KeyError()
			self.append(un_item)
		return self
		
	def __str__(self):
		chaine = str("[")
		for i,un_item in enumerate(self):
			chaine += un_item
			if i != len(self) - 1:
				chaine += ", "
		chaine += "]"
		return chaine
#--------- FIN DE LA CLASSE ---------#	
	
def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False


def traitement_requete_simple(query):
	""" Cette fonction traite la chaine query donne
		en parametre et renvoie une liste
		de ressources correspondantes """
	# On regroupe tous les mots separes par des espaces dans une liste
	liste = query.split()
	# Si la liste n'est pas vide on la rempli avec toutes les ressources qui existent 
	if liste:
		req = Ressource.objects.all()
	else:
		req = []
	# la liste va etre filtree a chaque iteration et va conserver les ressources en rapport avec les chaines donnees
	for chaine in liste:
		req = req.filter( Q(tags__nom__iexact=chaine) \
				| Q(revue__nom__icontains=chaine) \
				| Q(auteurs__nom__icontains=chaine) \
				| Q(auteurs__prenom__iexact=chaine) \
				| Q(editeur__iexact=chaine) \
				| Q(subcats__nom__icontains=chaine) \
				| Q(titre__icontains=chaine) \
				| Q(texte__icontains=chaine) \
				| Q(formation__icontains=chaine) \
				| Q(universite__icontains=chaine) \
				| Q(discipline__icontains=chaine) \
				| Q(annee__iexact=chaine)).distinct().order_by('-annee')
	# On recupere le total de resultats pour un affichage ulterieur
	nb_res = len(req)
	# On renvoie un tuple contenant l'ensemble des ressources d'une page donnee et le total des resultats
	return (req, nb_res)


def traitement_requete_avancee(context):
	""" Permet de realiser une recherche multicriteres a
		partir des parametres de l'url contenues dans context """
	# On appelle la fonction requete a partir des parametre des champ du formulaire
	argument_1 = requete(context['request'].GET.get('query_1'), context['request'].GET.get('comp_1'), context['request'].GET.get('crit_1'))
	argument_2 = requete(context['request'].GET.get('query_2'), context['request'].GET.get('comp_2'), context['request'].GET.get('crit_2'), context['request'].GET.get('op_1'))
	argument_3 = requete(context['request'].GET.get('query_3'), context['request'].GET.get('comp_3'), context['request'].GET.get('crit_3'), context['request'].GET.get('op_2'))
	argument_4 = requete(context['request'].GET.get('query_4'), context['request'].GET.get('comp_4'), context['request'].GET.get('crit_4'), context['request'].GET.get('op_3'))
	# On filtre le contenu du modele Ressource selon les arguments definis au-dessus et on trie par defaut par annees
	req = Ressource.objects.filter(reduce(op[context['request'].GET.get('op_3')], \
								[reduce(op[context['request'].GET.get('op_2')], \
								[reduce(op[context['request'].GET.get('op_1')], \
								[argument_1, argument_2]), argument_3]), argument_4])).distinct().order_by('-annee')
	# On recupere le nombre de resultats
	nb_res = len(req)
	# On renvoie un tuple avec les resultats et le nombre
	return (req, nb_res)


def requete(query, compar, field, oper=''):
	""" Cette fonction effectue une requete sur un champ renseigne field
		qui est compare au mot-clé query a partir du comparateur compar """
	# Si le champ passe en parametre est Auteur nom et prenom
	if field == 'AUTEUR':
		# On range les mots-cles dans une liste
		liste = query.split()
		try:
			ch_1 = liste.pop()
			ch_2 = liste.pop()
			# Si l'operateur logique est SAUF
			if oper == 'SAUF':
				# On enleve les resultats de cette requete au resultat final
				return ~Q(Q(**{'auteurs__nom'+comp[compar]: ch_1}) & Q(**{'auteurs__prenom'+comp[compar]: ch_2}) | Q(**{'auteurs__nom'+comp[compar]: ch_2}) & Q(**{'auteurs__prenom'+comp[compar]: ch_1}))
			else:
				# Sinon on recupere les resultats
				return Q(Q(**{'auteurs__nom'+comp[compar]: ch_1}) & Q(**{'auteurs__prenom'+comp[compar]: ch_2}) | Q(**{'auteurs__nom'+comp[compar]: ch_2}) & Q(**{'auteurs__prenom'+comp[compar]: ch_1}))
		# Dans le cas ou il n'y a aucun ou qu'un mot-cle donne
		except IndexError:
			# Si l'operateur logique est SAUF
			if oper == 'SAUF':
				# On enleve les resultats de cette requete au resultat final
				return(~Q(**{'auteurs__nom'+comp[compar]: query}))
			else:
				# Sinon on recupere les resultats
				return(Q(**{'auteurs__nom'+comp[compar]: query}))
	# Dans les autres cas ou le champ n'est pas AUTEUR
	# Si l'operateur logique est SAUF
	if oper == "SAUF":
		# On enleve les resultats de cette requete au resultat final
		return ~Q(**{fields[field]+comp[compar]: query})
	else:
		# Sinon on recupere les resultats
		return Q(**{fields[field]+comp[compar]: query})


def get_ressources(path):
	""" Cette fonction permet de récupérer l'ensemble des ressources
		d'une sous-catégorie d'une catégorie à partir de l'url path donnée """
	path = path.strip('/')
	(cat,sous_cat) = path.split('/')
	return Ressource.objects.filter(categories__slug__iexact=cat, subcats__slug__iexact=sous_cat).order_by('-annee')


def get_dates(ressources):
	list = []
	for res in ressources:
		if res.annee not in list:
			list.append(res.annee)
	list.sort(key=int)
	return list
	
	
