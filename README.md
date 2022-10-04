![interface](https://user-images.githubusercontent.com/59183609/188460191-8a856f44-57c3-474d-b2d4-f7565755dbfd.png)
# YKWIM
Ce projet a pour objectif de permettre aux utilisateurs d'enrichir sémantiquement leurs données (obtenir des données RDF) via une *méthode* basée sur l'utilisation 
d'un *tableur* appelé ici [template](https://github.com/Sarra-Ouelhadj/YKWIM/blob/master/YKWIM/static/doc/template.xlsx) et son traitement automatique.

## 1. Aperçu général de la méthode
![Méthode](https://user-images.githubusercontent.com/59183609/188460869-e497f42c-b209-4e50-a0c2-1c08723a89b9.png)

### 1.1 Utilisation du template (actions manuelles)
👉️ Voir [notice](https://github.com/Sarra-Ouelhadj/YKWIM/blob/master/YKWIM/static/doc/notice.pdf) méthode d’enrichissement sémantique

### 1.2 Traitement automatique (actions automatisées)
![auto](https://user-images.githubusercontent.com/59183609/188470029-ffa676ef-3781-424f-b3cd-370636633b4b.png)


#### 1.2.1 Validations effectuées sur le template et les fonctionnalités qu'il offre aux utilisateurs 


##### a. Validations
| feuille | vérification |
|---|---|
|Classes|0. La feuille classe doit contenir au moins une classe|
||1. Chaque classe doit avoir un lien de référence ou une définition|
|Attributs|0. Le nom de la classe du 1er attribut est obligatoire|
||1. Tous les champs doivent être remplis. Le choix existe uniquement entre lien de référence et définition|
||2. Chaque classe doit avoir au minimum un identifiant|
||3. Pas d'attributs avec le même nom dans le modèle UML|
|Énumérations|0. Chaque énumération doit avoir un lien de référence ou une définition|
||1. La source de chaque énumération est obligatoire|
|Valeurs d’énumération|0. Le nom de l'énumération de la 1ère valeur est obligatoire|
||1. Chaque valeur d'énumération doit avoir un lien de référence ou une définition|
|Associations|0. Chaque association doit avoir un lien de référence ou une définition|

##### b. Fonctionnalités
|feuille|fonctionnalité|
|---|---|
|Attributs|Afficher la liste des classes à partir de la feuille « Classes » colonne « classe »|
||Si pour les autres attributs la colonne classe est vide : hériter la classe de la ligne précédente (attribut précédent)|
|Valeurs d’énumération|Afficher la liste des énumérations à partir de la feuille «Énumérations» colonne « énumération »|
||Si pour les autres valeurs d’énumération la colonne énumération est vide : hériter l’énumération de la ligne précédente (énumération précédente)|
|Associations|Afficher la liste des classes sources à partir de la feuille « Classes » colonne « classe »|
||Si pour les autres associations la colonne classe source est vide : hériter de la classe source précédente|
||Afficher la liste des classes et des énumérations destinations à partir de la feuille « Classes » colonne « classe » et de la feuille «Énumérations» colonne « énumération »|

## 2. Lancement de la solution
### Prérequis (pour le local)
* Avoir python 3.8.10 installé
* Avoir pip 20.0.2 installé
* Avoir java 11.0.16

### en local
```
$ git clone https://github.com/Sarra-Ouelhadj/YKWIM.git
```

------
[optionnel] : pour installer les libraries dans un environnement virtuel au lieu du système
```
$ virtualenv env -p /usr/bin/python3
$ source env/bin/activate
```
------
```
$ cd YKWIM
$ pip install -r requirements.txt
$ python run.py
```
lancement de la solution en local sur http://127.0.0.1:5000/
- Télécharger [template de test](https://github.com/Sarra-Ouelhadj/YKWIM/blob/master/YKWIM/tests/template_test.ods) déjà rempli
- (mettre n'importe quel URL dans le champs URL du jeu de données pour l'instant) (en cours de développement)

### sur Heroku (en construction)

link : [https://semantic-lifting-method.herokuapp.com/](https://semantic-lifting-method.herokuapp.com/)

