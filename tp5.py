import sqlite3
import csv


def Create_Database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('CREATE TABLE region (CodeRegion int primary key, NomRegion text)')
    c.execute('CREATE TABLE department (CodeDepartment int primary key, NomDepartment text, CodeRegion int, foreign key(CodeRegion) references region(CodeRegion))')
    c.execute('CREATE TABLE commune (CodeCommune int, CodeDepartment int, NomCommune text, PopulationTotale int, primary key(CodeCommune,CodeDepartment),  foreign key(CodeDepartment) references department(CodeDepartment))')
    csv_reader = csv.reader(open('regions.csv','r',encoding='utf-8'))
    count = 0
    for row in csv_reader:
        count = count + 1
        if(count < 9):
            continue
        else:
            tmp = "".join(row)
            CodeRegion, NomRegion, t,t,t,t,t = tmp.split(";")
            c.execute('INSERT INTO region VALUES(?, ?)', [CodeRegion, NomRegion])
    csv_reader = csv.reader(open('departements.csv','r',encoding='utf-8'))
    count = 0
    for row in csv_reader:
        count = count + 1
        if(count < 9):
            continue
        else:
            tmp = "".join(row)
            CodeRegion, t, CodeDepartment, NomDepartment, t, t, t, t, t, t = tmp.split(";")
            if CodeRegion:
                c.execute('INSERT INTO department VALUES(?, ?, ?)', [CodeDepartment, NomDepartment, CodeRegion])
    csv_reader = csv.reader(open('communes.csv','r',encoding='utf-8'))
    count = 0
    for row in csv_reader:
        count = count + 1
        if(count < 9):
            continue
        else:
            tmp = "".join(row)
            t,t,CodeDepartment,t,t,CodeCommune,NomCommune,t,t,PopulationTotale,t = tmp.split(";")
            if CodeDepartment:
                c.execute('INSERT INTO commune VALUES(?, ? ,?, ?)', [CodeCommune, CodeDepartment, NomCommune, PopulationTotale])
    conn.commit()

def Calculer_Population():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    print('****  les populations totales de chaque département  ****')
    for row in c.execute('SELECT NomDepartment,SUM(PopulationTotale) FROM commune NATURAL JOIN department GROUP BY (CodeDepartment)'):
        print(row)
    print('****  les populations totales de chaque région  ****')
    for row in c.execute('SELECT NomRegion, SUM(PopulationTotale) FROM commune NATURAL JOIN department NATURAL JOIN region GROUP BY CodeRegion'):
        print(row)

def Determiner_Communes():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    temp=''
    ListDepartment=[]
    for row in c.execute('Select NomCommune, CodeDepartment from commune Order by NomCommune'):
        NomCommune = row[0]
        CodeDepartment = row[1]
        if NomCommune == temp:
            ListDepartment.append(CodeDepartment)
        else:
            if ListDepartment!=[]:
                for i in ListDepartment:
                    print('NomCommune: %s  Index: %s CodeDepartment: %s' %(temp, ListDepartment.index(i)+1, i))
            ListDepartment=[]
            ListDepartment.append(CodeDepartment)
            temp = NomCommune
    for i in ListDepartment:
        print('NomCommune: %s  Index: %s CodeDepartment: %s' %(temp, ListDepartment.index(i)+1, i))


import xml.etree.ElementTree as ET
def SauvegarderBddAXML():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    root = ET.Element('Data')
    for row in c.execute('SELECT CodeRegion, NomRegion FROM region'):
        Region = ET.SubElement(root, 'Region')
        CodeRegion = ET.SubElement(Region, 'CodeRegion')
        NomRegion = ET.SubElement(Region,'NomRegion')
        CodeRegion.text, NomRegion.text = str(row[0]), row[1]

    for row in c.execute('SELECT CodeDepartment, NomDepartment, CodeRegion FROM department'):
        Department = ET.SubElement(root, 'Departement')
        CodeDepartment = ET.SubElement(Department, 'CodeDepartment')
        NomDepartment = ET.SubElement(Department, 'NomDepartment')
        CodeRegion = ET.SubElement(Department, 'CodeRegion')
        CodeDepartment.text, NomDepartment.text, CodeRegion.text = str(row[0]), row[1], str(row[2])

    for row in c.execute('SELECT CodeCommune, CodeDepartment, NomCommune, PopulationTotale FROM commune'):
        Commune = ET.SubElement(root, 'Commune')
        CodeCommune = ET.SubElement(Commune, 'CodeCommune')
        CodeDepartment = ET.SubElement(Commune, 'CodeDepartment')
        NomCommune = ET.SubElement(Commune, 'NomCommune')
        PopulationTotale = ET.SubElement(Commune, 'PopulationTotale')
        CodeCommune.text, CodeDepartment.text, NomCommune.text, PopulationTotale.text = str(row[0]), str(row[1]), row[2], str(row[3])

    tree = ET.ElementTree(root)
    tree.write('result.xml', encoding='utf-8')

