---
title: "Pandas pour l'Analyse de Données"
description: "Maîtrisez la bibliothèque pandas pour l'analyse de données professionnelle avec DataFrames, opérations et transformations"
difficulty: "Advanced"
duration: "2 hours"
tags: [python, pandas, data-analysis, data-science, dataframes]
learning_objectives:
  - "Comprendre les DataFrames pandas et comment les créer"
  - "Charger et explorer les données à partir de fichiers CSV et d'autres sources"
  - "Effectuer des opérations de nettoyage et de transformation de données"
  - "Appliquer le groupage, le filtrage et les techniques d'agrégation"
  - "Exporter les données traitées dans divers formats"
prerequisites: [lesson-001-variables]
created: 2026-01-30
author: "LLM Assistant"
status: "published"
lang: fr
---

# Pandas pour l'Analyse de Données

**Difficulté**: 🔴 Avancé | **Durée**: 2 heures

**Tags**: [`python`](../../guides/tags-reference-fr.md#python) · [`pandas`](../../guides/tags-reference-fr.md#pandas) · [`data-analysis`](../../guides/tags-reference-fr.md#data-analysis) · [`data-science`](../../guides/tags-reference-fr.md#data-science) · [`dataframes`](../../guides/tags-reference-fr.md#dataframes)

---

## Objectifs d'Apprentissage

À la fin de cette leçon, vous serez capable de :
- Comprendre les DataFrames pandas et comment les créer
- Charger et explorer les données à partir de fichiers CSV et d'autres sources
- Effectuer des opérations de nettoyage et de transformation de données
- Appliquer le groupage, le filtrage et les techniques d'agrégation
- Exporter les données traitées dans divers formats

## Introduction

**Pandas** est la bibliothèque Python la plus populaire pour l'analyse de données. Elle fournit des outils puissants pour :

- **Charger les données** à partir de fichiers CSV, Excel, bases de données SQL, et plus
- **Explorer les données** rapidement avec des statistiques descriptives
- **Nettoyer les données** en traitant les valeurs manquantes et les transformations
- **Analyser les données** avec groupage, filtrage et agrégations
- **Visualiser les données** avec des capacités de traçage intégrées
- **Exporter les résultats** dans plusieurs formats

Si vous travaillez avec des données en Python, vous utiliserez extensively pandas.

## Qu'est-ce qu'un DataFrame ?

Un **DataFrame** est un tableau 2D avec des lignes et des colonnes—similaire à une feuille de calcul Excel ou une table de base de données.

```
   Name    Age  Salary
0  Alice    28   55000
1    Bob    34   62000
2  Carol    29   58000
```

Chaque colonne est une **Series** (données 1D), et leur combinaison crée un **DataFrame** (données 2D).

## Créer des DataFrames

### À partir d'un Dictionnaire
```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [28, 34, 29],
    'Salary': [55000, 62000, 58000]
}

df = pd.DataFrame(data)
print(df)
```

### À partir d'une Liste de Listes
```python
data = [
    ['Alice', 28, 55000],
    ['Bob', 34, 62000],
    ['Carol', 29, 58000]
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'Salary'])
print(df)
```

### À partir d'un Fichier CSV
```python
df = pd.read_csv('data.csv')
print(df.head())  # Afficher les 5 premières lignes
```

## Explorer les Données

Une fois que vous avez un DataFrame, explorez-le :

```python
# Afficher les premières lignes
df.head()

# Afficher les dernières lignes
df.tail()

# Statistiques de base
df.describe()

# Types de données
df.dtypes

# Forme (lignes, colonnes)
df.shape

# Noms des colonnes
df.columns

# Obtenir des informations résumées
df.info()
```

### Exemple
```python
df.head(3)
# Output:
#      Name  Age  Salary
# 0   Alice   28   55000
# 1     Bob   34   62000
# 2   Carol   29   58000

df.describe()
# Output:
#         Age       Salary
# count    3.0    3.000000
# mean    30.3    58333.333333
# std      3.2    3513.641016
# min     28.0    55000.000000
# 25%     28.5    56500.000000
# 50%     29.0    58000.000000
# 75%     31.5    60000.000000
# max     34.0    62000.000000
```

## Accéder aux Données

### Par Nom de Colonne
```python
df['Name']        # Retourner Series
df[['Name', 'Age']]  # Retourner DataFrame avec 2 colonnes
```

### Par Index de Ligne
```python
df.loc[0]         # Accéder par étiquette
df.iloc[0]        # Accéder par position
```

### Par Condition
```python
df[df['Age'] > 30]      # Lignes où Age > 30
df[df['Salary'] > 58000]  # Lignes où Salary > 58000

# Conditions multiples
df[(df['Age'] > 28) & (df['Salary'] > 55000)]
```

## Nettoyage des Données

### Traiter les Valeurs Manquantes
```python
# Vérifier les valeurs manquantes
df.isnull()
df.isnull().sum()

# Supprimer les lignes avec des valeurs manquantes
df.dropna()

# Remplir les valeurs manquantes
df.fillna(0)
df.fillna(df.mean())  # Remplir avec la moyenne de la colonne
```

### Supprimer les Doublons
```python
# Vérifier les doublons
df.duplicated()

# Supprimer les doublons
df.drop_duplicates()
```

### Renommer les Colonnes
```python
df.rename(columns={'Age': 'Years_Old'})
df.columns = ['Name', 'Years_Old', 'Salary']
```

## Transformation des Données

### Ajouter de Nouvelles Colonnes
```python
# Créer une nouvelle colonne à partir du calcul
df['Years_to_Retirement'] = 65 - df['Age']

# Créer une nouvelle colonne à partir d'une condition
df['High_Earner'] = df['Salary'] > 60000
```

### Tri
```python
# Trier par une colonne
df.sort_values('Salary')

# Trier par plusieurs colonnes
df.sort_values(['Age', 'Salary'])

# Trier décroissant
df.sort_values('Salary', ascending=False)
```

### Groupage et Agrégation
```python
# Grouper et calculer la moyenne
df.groupby('Department')['Salary'].mean()

# Agrégations multiples
df.groupby('Department').agg({
    'Salary': 'mean',
    'Age': 'min',
    'Name': 'count'
})
```

## Exercices

### Exercice 1 : Créer et Explorer un DataFrame

**Tâche** : Créez un DataFrame avec les données des étudiants :
- Noms : Alice, Bob, Carol, David
- Scores Mathématiques : 85, 92, 78, 88
- Scores Anglais : 88, 85, 90, 79

Ensuite :
1. Afficher les 2 premières lignes
2. Obtenir des statistiques résumées
3. Trouver les étudiants avec Mathématiques > 85

**Exemple de Solution** :
```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Carol', 'David'],
    'Math': [85, 92, 78, 88],
    'English': [88, 85, 90, 79]
}

df = pd.DataFrame(data)

print(df.head(2))
print(df.describe())
print(df[df['Math'] > 85])
```

### Exercice 2 : Transformation des Données

**Tâche** : Utilisant le DataFrame des étudiants ci-dessus :
1. Créez une nouvelle colonne 'Average' avec la moyenne des scores Mathématiques et Anglais
2. Créez une colonne 'Passing' (Vrai si Average >= 80)
3. Triez par Average en ordre décroissant

**Exemple de Solution** :
```python
df['Average'] = (df['Math'] + df['English']) / 2
df['Passing'] = df['Average'] >= 80

df_sorted = df.sort_values('Average', ascending=False)
print(df_sorted)
```

### Défi : Analyse des Données de Ventes

**Tâche** : Étant donné des données de ventes, effectuer une analyse :
1. Charger ou créer un DataFrame avec les données de ventes
2. Calculer les ventes totales par produit
3. Trouver le produit avec les ventes moyennes les plus élevées
4. Créer une nouvelle colonne pour la performance des ventes

**Exemple de Solution** :
```python
sales_data = {
    'Product': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Sales': [100, 150, 200, 180, 120, 140],
    'Month': [1, 2, 1, 2, 1, 2]
}

df = pd.DataFrame(sales_data)

# Total par produit
print(df.groupby('Product')['Sales'].sum())

# Moyenne par produit
avg_by_product = df.groupby('Product')['Sales'].mean()
print(f"Highest: {avg_by_product.idxmax()} with ${avg_by_product.max():.2f}")

# Performance (au-dessus/en dessous de la moyenne globale)
avg_overall = df['Sales'].mean()
df['Performance'] = df['Sales'] > avg_overall
```

## Évaluation

### Questions d'Autoévaluation

1. **Qu'est-ce qu'un DataFrame dans pandas ?**
   - Un DataFrame est un tableau 2D avec des lignes et des colonnes, similaire à une feuille de calcul ou une table de base de données.

2. **Comment charger les données d'un fichier CSV dans un DataFrame ?**
   - Utilisez `df = pd.read_csv('filename.csv')`

3. **Comment sélectionnez-vous les lignes où Age > 30 ?**
   - Utilisez `df[df['Age'] > 30]` pour filtrer le DataFrame.

4. **Quelle est la différence entre `.loc[]` et `.iloc[]` ?**
   - `.loc[]` accède par étiquette/nom d'index. `.iloc[]` accède par position (emplacement entier).

5. **Comment créez-vous une nouvelle colonne à partir des colonnes existantes ?**
   - Attribuez une nouvelle colonne : `df['NewColumn'] = df['Col1'] + df['Col2']`

## Résumé

Pandas est essentiel pour l'analyse de données en Python :

- Les **DataFrames** sont des tableaux 2D avec des lignes et des colonnes
- **Charger les données** à partir de CSV, Excel, bases de données
- **Explorer les données** avec `describe()`, `info()`, `head()`
- **Nettoyer les données** en traitant les valeurs manquantes et les doublons
- **Transformer les données** en créant de nouvelles colonnes, en filtrant, en triant
- **Agréger les données** using `groupby()` et `agg()`
- **Exporter les données** en CSV ou autres formats

Pandas permet une analyse de données efficace et professionnelle.

## Prochaines Étapes

- Pratiquez avec des ensembles de données réels (Kaggle, bases de données gouvernementales)
- Apprenez la visualisation des données avec matplotlib et seaborn
- Explorez les fonctionnalités avancées de pandas (fusion, remodelage)
- Combinez pandas avec les bibliothèques d'apprentissage automatique (scikit-learn)

---

*Félicitations d'être arrivé à l'analyse de données avancée ! Consultez davantage de leçons dans la section [Data Science](index-fr.md).*
