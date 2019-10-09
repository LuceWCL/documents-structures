import csv

with open('tournagesdefilmsparis2011.csv','r') as csvfile, open('tournage.xml','w') as xmlfile:
    readCSV = csv.reader(csvfile, delimiter=";")

    data=[]
    for row in readCSV:
        data.append(row)
    print(data)

    def convert_row(row):
        return """
<Shootings>
    <Film>
        <Title>%s</Title>
        <Director>%s</Director>
        <Lieu>
            <Adress>%s</Adress>
            <Arrondissement>%s</Arrondissement>
            <Coordinates>%s</Coordinates>
        </Lieu>
        <Producer_company>%s</Producer_company>
        <Type>%s</Type>
        <Date>
            <Beggining>%s</Beggining>
            <End>%s</End>
        </Date>
    </Film>
</Shootings>"""%(row[0], row[1], row[2], row[5], row[8], row[3], row[4],row[6],row[7])
    xmlfile.write('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE Shootings SYSTEM "gram_tournage.dtd">')
    xmlfile.write(''.join([convert_row(row) for row in data[1:]]))
