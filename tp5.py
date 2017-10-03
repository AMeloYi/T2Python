import sqlite3
import csv

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
        c.execute('INSERT INTO commune VALUES(?, ? ,?, ?)', [CodeCommune, CodeDepartment, NomCommune, PopulationTotale])

conn.commit()
