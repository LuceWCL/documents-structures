# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:17:25 2019

@author: Lucie
"""

from lxml import etree
xmlfile = "Duchn-etiquetage.txt.xml"
tree = etree.parse(xmlfile)
root = tree.getroot()

#extraire les determinants
det = []
for elt in root.iter('element'):
    for child in elt:
        if child.attrib.get("type")=="type" and "DET" in child.text:
            for siblg in child.itersiblings():
                if siblg.attrib.get("type")=="string":
                    det.append(siblg.text)
#print(det)

#afficher les patrons DET-NOM

liste = []
for elt in root.iter("element"):
    for child in elt:
        data = tuple()
        if child.attrib.get("type") == "type" :
            typ = child.text
        if child.attrib.get("type") == "lemma" :
            lem = child.text
        if child.attrib.get("type") == "string" :
            strg=child.text
        
    data = (typ,lem,strg)
    liste.append(data)

print(liste) #('DET:ART', 'le', 'les')

for i,tupl in enumerate(liste):
    if "DET" in tupl[0] and liste[i+1][0]=="NOM":
        print(tupl[2]+" - "+liste[i+1][2]) #les - marchands
        
#reconstruire les phrases
liste_phrase = []
phrase_complete=[]
for tupl in liste:
    if  tupl[0] == "SENT":
        liste_phrase.append(tupl[2])
        concat_elt = "".join(liste_phrase)+"\n"
        phrase_complete.append(concat_elt)
        liste_phrase=[]
    else:
        liste_phrase.append(tupl[2]+" ")

print(phrase_complete)

#transformer l'affichage en : token/lemme/pos
for tupl in liste:
    print(f"{tupl[2]}/{tupl[1]}/{tupl[0]}\n")