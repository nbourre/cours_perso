---
title: "Introduction aux Variables"
description: "Apprenez à créer et utiliser des variables pour stocker et manipuler des données en Python"
difficulty: "Beginner"
duration: "30 minutes"
tags: [python, variables, data-types, basics]
learning_objectives:
  - "Comprendre ce que sont les variables et pourquoi elles sont utiles"
  - "Créer et assigner des valeurs aux variables"
  - "Comprendre les types de données Python (chaînes, entiers, décimales, booléens)"
created: 2026-01-30
author: "LLM Assistant"
status: "published"
---

# Introduction aux Variables

**Difficulté**: 🟢 Débutant | **Durée**: 30 minutes

**Tags**: [`python`](../../guides/tags-reference-fr.md#python) · [`variables`](../../guides/tags-reference-fr.md#variables) · [`data-types`](../../guides/tags-reference-fr.md#data-types) · [`basics`](../../guides/tags-reference-fr.md#basics)

---

## Objectifs d'Apprentissage

À la fin de cette leçon, vous serez capable de :
- Comprendre ce que sont les variables et pourquoi elles sont utiles
- Créer et assigner des valeurs aux variables
- Comprendre les types de données Python (chaînes, entiers, décimales, booléens)

## Introduction

En programmation, une **variable** est un conteneur nommé qui stocke une valeur. Pensez-y comme une boîte étiquetée où vous pouvez mettre des informations que votre programme utilise et consulte plus tard.

Les variables sont essentielles car elles vous permettent de :
- **Stocker des données** dont votre programme a besoin pour fonctionner
- **Référencer les données** par un nom significatif au lieu de mémoriser les valeurs
- **Modifier les valeurs** au fur et à mesure que votre programme s'exécute
- **Réutiliser les données** dans tout votre code

Sans variables, la programmation serait presque impossible !

## Qu'est-ce qu'une Variable ?

Une variable a trois éléments clés :
1. **Nom** : Comment vous la référencez (par ex. `age`, `user_name`)
2. **Type** : Quel type de données elle stocke (par ex. texte, nombre)
3. **Valeur** : Les données réelles stockées (par ex. 25, "Alice")

### Créer une Variable

En Python, créer une variable est simple :

```python
variable_name = value
```

**Exemple** :
```python
age = 25
name = "Alice"
height = 5.6
is_student = True
```

Le signe `=` s'appelle l'**opérateur d'assignation**. Cela signifie "stockez cette valeur dans cette variable."

## Types de Données Python

Python a plusieurs types de données fondamentaux. Explorons les plus courants :

### 1. Entier (int)
Les nombres entiers sans décimales.

```python
age = 25
temperature = -5
count = 0
```

### 2. Décimal (float)
Les nombres avec décimales.

```python
price = 19.99
pi = 3.14159
height = 5.6
```

### 3. Chaîne de Caractères (str)
Du texte, entre guillemets (simple `'` ou double `"`).

```python
name = "Alice"
greeting = 'Hello, World!'
address = "123 Main Street"
```

### 4. Booléen (bool)
Les valeurs Vrai ou Faux (utilisées pour la logique et les décisions).

```python
is_student = True
is_online = False
has_license = True
```

## Nommer les Variables

Lorsque vous nommez une variable, suivez ces conventions :
- ✅ **Utilisez des lettres minuscules** : `user_name`
- ✅ **Utilisez des tirets bas entre les mots** : `first_name`, `is_online`
- ✅ **Utilisez des noms significatifs** : `age` au lieu de `a`
- ❌ **Évitez les espaces** : `user name` ne fonctionne pas
- ❌ **Ne commencez pas par des chiffres** : `2cars` est invalide, mais `cars2` est correct
- ❌ **N'utilisez pas les mots clés Python** : `class`, `def`, `for` sont réservés

**Bons noms de variables** :
```python
user_age = 25
total_price = 99.99
is_active = True
customer_name = "John"
```

**Évitez les suivants** :
```python
a = 25                  # Pas significatif
User_Age = 25          # Utilisez des minuscules
user age = 25          # Impossible d'utiliser des espaces
2user = 25             # Impossible de commencer par un chiffre
```

## Exercices

### Exercice 1 : Créez Vos Premières Variables
Créez des variables pour stocker des informations vous concernant.

**Tâche** : Écrivez un programme Python qui crée ces variables :
- Votre nom (chaîne de caractères)
- Votre âge (entier)
- Votre taille en mètres (décimal)
- Si vous aimez la programmation (booléen)

**Exemple de Solution** :
```python
name = "Alice"
age = 25
height = 1.75
likes_coding = True

print(name)          # Output: Alice
print(age)           # Output: 25
print(height)        # Output: 1.75
print(likes_coding)  # Output: True
```

### Exercice 2 : Stocker des Informations sur un Produit
Créez des variables pour représenter un produit dans une boutique en ligne.

**Tâche** : Créez des variables pour :
- Nom du produit (chaîne de caractères)
- Prix (décimal)
- Quantité en stock (entier)
- En solde (booléen)

**Exemple de Solution** :
```python
product_name = "Python Book"
price = 29.99
quantity_in_stock = 150
on_sale = True

print(f"{product_name}: ${price}")
```

## Évaluation

### Questions d'Autoévaluation

1. **Qu'est-ce qu'une variable et pourquoi les utilisons-nous ?**
   - Une variable est un conteneur nommé qui stocke des données. Nous les utilisons pour stocker les informations dont notre programme a besoin, rendre le code plus lisible, et faciliter la modification des valeurs.

2. **Comment créez-vous une variable en Python ?**
   - Utilisez la syntaxe : `variable_name = value`. Par exemple, `age = 25`.

3. **Quels sont les quatre types de données fondamentaux mentionnés dans cette leçon ?**
   - Les entiers (nombres entiers), les décimales (nombres avec virgule), les chaînes de caractères (texte), et les booléens (Vrai/Faux).

4. **Pouvez-vous nommer une variable avec un espace ? Pourquoi ou pourquoi pas ?**
   - Non, Python ne permet pas les espaces dans les noms de variables. Utilisez plutôt des tirets bas : `user_name` et non `user name`.

5. **Écrivez une ligne Python qui crée une variable nommée `favorite_color` avec la valeur "bleu".**
   - `favorite_color = "bleu"`

## Résumé

Les variables sont fondamentales en programmation. Elles vous permettent de stocker, référencer, et manipuler les données. Souvenez-vous :

- Créez les variables avec : `name = value`
- Utilisez des noms significatifs et en minuscules avec des tirets bas
- Python a quatre types fondamentaux : int, float, str, bool
- Une fois créées, vous pouvez utiliser les variables dans tout votre code

Dans la leçon suivante, vous apprendrez à faire des choses avec les variables—calculer avec les nombres, combiner les chaînes de caractères, et prendre des décisions en fonction de leurs valeurs.

## Prochaines Étapes

- Pratiquez la création de variables avec différents types de données
- Expérimentez l'affichage des variables
- Consultez la leçon [Fonctions](lesson-002-functions-fr.md) pour apprendre comment organiser le code avec les variables
- Explorez davantage les types de données Python (listes, dictionnaires) dans les leçons futures

---

*Prêt à en apprendre davantage ? Consultez [Fonctions : Réutilisation et Organisation du Code](lesson-002-functions-fr.md).*
