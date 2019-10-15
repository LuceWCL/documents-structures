# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 09:39:41 2019

@author: Lucie
"""

from lxml import etree
xmlfile = "valery_ame-et-danse_1921.xml"
# Initialiser la lecture du fichier
tree = etree.parse(xmlfile)
# Le contenu en tant que string = nom de l'élément
print(etree.tostring(tree))
# La racine
root = tree.getroot() #renvoie un objet élément
print(root.tag)
# Utiliser un espace de nom
# lxml a une syntaxe propre à lui = indiquer par des accolades le space-name
TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
TEI = "{%s}" % TEI_NAMESPACE
# Obtenir le tag et valeur des enfants de <titleStmt>
#iterer à travers tout le document
#si on spécifie un attribut ("nom_de_balise"), l'itération s'arrête sinon va jusqu'à la fin sans s'arrêter
#el.tag == balise
#el.text = entre les balises
for element in root.iter(TEI + 'titleStmt'):
    for child in element:
        print(child.tag, child.text, child.attrib)
# Afficher les attributs (dictionnaire de tous les attributs de l'élément courant)
print(root.attrib)
# Afficher un attribut particulier
print(root.get('{http://www.w3.org/XML/1998/namespace}' + 'lang'))
# Ajouter un attribut avec son nom et sa vlaeur 
root.set('nouvel-attribut', 'documentsStructures')
#print(root.attrib)
# Ajouter un enfant
text = etree.SubElement(root, "text")
#text.text = "un texte"
#text.set("un-attribut", 'une-valeur')
# Afficher joliment
print(etree.tostring(root, pretty_print=True))