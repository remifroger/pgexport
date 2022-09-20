#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from dotenv import load_dotenv
load_dotenv()

PGHOST = os.getenv('PGHOST')
PGPORT = os.getenv('PGPORT')
PGUSER = os.getenv('PGUSER')
PGPWD = os.getenv('PGPWD')
PGDB = os.getenv('PGDB')
QGISBINPATH = os.getenv('QGISBINPATH')

if PGHOST == "" or PGPORT == "" or PGUSER == "" or PGPWD == "" or PGDB == "" or QGISBINPATH == "":
    print('Renseignez les variables d\'environnement du fichier .env')
    exit()

if not os.path.exists(QGISBINPATH):
    print('Le chemin vers les binaires QGIS n\'existe pas (exemple : C:\Program Files\QGIS X.XX\bin)')
    exit()

outputDir  = sys.argv[1]
with open('export.txt') as f:
    conf = f.read().splitlines() 

os.chdir(QGISBINPATH)
for el in conf:
    schema, separator, table = el.partition('.')
    try:
        print('Export en CSV de {0}, schéma : {1}'.format(table.replace('"', ''), schema))
        subprocess.check_call(['ogr2ogr', '-f', 'CSV', os.path.join(outputDir, "{0}.csv".format(table.replace('"', ''))), "PG:host={0} port={1} dbname={2} user={3} password={4}".format(PGHOST, PGPORT, PGDB, PGUSER, PGPWD), el])
        print('Exporté')
    except subprocess.CalledProcessError as e:
        print(e.output)
    try:
        print('Export en SHP de {0}, schéma : {1}'.format(table.replace('"', ''), schema))
        subprocess.check_call(['ogr2ogr', '-f', 'ESRI Shapefile', os.path.join(outputDir, "{0}.shp".format(table.replace('"', ''))), "PG:host={0} port={1} dbname={2} user={3} password={4}".format(PGHOST, PGPORT, PGDB, PGUSER, PGPWD), el])
        print('Exporté')
    except subprocess.CalledProcessError as e:
        print(e.output)

print('Terminé')