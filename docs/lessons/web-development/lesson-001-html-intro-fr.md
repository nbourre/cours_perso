---
title: "Les Fondamentaux du HTML : Construire des Pages Web"
description: "Créez vos premières pages web en utilisant le balisage HTML sémantique et comprenez la structure des documents"
difficulty: "Beginner"
duration: "45 minutes"
tags: [html, web, markup, semantic-html, elements]
learning_objectives:
  - "Comprendre ce que le HTML est et son rôle dans les pages web"
  - "Créer une structure de document HTML valide"
  - "Utiliser correctement les éléments HTML courants"
  - "Écrire un HTML sémantique et accessible"
created: 2026-01-30
author: "LLM Assistant"
status: "published"
lang: fr
---

# Les Fondamentaux du HTML : Construire des Pages Web

**Difficulté**: 🟢 Débutant | **Durée**: 45 minutes

**Tags**: [`html`](../../guides/tags-reference-fr.md#html) · [`web`](../../guides/tags-reference-fr.md#web) · [`markup`](../../guides/tags-reference-fr.md#markup) · [`semantic-html`](../../guides/tags-reference-fr.md#semantic-html) · [`elements`](../../guides/tags-reference-fr.md#elements)

---

## Objectifs d'Apprentissage

À la fin de cette leçon, vous serez capable de :

- Comprendre ce que le HTML est et son rôle dans les pages web
- Créer une structure de document HTML valide
- Utiliser correctement les éléments HTML courants
- Écrire un HTML sémantique et accessible

## Introduction

**HTML** (HyperText Markup Language) est la base de chaque page web. Il fournit la structure et le contenu que les navigateurs web affichent. Le HTML fonctionne aux côtés du CSS (style) et de JavaScript (interactivité) pour créer des expériences web complètes.

Pensez au HTML comme le squelette d'une page web :

- **HTML** = Structure (os)
- **CSS** = Style (peau, muscles)
- **JavaScript** = Interactivité (mouvement)

Dans cette leçon, nous nous concentrons sur les fondamentaux du HTML.

## Qu'est-ce que le HTML ?

Le HTML utilise des **balises** pour dire aux navigateurs comment afficher le contenu. Une balise ressemble à ceci :

```html
<tag>content</tag>
```

Les balises se présentent par paires (ouverture et fermeture) et peuvent avoir des **attributs** qui fournissent des informations supplémentaires :

```html
<tag attribute="value">content</tag>
```

### Balises HTML Courantes

Voici les éléments HTML les plus essentiels :

#### Titres
```html
<h1>Titre Principal</h1>        <!-- Plus grand, plus important -->
<h2>Titre de Section</h2>
<h3>Titre de Sous-section</h3>
<h4>Plus Petit Titre</h4>
<h5>Encore Plus Petit</h5>
<h6>Plus Petit Titre</h6>  <!-- Moins important -->
```

#### Paragraphes et Texte
```html
<p>Ceci est un paragraphe de texte.</p>
<strong>Texte important</strong>
<em>Texte accentué</em>
<br>  <!-- Saut de ligne (pas de balise fermante nécessaire) -->
```

#### Liens
```html
<a href="https://example.com">Cliquez ici</a>
<a href="page.html">Aller à une autre page</a>
```

#### Listes
```html
<!-- Liste non ordonnée (à puces) -->
<ul>
  <li>Élément 1</li>
  <li>Élément 2</li>
</ul>

<!-- Liste ordonnée (numérotée) -->
<ol>
  <li>Première étape</li>
  <li>Deuxième étape</li>
</ol>
```

#### Images
```html
<img src="photo.jpg" alt="Description de l'image">
```

## Structure du Document HTML

Chaque page HTML suit cette structure :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Titre de la Page</title>
  </head>
  <body>
    <!-- Le contenu va ici -->
  </body>
</html>
```

**Décomposons-le** :

- `<!DOCTYPE html>` : Indique au navigateur qu'il s'agit de HTML5
- `<html>` : Élément racine contenant tout
- `<head>` : Contient les métadonnées (titre, jeu de caractères, liens CSS)
- `<meta charset="UTF-8">` : Spécifie l'encodage des caractères
- `<title>` : Titre de la page affiché dans l'onglet du navigateur
- `<body>` : Contient le contenu visible de la page

## Exemple Complet

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Ma Première Page Web</title>
  </head>
  <body>
    <h1>Bienvenue sur Ma Page Web</h1>
    <p>Ceci est ma première page HTML !</p>
    
    <h2>Mes Intérêts</h2>
    <ul>
      <li>Développement Web</li>
      <li>Programmation</li>
      <li>Design</li>
    </ul>
    
    <p>Consultez <a href="https://example.com">ce site</a> pour plus d'informations.</p>
  </body>
</html>
```

## HTML Sémantique

**HTML sémantique** signifie utiliser les balises HTML qui décrivent leur objectif, pas seulement comment elles apparaissent.

### Bon (Sémantique)
```html
<nav>
  <a href="/">Accueil</a>
  <a href="/about">À Propos</a>
</nav>

<article>
  <h1>Titre de l'Article</h1>
  <p>Contenu de l'article...</p>
</article>

<footer>
  <p>&copy; 2026 Ma Compagnie</p>
</footer>
```

### À Éviter (Non-Sémantique)
```html
<div>
  <a href="/">Accueil</a>
  <a href="/about">À Propos</a>
</div>

<div>
  <h1>Titre de l'Article</h1>
  <p>Contenu de l'article...</p>
</div>

<div>
  <p>&copy; 2026 Ma Compagnie</p>
</div>
```

Les balises sémantiques rendent le code plus facile à lire et améliorent l'accessibilité.

## Exercices

### Exercice 1 : Créez une Page HTML de Base

**Tâche** : Créez une page HTML sur votre passe-temps préféré qui comprend :

- Un titre dans l'onglet du navigateur
- Un titre principal (h1)
- Au moins un paragraphe décrivant le passe-temps
- Une liste à puces de choses liées au passe-temps

**Exemple de Solution** :
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Mon Passe-temps</title>
  </head>
  <body>
    <h1>Photographie</h1>
    <p>La photographie est ma meilleure façon de capturer les moments et d'exprimer ma créativité.</p>
    
    <h2>Pourquoi J'aime la Photographie</h2>
    <ul>
      <li>Elle m'aide à voir le monde différemment</li>
      <li>Je peux partager des souvenirs avec les autres</li>
      <li>C'est une forme d'expression créative</li>
    </ul>
  </body>
</html>
```

### Exercice 2 : Créez une Page de Recette

**Tâche** : Créez une page de recette avec :

- Un titre de recette (h1)
- Une liste d'ingrédients (utilisez `<ol>` pour une liste numérotée)
- Des instructions (utilisez `<ol>` pour les étapes numérotées)
- Un lien vers un site de recettes associé

**Exemple de Solution** :
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Biscuits aux Pépites de Chocolat</title>
  </head>
  <body>
    <h1>Biscuits aux Pépites de Chocolat</h1>
    
    <h2>Ingrédients</h2>
    <ul>
      <li>2 tasses de farine</li>
      <li>1 tasse de beurre</li>
      <li>1 tasse de pépites de chocolat</li>
    </ul>
    
    <h2>Instructions</h2>
    <ol>
      <li>Mélanger les ingrédients secs</li>
      <li>Ajouter le beurre et mélanger</li>
      <li>Incorporer les pépites de chocolat</li>
      <li>Cuire à 375°F pendant 10 minutes</li>
    </ol>
    
    <p>Obtenez plus de recettes sur <a href="https://www.allrecipes.com">AllRecipes</a></p>
  </body>
</html>
```

## Évaluation

### Questions d'Autoévaluation

1. **Que signifie HTML et quel est son objectif ?**
   - HTML signifie HyperText Markup Language. Son objectif est de fournir la structure et le contenu des pages web.

2. **Quelle est la différence entre une balise ouvrante et une balise fermante ?**
   - Une balise ouvrante marque le début d'un élément (par ex. `<p>`). Une balise fermante marque où il se termine (par ex. `</p>`).

3. **Quels éléments doivent être à l'intérieur de la balise `<head>` ?**
   - Les métadonnées comme le titre de la page (`<title>`), le jeu de caractères (`<meta>`) et les liens aux feuilles de style doivent être dans le `<head>`.

4. **Qu'est-ce que le HTML sémantique et pourquoi est-il important ?**
   - Le HTML sémantique utilise des balises qui décrivent leur objectif (comme `<nav>`, `<article>`, `<footer>`). C'est important pour l'accessibilité et la lisibilité du code.

5. **Quel est l'ordre correct des balises HTML, HEAD et BODY ?**
   - La balise `<html>` enveloppe tout. À l'intérieur se trouvent `<head>` (d'abord) et `<body>` (deuxième).

## Résumé

Le HTML est la base des pages web :

- Le HTML utilise des **balises** pour structurer le contenu
- Chaque page a besoin d'une **structure de document** adéquate avec `<!DOCTYPE>`, `<html>`, `<head>`, et `<body>`
- Utilisez les balises **HTML sémantique** pour écrire un code accessible et lisible
- Apprenez les balises courantes pour les titres, paragraphes, liens, listes et images
- La structure n'est que le début—CSS ajoute le style et JavaScript ajoute l'interactivité

## Prochaines Étapes

- Pratiquez l'écriture de pages HTML sur différents sujets
- Apprenez le CSS pour styliser vos pages HTML
- Explorez les formulaires (`<form>`, `<input>`) pour l'interaction des utilisateurs
- Consultez la leçon [CSS Essentials](lesson-002-css-basics-fr.md) pour ajouter du style

---

*Un excellent début ! Ensuite, apprenez à styliser vos pages avec [CSS Essentials](lesson-002-css-basics-fr.md).*