def ChargerXML():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    tree = ET.parse('result.xml')
    root = tree.getroot()
    for child in root:
        if child.tag == 'Region':
            for subChild in child:
                if subChild.tag == 'CodeRegion':
                    CodeRegion = subChild.text
                elif subChild.tag == 'NomRegion':
                    NomRegion = subChild.text
            c.execute('INSERT INTO region VALUES(?, ?)', [CodeRegion, NomRegion])
        elif child.tag == 'Department':
            for subChild in child:
                if subChild.tag == 'CodeDepartment':
                    CodeDepartment = subChild.text
                elif subChild.tag == 'NomDepartment':
                    NomDepartment = subChild.text
                elif subChild.tag == 'CodeRegion':
                    CodeRegion = subChild.text
            c.execute('INSERT INTO department VALUES(?, ?, ?)', [CodeDepartment, NomDepartment, CodeRegion])
        elif child.tag == 'Commune':
            for subChild in child:
                if subChild.tag == 'CodeCommune':
                    CodeCommune = subChild.text
                elif subChild.tag == 'CodeDepartment':
                    CodeDepartment = subChild.text
                elif subChild.tag == 'NomCommune':
                    NomCommune = subChild.text
                elif subChild.tag == 'PopulationTotale':
                    PopulationTotale = subChild.text
            c.execute('INSERT INTO commune VALUES(?, ? ,?, ?)', [CodeCommune, CodeDepartment, NomCommune, PopulationTotale])
    conn.commit()

def AjouterNouvelle():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    c.execute('CREATE TABLE nouvellesregions (CodeRegion int primary key, NomRegion text)')
    csv_reader = csv.reader(open('zones-2016.csv','r',encoding='utf-8'))
    count = 0
    for row in csv_reader:
        count = count + 1
        if(count < 4550):
            continue
        else:
            tmp = "".join(row)
            t, CodeRegion, NomRegion, t = tmp.split(";")
            c.execute('INSERT INTO nouvellesregions VALUES(?, ?)', [CodeRegion, NomRegion])
    conn.commit()

    c.execute('ALTER TABLE department ADD CodeNouvelleRegion text')
    conn.commit()

    csv_reader = csv.reader(open('communes-2016.csv','r',encoding='utf-8'))
    count = 0
    temp_CodeDepartment = '0'
    for row in csv_reader:
        count = count + 1
        if(count < 7):
            continue
        else:
            tmp = "".join(row)
            t, t, CodeDepartment, CodeNouvelleRegion, t, t, t, t= tmp.split(";")
            if(temp_CodeDepartment == CodeDepartment):
                continue
            else:
                c.execute('UPDATE department SET CodeNouvelleRegion = ? WHERE CodeDepartment = ?', [CodeNouvelleRegion, CodeDepartment])
                temp_CodeDepartment == CodeDepartment
    conn.commit()

def Calculer_Nouvelle():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    print('****  les populations totales de chaque région  ****')
    for row in c.execute('SELECT n.CodeRegion, n.NomRegion, SUM(c.PopulationTotale) FROM commune c ,department d, nouvellesregions n WHERE c.CodeDepartment=d.CodeDepartment AND d.CodeNouvelleRegion=n.CodeRegion GROUP BY n.CodeRegion'):
        print(row)

if __name__=='__main__':
    #Create_Database()
    #Calculer_Population()
    Determiner_Communes()
    #SauvegarderBddAXML()
    #ChargerXML()
    #AjouterNouvelle()
    #Calculer_Nouvelle()
