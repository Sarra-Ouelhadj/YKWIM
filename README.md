![interface](https://user-images.githubusercontent.com/59183609/188460191-8a856f44-57c3-474d-b2d4-f7565755dbfd.png)
# YKWIM
Ce projet a pour objectif de permettre aux utilisateurs d'enrichir sémantiquement leurs données (obtenir des données RDF) via une *méthode* basée sur l'utilisation 
d'un *tableur* appelé ici [template](https://github.com/Sarra-Ouelhadj/YKWIM/blob/master/YKWIM/static/doc/template.ods) et son traitement automatique.

## Aperçu de la méthode

[Notice méthode d’enrichissement sémantique](https://github.com/Sarra-Ouelhadj/YKWIM/blob/master/YKWIM/static/doc/notice.pdf)

## Aperçu du traitement automatique

### Validations effectuées sur le template et les fonctionnalités qu'il offre aux utilisateurs 


#### Validations
| feuille | vérification |
|---|---|
|Classes|0. La feuille classe doit contenir au moins une classe|
||1. Chaque classe doit avoir un lien de référence ou une définition|
|Attributs|0. Le nom de la classe du 1er attribut est obligatoire|
||1. Tous les champs doivent être remplis. Le choix existe uniquement entre lien de référence et définition.|
||2. Chaque classe doit avoir au minimum un identifiant|
|Énumérations|0. Chaque énumération doit avoir un lien de référence ou une définition|
|Valeurs d’énumération|0. Le nom de l'énumération de la 1ère valeur est obligatoire|
||1. Chaque valeur d'énumération doit avoir un lien de référence ou une définition|
|Associations|0. Chaque association doit avoir un lien de référence ou une définition|

#### Fonctionnalités
|feuille|fonctionnalité|
|---|---|
|Attributs|Afficher la liste des classes à partir de la feuille « Classes » colonne « classe »|
||Si pour les autres attributs la colonne classe est vide : hériter la classe de la ligne précédente (attribut précédent)|
|Valeurs d’énumération|Afficher la liste des énumérations à partir de la feuille «Énumérations» colonne « énumération »|
||Si pour les autres valeurs d’énumération la colonne énumération est vide : hériter l’énumération de la ligne précédente (énumération précédente)|
|Associations|Afficher la liste des classes sources à partir de la feuille « Classes » colonne « classe »|
||Si pour les autres associations la colonne classe source est vide : hériter de la classe source précédente|
||Afficher la liste des classes et des énumérations destinations à partir de la feuille « Classes » colonne « classe » et de la feuille «Énumérations» colonne « énumération »|

## Lancement de la solution
### en local
```
$ git clone
$ cd SemanticLifting
$ python run.py
```
### sur Heroku
```
$ heroku run 
```
