# ENSIIE-Hackathon
Sujet : Dashboard de corrélation entre sentiment et mouvement de marché

## Objectif
Ce projet vise à construire un dashboard qui analyse la corrélation entre le **sentiment public** et les **mouvements de marché** pour une liste prédéfinie d'**actions** (du CAC40 ou NASDAQ) sur une période.

Vous explorerez comment le sentiment extrait de commentaires & publications sur réseaux sociaux & articles de presse ou bien commentaires financiers peut être lié aux flustuation de prix, et si des cheémas ou signaux prédictifs peuvent être identifiés. 

En effet, les prix de marché sont influencés non seulement par les fondamentaux financiers, mais aussi par la perception publique et le sentiment des investisseurs. En analysant des données textuelles issues de plateformes comme Reddit ou bien des sites d'actualités financières, on peut tenter de détecter des tendances de sentiment et les comparer aux mouvements réels de marché. 

## Ce que vous allez construire
Vous pouvez choisir de prioriser un des 2 axes principaux :
### 1. Récupération et selection des données 
- Selection des sources pertinentes et des actions à suivre
- Collecte de données via scraping, API ou wrappers existants
- Normalisation des formats et nettoyage des données
- Identifier les sentiments dans les commentaires ou titres de presse ou autres articles

### 2. Design et implémentation du dashboard
- Conception d'une interface claire (et intéractive ?)
- Choix des visualisations pertinentes (courbes, heatmaps, etc...)
- Prise en compte de l'expérience utilisateur

## Critère du jury
L'avis du jury sera basé sur les 2 axes décrits ci-dessus. 


# Besoin d'aide ?
Les encadrants sont là pour ça :) 

### sur l'analyse de sentiment (facile)
- avec [Vader](https://www.geeksforgeeks.org/python/python-sentiment-analysis-using-vader/)
- avec textblob
```python
from textblob import TextBlob
text = "Apple stock surged after strong earnings and optimistic guidance for the next quarter."
blob = TextBlob(text)
print(blob.sentiment)
```
- vous pouvez également vous renseigner sur les modèles Huggingface (finBERT, etc)

### sur la récupération de prix de marché
Faites un petit tour [ici]() pour yfinance

### sur un dataset 
Si vraiment vous faites face à un soucis d'extraction de données financier et sentiment, PAS DE PANIQUE ! Faites un tour sur ce [site](https://www.kaggle.com/code/yashvi/reliance-stock-prices-with-news-sentiment/notebook) pour récupérer un dataset
