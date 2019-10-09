import csv
import xml.etree.ElementTree as ET

with open('tournagesdefilmsparis2011.csv','r') as csvfile, open('test_tournage.xml','w') as xmlfile:
    readCSV = csv.reader(csvfile, delimiter=";")

    data=[]
    for row in readCSV:
        data.append(row)
    #print(data)
    n=0

    root = ET.Element('Shootings')
    title = ET.SubElement(root,'Title',Status=f'{n}')
    ET.SubElement(title, 'Director')
    ET.SubElement(title, 'Lieu')
    lieu = ET.SubElement(title, 'Adress')
    ET.SubElement(lieu, 'Arrondissement')
    ET.SubElement(lieu, 'Coordinates')
    ET.SubElement(title, 'Producer_company')
    ET.SubElement(title, 'Type')
    date = ET.SubElement(title,'Date')
    ET.SubElement(date,'Beggining')
    ET.SubElement(date,'End')

    xmlfile.write(ET.tostring(root).decode())
