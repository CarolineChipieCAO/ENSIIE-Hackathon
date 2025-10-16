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
Les encadrants sont là pour ça :) mais avant cela, jetez un oeil ...

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
Faites un petit tour [ici](https://pypi.org/project/yfinance/) pour la documentation yfinance. Un exemple simple d'utilisation d'yfinance : [get_stock.py](https://github.com/CarolineChipieCAO/ENSIIE-Hackathon/blob/main/get_stock.py)

### sur la récupération des messages Reddit
Le moyen le plus simple pour collecter des données Reddit est d’utiliser **l’API officielle** via la librairie **[PRAW](https://praw.readthedocs.io)**.

#### Étapes de configuration

1. Crée un compte sur [Reddit](https://www.reddit.com/).  
2. Rendez-vous sur la page des applications : [https://old.reddit.com/prefs/apps/](https://old.reddit.com/prefs/apps/)  
3. Clique sur **“create another app…”**, choisis le type **“script”**, et remplis les champs demandés.  
4. Une fois l’application créée, tu obtiendras deux identifiants :
   - `client_id`
   - `client_secret`

*(Voir capture d’écran ci-dessous pour repère visuel)*

![](https://github.com/CarolineChipieCAO/ENSIIE-Hackathon/blob/main/doc/reddit_api.png?raw=true)

Documentation Praw : [https://praw.readthedocs.io](https://praw.readthedocs.io)

Voir les exemples [reddit_search.py](https://github.com/CarolineChipieCAO/ENSIIE-Hackathon/blob/main/reddit_search.py), [reddit_stream_comment.py](https://github.com/CarolineChipieCAO/ENSIIE-Hackathon/blob/main/reddit_stream_comment.py) et [reddit_stream_submission.py](https://github.com/CarolineChipieCAO/ENSIIE-Hackathon/blob/main/reddit_stream_submission.py)


Pour se connecter remplace les valeurs : 
```
<your_client_id> : client_id
<your_client_secret> : client_secret
<your_password> : password du compte Reddit
<your_username> : username du compte Reddit
<your_user_agent> : "demo script"

```
### Exemples de subreddits à suivre
Subreddits financiers "sérieux" : 
[investing](https://www.reddit.com/r/investing/), [StockMarket](https://www.reddit.com/r/StockMarket/), [WallStreetbetsELITE](https://www.reddit.com/r/WallStreetbetsELITE/), [economy](https://www.reddit.com/r/economy/)

Subreddits trading/spéculation : 
[wallstreetbets](https://www.reddit.com/r/wallstreetbets/), [options](https://www.reddit.com/r/options/), [pennystocks](https://www.reddit.com/r/pennystocks/), [Daytrading](https://www.reddit.com/r/Daytrading/)

Subreddits spécialisés par secteur :
[AMD_Stock](https://www.reddit.com/r/AMD_Stock/), [NVDA_Stock](https://www.reddit.com/r/NVDA_Stock/), [Bitcoin](https://www.reddit.com/r/Bitcoin/), [CryptoCurrency](https://www.reddit.com/r/CryptoCurrency/)

### sur l'obtention un dataset 
Si vraiment vous faites face à un soucis d'extraction de données financier et sentiment, PAS DE PANIQUE ! Faites un tour sur ce [site](https://www.kaggle.com/code/yashvi/reliance-stock-prices-with-news-sentiment/notebook) pour récupérer un dataset
