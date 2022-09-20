# pgexport

Versions : testé sur Python 2.7.X et Python 3.10.X

Exporte dans un dossier des tables en provenance de PostgreSQL.

Nécessite l'installation de QGIS (ogr2ogr).

## Pré-requis

Remplir les variables d'environnement (.env) et le fichier export.txt, avec une ligne par table que vous souhaitez exporter (selon le format schema.table ou schema."table 1").

## Usage

```
python main.py "path\to\dir"
```

Par exemple, la commande ci-dessous va exporter l'ensemble des tables PostgreSQL du fichier export.txt dans le dossier tests (C:\Users\frog\OneDrive - Projet\data\tests).

```
python main.py "C:\Users\frog\OneDrive - Projet\data\tests"
```

Attention, bien veiller à mettre le chemin du dossier entre guillemets.