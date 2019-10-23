# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:28:43 2019

@author: Lucie
"""

from lxml import etree
xmlfile = "valery_ame-et-danse_1921.xml"
tree = etree.parse(xmlfile)
root = tree.getroot()
TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
TEI = "{%s}" % TEI_NAMESPACE

#affiche le nom de l'éditeur <edition>
for element in root.iter(TEI + 'edition'):
    print(element.text)
        
#affiche l'url de la licence <licence>
for element in root.iter(TEI + 'ref'):
    print(element.attrib.get('target'))

#afficher le personnage avec le plus de réplique (@speaker)
#et le nombre de répliques
d={}
for element in root.iter(TEI + "label"):
    d[element.text] = d.get(element.text,0)+1
print(sorted(d.items(),key=lambda x:x[1],reverse=True))

#ajouter un autre <respStmt> avec deux enfants nam et resp contenant du texte
for element in root.iter(TEI + 'editionStmt'):
    respStmt = etree.SubElement(element,"respStmt")
    name = etree.SubElement(respStmt,"name")
    resp = etree.SubElement(respStmt,"resp")
    name.text = "name"
    resp.text = "resp"
#print(etree.tostring(root, pretty_print=True))
tree.write('xmlfile.xml',encoding = 'utf-8', pretty_print=True)

#modifier la valeur de la signateur <signed> pour afficher le texte en majuscule
for element in root.iter(TEI + 'signed'):
    for child in element:
        child.text = child.text.upper()
#print(etree.tostring(root, pretty_print=True))
tree.write('xmlfile.xml',encoding = 'utf-8',pretty_print=True)