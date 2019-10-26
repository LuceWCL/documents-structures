import csv
from lxml import etree

with open("tournagesdefilmsparis2011.csv","r",encoding="utf-8") as csvfile, open("test_tournage.xml","wb") as xmlfile:
    tournage = csv.reader(csvfile, delimiter=";")

    next(tournage)

    root = etree.Element("Shootings")
    for i, row in enumerate(tournage, start=1):
        Film = etree.SubElement(root,"Film")
        Film.set("n",str(i))

        Title = etree.SubElement(Film,"Title")
        Title.text = row[0]

        Director = etree.SubElement(Film, "Director")
        Director.text = row[1]

        Lieu = etree.SubElement(Film, "Lieu")
        Adress = etree.SubElement(Lieu,"Adress")
        Adress.text = row[2]
        Arrondissement = etree.SubElement(Lieu,"Arrondissement")
        Arrondissement.text = row[5]
        Coordinates = etree.SubElement(Lieu,"Coordinates")
        Coordinates.text = row[8]

        Producer_company = etree.SubElement(Film,"Producer_company")
        Producer_company.text = row[3]

        Type = etree.SubElement(Film,"Type")
        Type.text = row[4]

        Date = etree.SubElement(Film,"Date")
        Beggining = etree.SubElement(Date,"Beggining")
        Beggining.text = row[6]
        End = etree.SubElement(Date,"End")
        End.text = row[7]

    tree = etree.ElementTree(root)

    tree.write(xmlfile, encoding="utf-8",xml_declaration=True, method="xml",pretty_print=True)
