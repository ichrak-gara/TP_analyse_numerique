# <span style="color:	#394CDF ">Projet:  Analyse Numérique </span>


# - <span style="color:	#C728A3 ">Réalisé par: </span>



## <center><img align="left" width="100" height="100" src="ichrak.jpg"/> <span style="color:#1C1C1E ">Ichrak Gara & Bacem Abroug </span><img align="right" width="100" height="100" src="bacem.jpg"/></center>

_________________________________
________________________________
____________________________






# - <span style="color:	#C728A3 ">Classe:  </span>
## <center><span style="color:	#1C1C1E ">2DNI_G2 </span></center>



# <span style="color:	olivedrab ">I. Objectif: </span>

Notre objectif principal du projet est de développer et d'implémenter une **`interface graphique`** à utiliser pour **`interpoler`** une fonction sous la forme d'une courbe tout en **`intégrant`** simultanément une intégrale assez complexe dans une forme polynomiale.

# <span style="color:	olivedrab ">II. Introduction Générale de l'analyse Numérique: </span>

L'analyse numérique, c'est une **`branche des mathématiques`**, des mathématiques appliquées, dont le but est de :
- mettre au point et d'étudier des méthodes de résolution numérique.
- calculer véritablement des nombres qui vont représenter des phénomènes physiques

Pour **`résoudre numériquement des équations`** qui sont issues de problèmes posés par la physique ou par les sciences appliquées.

L’analyse numérique a commencé bien avant la conception des ordinateurs et leur utilisation quotidienne que nous connaissons aujourd’hui.

Les premières méthodes ont été développées pour essayer de trouver des **`moyens rapides`** et **`efficaces`** de s’attaquer à des problèmes soit **`fastidieux`** à résoudre à cause de leur **`grande dimension`** (systèmes à plusieurs dizaines d’équations par exemple), soit parce qu’il n’existe pas solutions explicites connues même pour certaines équations assez simples en apparence.

# <span style="color:	olivedrab ">III. Motivation: </span>

- Recherche et développement : études expérimentales coûteuses
- Les modèles considérés sont composés d’ensemble d’équations dont on ne sait pas déterminer de solutions explicites
- Proposer une solution approchée, calculée à l’aide de l’ordinateur.

En analyse numérique on s’intéresse sur la mise en pratique des méthodes permettant de résoudre, par des calculs purement numériques, des problèmes d’analyse mathématique. c'est pour cela nous nous intéressons dans notre projet sur 
l'interpolation polynomiale et l'intégration numérique qui résoudront le problème de calcule.


# <span style="color:	olivedrab ">IV. Interpolation: </span>

En analyse numérique, l'interpolation est une opération mathématique permettant de remplacer une courbe ou une fonction par une autre courbe (ou fonction) plus simple, mais qui coïncide avec la première en un nombre fini de points (ou de valeurs) donnés au départ.

<div class="alert alert-success">
=> elle désigne la construction d’une courbe à partir de la donnée d’un nombre fini de points.
</div>

il existe différents types de l'interpolation:

- Interpolation linéaire.
- Interpolation cosinus. 
- Interpolation polynomiale.
- Interpolation polynomiale par parties.

## <span style="color:	#AF3B8A ">1. Interpolation polynomiale: </span>

Une interpolation polynomiale consiste à utiliser un polynôme unique, de degré aussi grand que nécessaire, pour estimer localement l'équation représentant la courbe afin de déterminer la valeur entre les échantillons.

## <span style="color:	#AF3B8A ">2. Principe: </span>

Pour représenter une fonction en informatique, on prend en général « un certain nombre » de points et l'on fait une interpolation polynomiale, ce qui évite de calculer trop de points. Se pose alors la question du choix des points.

Dans un premier temps, on peut prendre des points régulièrement répartis dans l'intervalle. Cependant, cela peut donner des « effets de bord » (le polynôme représente bien au milieu de l'intervalle, mais a un comportement différent aux bords bien que passant par les points), et pose problème dans les endroits où les variations de pente sont importantes.

Pour éviter les effets de bord, on utilise des points répartis selon une fonction sinusoïdale.
<p align="center">
  <img  src="images/1.png"/>
</p>


<div class="alert alert-warning">
Pour chaque intervalle, on calcule la différence entre le polynôme et la fonction au point médian, et si cet écart est supérieur à un seuil de tolérance, on rajoute un point au milieu de l'intervalle.
</div>

Les différents interpolations qu'on peut utiliser pour interpoler I sont :
- **`Interpolation de Lagrange`**
- **`Interpolation de Newton`**

# <span style="color:	olivedrab ">V. Intégration: </span>

En mathématique, l'intégration est une opération consistant à calculer l'intégrale d'une fonction d'une ou plusieurs variables.


## <span style="color:	#AF3B8A ">1. Intégration Numérique: </span>

Dans certains cas très limités, une telle **`intégrale`** peut être calculée analytiquement (à la main). Cependant, ce n’est que très rarement possible, et le plus souvent un des cas suivants se présente :
- Le calcul analytique est long, compliqué et rébarbatif
- Le résultat de l’intégrale est une fonction compliquée qui fait appel à d’autres fonctions elles-même longues à évaluer
- Cette intégrale n’a pas d’expression analytique
Dans tous ces cas, on préfèrera calculer **`numériquement la valeur de l’intégrale I`**.

## <span style="color:	#AF3B8A ">2. Principe: </span>

