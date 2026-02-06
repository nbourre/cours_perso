---
title: "Fonctions : Réutilisation et Organisation du Code"
description: "Apprenez à écrire des fonctions réutilisables pour organiser votre code et éviter la répétition"
difficulty: "Beginner"
duration: "45 minutes"
tags: [python, functions, code-organization, parameters, return-values]
learning_objectives:
  - "Comprendre ce que sont les fonctions et pourquoi elles sont utiles"
  - "Définir et appeler des fonctions avec des paramètres"
  - "Utiliser les valeurs de retour pour obtenir les résultats des fonctions"
  - "Appliquer les fonctions pour organiser le code efficacement"
prerequisites: [lesson-001-variables]
created: 2026-01-30
author: "LLM Assistant"
status: "published"
lang: fr
---

# Fonctions : Réutilisation et Organisation du Code

**Difficulté**: 🟢 Débutant | **Durée**: 45 minutes

**Tags**: [`python`](../../guides/tags-reference-fr.md#python) · [`functions`](../../guides/tags-reference-fr.md#functions) · [`code-organization`](../../guides/tags-reference-fr.md#code-organization) · [`parameters`](../../guides/tags-reference-fr.md#parameters) · [`return-values`](../../guides/tags-reference-fr.md#return-values)

---

## Objectifs d'Apprentissage

À la fin de cette leçon, vous serez capable de :
- Comprendre ce que sont les fonctions et pourquoi elles sont utiles
- Définir et appeler des fonctions avec des paramètres
- Utiliser les valeurs de retour pour obtenir les résultats des fonctions
- Appliquer les fonctions pour organiser le code efficacement

## Introduction

Une **fonction** est un bloc de code réutilisable qui effectue une tâche spécifique. Les fonctions sont l'un des outils les plus puissants en programmation car elles vous permettent de :

- **Éviter la répétition** : Écrivez du code une fois, utilisez-le plusieurs fois
- **Organiser le code** : Divisez les problèmes complexes en parties plus petites
- **Rendre le code lisible** : Donnez des noms significatifs aux blocs de logique
- **Tester plus facilement** : Testez les fonctions individuelles isolément
- **Collaborer** : Travaillez avec vos collègues en utilisant des fonctions partagées

Sans fonctions, votre code deviendrait long, confus et difficile à maintenir.

## Qu'est-ce qu'une Fonction ?

Une fonction a ces parties :

1. **Nom** : Comment vous appelez la fonction
2. **Paramètres** (optionnel) : Les entrées que la fonction reçoit
3. **Corps** : Le code que la fonction exécute
4. **Valeur de retour** (optionnel) : La sortie que la fonction donne

### Structure Simple d'une Fonction

```python
def function_name(parameters):
    # Code goes here (the "body")
    return result
```

Le mot clé `def` signifie "définir une fonction."

## Créer et Appeler des Fonctions

### Exemple 1 : Une Fonction Simple

```python
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
greet()  # Output: Hello, World!
```

Remarquez que nous avons écrit `print("Hello, World!")` une seule fois dans la définition de la fonction, mais nous pouvons l'appeler plusieurs fois !

### Exemple 2 : Fonctions avec Paramètres

Les paramètres vous permettent de passer des données à une fonction. Ce sont comme des entrées.

```python
def greet(name):
    print(f"Hello, {name}!")

# Call the function with different inputs
greet("Alice")   # Output: Hello, Alice!
greet("Bob")     # Output: Hello, Bob!
```

### Exemple 3 : Fonctions avec Valeurs de Retour

Une valeur de retour est ce que la fonction vous renvoie.

```python
def add(a, b):
    result = a + b
    return result

# Call the function and use the result
sum1 = add(5, 3)      # sum1 is 8
sum2 = add(10, 20)    # sum2 is 30
print(sum1 + sum2)    # Output: 58
```

### Exemple 4 : Fonction Complète

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

# Use the function
room_area = calculate_area(5, 4)  # 20 square meters
print(f"Room area: {room_area} m²")  # Output: Room area: 20 m²
```

## Paramètres de Fonction

### Paramètre Unique

```python
def square(number):
    result = number * number
    return result

print(square(5))  # Output: 25
```

### Paramètres Multiples

```python
def add(a, b):
    return a + b

print(add(3, 7))  # Output: 10
```

### Paramètres par Défaut

Vous pouvez fournir des valeurs par défaut :

```python
def greet(name="Friend"):
    return f"Hello, {name}!"

print(greet())           # Output: Hello, Friend!
print(greet("Alice"))    # Output: Hello, Alice!
```

## Valeurs de Retour

Les fonctions peuvent renvoyer des données que vous utilisez dans votre programme :

```python
def get_user_info():
    age = 25
    name = "Alice"
    return name, age  # Can return multiple values!

name, age = get_user_info()
print(f"{name} is {age} years old")  # Output: Alice is 25 years old
```

## Exercices

### Exercice 1 : Créez une Fonction Simple
Créez une fonction qui convertit les degrés Celsius en Fahrenheit.

**Formule** : `F = (C × 9/5) + 32`

**Tâche** : Écrivez une fonction nommée `celsius_to_fahrenheit` qui :
- Prend une température en Celsius comme paramètre
- Calcule l'équivalent en Fahrenheit
- Renvoie le résultat

**Exemple de Solution** :
```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test it
print(celsius_to_fahrenheit(0))    # Output: 32.0
print(celsius_to_fahrenheit(100))  # Output: 212.0
```

### Exercice 2 : Fonction avec Paramètres Multiples
Créez une fonction qui calcule un prix avec réduction.

**Tâche** : Écrivez une fonction nommée `apply_discount` qui :
- Prend le prix original et le pourcentage de réduction comme paramètres
- Calcule le nouveau prix
- Renvoie le prix après réduction

**Exemple de Solution** :
```python
def apply_discount(original_price, discount_percent):
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    return final_price

# Test it
print(apply_discount(100, 20))  # Output: 80.0 (20% off)
print(apply_discount(50, 10))   # Output: 45.0 (10% off)
```

### Défi : Fonction qui Renvoie Plusieurs Valeurs

Créez une fonction qui analyse une liste de nombres.

**Tâche** : Écrivez une fonction nommée `analyze_numbers` qui :
- Prend une liste de nombres comme paramètre
- Calcule la somme, la moyenne, et le nombre d'éléments
- Renvoie les trois valeurs

**Exemple de Solution** :
```python
def analyze_numbers(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, average, count

# Test it
data = [10, 20, 30, 40]
total, avg, count = analyze_numbers(data)
print(f"Sum: {total}, Average: {avg}, Count: {count}")
# Output: Sum: 100, Average: 25.0, Count: 4
```

## Évaluation

### Questions d'Autoévaluation

1. **Qu'est-ce qu'une fonction et pourquoi sont-elles utiles ?**
   - Une fonction est un bloc de code réutilisable qui effectue une tâche. Les fonctions vous aident à éviter la répétition, à organiser le code et à rendre les programmes plus lisibles.

2. **Comment défilez-vous une fonction en Python ?**
   - Utilisez le mot clé `def` suivi du nom de la fonction et des parenthèses : `def function_name(parameters):` puis le corps de la fonction.

3. **Quelle est la différence entre un paramètre et un argument ?**
   - Un paramètre est ce que vous définissez dans la fonction (par ex. `def add(a, b)`). Un argument est la valeur réelle que vous passez lors de l'appel de la fonction (par ex. `add(3, 5)`).

4. **Que fait l'instruction `return` ?**
   - L'instruction `return` renvoie une valeur de la fonction au code qui l'a appelée.

5. **Une fonction peut-elle ne pas avoir de paramètres ?**
   - Oui, vous pouvez écrire `def function_name():` avec des parenthèses vides.

## Résumé

Les fonctions sont essentielles pour écrire du code propre et organisé :

- **Défilez** les fonctions avec `def function_name():`
- **Utilisez des paramètres** pour passer des données aux fonctions
- **Utilisez les instructions return** pour renvoyer des résultats
- **Appelez les fonctions** par nom avec des arguments
- **Réutilisez le code** en appelant la même fonction plusieurs fois

Les fonctions vous aident à diviser les gros problèmes en petites parties gérables.

## Prochaines Étapes

- Écrivez vos propres fonctions pour des tâches quotidiennes
- Expérimentez avec des fonctions qui renvoient différents types de données
- Explorez les fonctions intégrées comme `len()`, `sum()`, `max()`
- Explorez la portée des variables (variables locales vs globales) dans les leçons futures

---

*Vous développez d'excellentes habitudes de programmation ! Consultez davantage de leçons dans la section [Python Basics](index-fr.md).*