L’idée principale est de trouver des méthodes qui permettent de calculer rapidement une valeur approchée I de l’intégrale à calculer tel que:
<p align="center">
  <img  src="images/2.PNG"/>
</p>

Les méthode qu'on va utiliser pour calculer l'intergrale I sont :
- **`Méthode des réctangles`**
<p align="center">
  <img  src="images/rect6.gif"/>
</p>

- **`Méthode du point milieu`**
<p align="center">
  <img  src="images/Trapezium2.gif"/>
</p>

- **`Méthode des trapézes`**
<p align="center">
  <img  src="images/trap%C3%A9ze.png"/>
</p>

- **`Méthodes de Simpson`**
<p align="center">
  <img  src="images/ps205_982234Simpson.gif"/>
</p>


# <span style="color:	olivedrab ">VI. Environnement de travail: </span>

En fait **`L'interface utilisateur graphique (GUI)`** est une forme d'interface utilisateur qui permet aux utilisateurs d'interagir avec les ordinateurs via des indicateurs visuels utilisant des éléments tels que des icônes, des menus, des fenêtres, etc.

Le langage de programmation que nous avons utilisé dans notre projet: c'est le langage **`Python`** en utilisant le module **`Tkinter`**
<p align="center">
  <img  src="images/4.PNG"/>
</p>



#### Qu'est-ce que Tkinter?
<p align="center">
  <img  src="images/6.PNG"/>
</p>



**`Tkinter`** est le module python intégré utilisé pour créer des applications GUI. C'est l'un des modules les plus couramment utilisés pour créer des applications GUI en Python car il est **`simple`** et **`facile`** à utiliser.

Pour créer une application tkinter:

- Importer le module - tkinter
- Créer la fenêtre principale (conteneur)
- Ajoutez n'importe quel nombre de widgets à la fenêtre principale
- Appliquez l'événement Trigger sur les widgets.

# <span style="color:	olivedrab ">VII. Réalisation et Validation: </span>

Dans cette partie, nous allons présenter les différentes interfaces de notre projet qui se compose de 3 interfaces graphiques:
- **`Interface générale pour la sélection de l'utilisateur`**
- **`Interface pour implémenter des interpolations polynomiales`**
- **`Interface pour implémenter l'intégration numérique`**

## <span style="color:	#AF3B8A ">1. Interface 1: </span>
<p align="center">
  <img  src="images/interface1.PNG"/>
</p>


<div class="alert alert-success">
    
Cette interface contient 3 boutons:
    
- **`Bouton "Interpolation polynomiale"`**: Ce bouton affiche une nouvelle interface qui interpole les points dans une 
    
    courbe et montre également le polynôme Pn (X).
    
    
- **`Bouton "Intégration numérique"`**: Ce bouton affiche une autre interface qui intègre une fonction en spécifiant divers paramètres à suivre.
    
    
- **`Bouton "Quitter"`**: qui permet de fermer toutes les interfaces.
</div>

## <span style="color:	#AF3B8A ">2. Interface 2: </span>
<p align="center">
  <img  src="images/interface-2.PNG"/>
</p>

<p align="center">
  <img  src="images/integrale_I.jfif"/>
</p>



<div class="alert alert-success">
    
- Cette interface comprend principalement **`deux zones de texte`**. Nous pouvons saisir les valeurs x et y que nous interpolerons sous la forme d'un **`polynôme Pn (x)`** et une courbe pour ce polynôme en utilisant le bouton **`"finish & plot"`**. 
    
    
- Sinon, nous construisons les points x et y directement sur la courbe et on affiche le polynôme directement.
    
    
 
- Ce polynôme est également affiché en bas de la fenêtre (encadré en rouge dans la figure ci-dessus) ou le cas où 
    l'utilisateur veut copier le polynôme...
    
    
- Nous pouvons également afficher la valeur de l'intégrale de cette fonction en utilisant le bouton **`"Integrate this function"`** , qui **`affiche la valeur intégrale`** sous forme de petite fenêtre comme illustré dans la figure 2 ci-
    dessus avec une représentation graphique de la courbe intégrer avec la méthode des trapézes.
    

    
- Et le dernier bouton est **`"Clear all"`** qui **`efface`** tous les paramètres et peut reconstituer pour une autre 
    fonction.
</div>


## <span style="color:	#AF3B8A ">3. Interface 3: </span>
<p align="center">
  <img  src="images/interface3-1.jfif"/>
</p>

<p align="center">
  <img  src="images/interface3-2.jfif"/>
</p>


<div class="alert alert-success">
     
- Cette interface permet **`l'intégration d'une fonction f`** spécifique en spécifiant des paramètres tels que 
    **`l'intervalle [a, b]`** de la fonction, **`la méthode d'intégration`** (méthode des trapéses, méthode Simpson,
    méthode rectangle ou méthode point milieu) et **`la valeurs N`** (nombre des points ou les échantillons)
    
    
- Cette intégration apparaît sous forme de **`représentation graphique`** à l'aide du bouton **`"plot & integrate function"`** 
</div>


# <span style="color:	#AF3B8A ">Simulation: </span>

#### Nous avons simulé notre travail sous forme de GIF ci-dessous pour mieux comprendre le flux des boutons et l'affichage des courbes.

## <span style="color:	#3374D5 ">Simulation pour l'interface d'interpolation: </span>
<p align="center">
  <img  src="images/simulation_gif1.gif"/>
</p>


## <span style="color:	#3374D5 ">Simulation pour l'interface d'intégration: </span>
<p align="center">
  <img  src="images/simulation_gif2.gif"/>
</p>

