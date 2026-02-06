---
title: "Les Bases du CSS : Styliser Vos Pages Web"
description: "Maîtrisez le CSS pour rendre vos pages web magnifiques avec des couleurs, des mises en page et un design réactif"
difficulty: "Beginner"
duration: "1 hour"
tags: [css, styling, web, selectors, layout, responsive]
learning_objectives:
  - "Comprendre la syntaxe CSS et comment appliquer les styles"
  - "Utiliser les sélecteurs CSS pour cibler les éléments HTML"
  - "Appliquer efficacement les couleurs, les polices et l'espacement"
  - "Créer des mises en page réactives pour différentes tailles d'écran"
prerequisites: [lesson-001-html-intro]
created: 2026-01-30
author: "LLM Assistant"
status: "published"
---

# Les Bases du CSS : Styliser Vos Pages Web

**Difficulté**: 🟢 Débutant | **Durée**: 1 heure

**Tags**: [`css`](../../guides/tags-reference-fr.md#css) · [`styling`](../../guides/tags-reference-fr.md#styling) · [`web`](../../guides/tags-reference-fr.md#web) · [`selectors`](../../guides/tags-reference-fr.md#selectors) · [`layout`](../../guides/tags-reference-fr.md#layout) · [`responsive`](../../guides/tags-reference-fr.md#responsive)

---

## Objectifs d'Apprentissage

À la fin de cette leçon, vous serez capable de :
- Comprendre la syntaxe CSS et comment appliquer les styles
- Utiliser les sélecteurs CSS pour cibler les éléments HTML
- Appliquer efficacement les couleurs, les polices et l'espacement
- Créer des mises en page réactives pour différentes tailles d'écran

## Introduction

**CSS** (Cascading Style Sheets) est le langage du design web. Bien que le HTML fournisse la structure, le CSS rend les pages web magnifiques en contrôlant les couleurs, les polices, les mises en page et l'espacement.

Le CSS vous permet de :
- **Styliser le texte** : Couleurs, polices, tailles
- **Contrôler la mise en page** : Positionnement, grilles, flexbox
- **Ajouter des effets visuels** : Ombres, bordures, animations
- **Rendre les pages réactives** : Adapter à différentes tailles d'écran
- **Séparer le contenu du design** : Garder le HTML propre

## Les Bases du CSS

### Syntaxe CSS

Une règle CSS a deux parties :

```css
selector {
  property: value;
}
```

**Exemple** :
```css
p {
  color: blue;
  font-size: 16px;
}
```

Cela signifie : "Rendre tous les paragraphes bleus et de 16 pixels de large."

### Trois Façons d'Ajouter du CSS

#### 1. CSS Inline
```html
<p style="color: red;">Ce texte est rouge</p>
```

#### 2. CSS Interne (dans `<head>`)
```html
<head>
  <style>
    p {
      color: red;
    }
  </style>
</head>
```

#### 3. CSS Externe (recommandé)
```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

Dans `styles.css` :
```css
p {
  color: red;
}
```

## Sélecteurs CSS

Les sélecteurs déterminent quels éléments HTML sont stylisés.

### Sélecteur d'Élément
```css
p {
  color: blue;
}
```
Style TOUS les éléments `<p>`.

### Sélecteur de Classe
```css
.highlight {
  background-color: yellow;
}
```

```html
<p class="highlight">Ceci est mis en évidence</p>
```

### Sélecteur d'ID
```css
#header {
  background-color: navy;
  color: white;
}
```

```html
<div id="header">Bienvenue</div>
```

### Sélecteurs Multiples
```css
h1, h2, h3 {
  color: darkgreen;
}
```
Style tous les éléments h1, h2 et h3 de la même manière.

## Propriétés CSS Courantes

### Couleurs
```css
p {
  color: blue;                    /* Couleur du texte */
  background-color: lightblue;    /* Couleur de fond */
  border: 2px solid black;        /* Bordure */
}
```

Les couleurs peuvent être : nommées (`red`), hexadécimales (`#FF0000`) ou RGB (`rgb(255, 0, 0)`)

### Polices
```css
body {
  font-family: Arial, sans-serif;    /* Type de police */
  font-size: 14px;                   /* Taille du texte */
  font-weight: bold;                 /* Gras, normal */
  line-height: 1.5;                  /* Espace entre les lignes */
}
```

### Espacement
```css
p {
  margin: 10px;         /* Espace à l'extérieur de l'élément */
  padding: 10px;        /* Espace à l'intérieur de l'élément */
}
```

### Modèle de Boîte
```css
div {
  width: 300px;         /* Largeur de l'élément */
  height: 200px;        /* Hauteur de l'élément */
  margin: 20px;         /* Espacement externe */
  padding: 15px;        /* Espacement interne */
  border: 1px solid;    /* Bordure */
}
```

## Exemple Complet

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Page Stylisée</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f5f5f5;
        margin: 0;
        padding: 20px;
      }
      
      h1 {
        color: darkblue;
        border-bottom: 3px solid darkblue;
        padding-bottom: 10px;
      }
      
      .intro {
        background-color: lightblue;
        padding: 15px;
        border-radius: 5px;
      }
      
      p {
        line-height: 1.6;
        color: #333;
      }
    </style>
  </head>
  <body>
    <h1>Bienvenue sur Mon Site</h1>
    <p class="intro">Ceci est un paragraphe d'introduction stylisé.</p>
    <p>Ce paragraphe a un style régulier.</p>
  </body>
</html>
```

## Les Bases du Design Réactif

Le design réactif rend les pages belles sur les téléphones, les tablettes et les ordinateurs.

### La Balise Viewport Meta
Incluez toujours ceci dans votre `<head>` :
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Media Queries
Ajustez les styles en fonction de la taille de l'écran :

```css
/* Styles de bureau */
.container {
  width: 1000px;
}

/* Styles de tablette */
@media (max-width: 768px) {
  .container {
    width: 100%;
  }
}

/* Styles mobiles */
@media (max-width: 480px) {
  .container {
    width: 100%;
    padding: 10px;
  }
}
```

## Exercices

### Exercice 1 : Styliser une Page Simple

**Tâche** : Créez une page HTML avec CSS qui stylise :
- Un titre avec une couleur de fond et une couleur de texte
- Des paragraphes avec une police et un espacement spécifiques
- Au moins un élément avec un sélecteur de classe

**Exemple de Solution** :
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Ma Page Stylisée</title>
    <style>
      h1 {
        color: white;
        background-color: navy;
        padding: 20px;
        text-align: center;
      }
      
      p {
        font-size: 16px;
        line-height: 1.6;
        color: #333;
      }
      
      .special {
        color: red;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <h1>Mon Site</h1>
    <p>Bienvenue sur ma page.</p>
    <p class="special">Ce paragraphe est spécial !</p>
  </body>
</html>
```

### Exercice 2 : Créez une Mise en Page de Carte

**Tâche** : Créez une "carte" avec CSS qui a :
- Une bordure
- Rembourrage à l'intérieur
- Un effet d'ombre
- Une couleur de fond différente de la page

**Exemple de Solution** :
```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        background-color: #f0f0f0;
        padding: 20px;
      }
      
      .card {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        max-width: 400px;
      }
      
      .card h2 {
        margin-top: 0;
        color: darkblue;
      }
    </style>
  </head>
  <body>
    <div class="card">
      <h2>Carte Produit</h2>
      <p>Ceci est un composant de carte stylisé.</p>
    </div>
  </body>
</html>
```

## Évaluation

### Questions d'Autoévaluation

1. **Que signifie CSS et quel est son objectif ?**
   - CSS signifie Cascading Style Sheets. Son objectif est de styliser les éléments HTML avec des couleurs, des polices, des mises en page et de l'espacement.

2. **Quelles sont les trois façons d'ajouter du CSS à une page HTML ?**
   - CSS Inline (dans la balise HTML), CSS Interne (dans la balise `<style>`), CSS Externe (dans un fichier .css séparé).

3. **Quelle est la différence entre un sélecteur de classe et un sélecteur d'ID ?**
   - Les sélecteurs de classe (`.classname`) peuvent être utilisés sur plusieurs éléments. Les sélecteurs d'ID (`#idname`) sont uniques à un élément.

4. **Que comprend le modèle de boîte CSS ?**
   - Le modèle de boîte comprend la marge (espace externe), la bordure, le rembourrage (espace interne) et le contenu.

5. **Comment rendre une page réactive à différentes tailles d'écran ?**
   - Utilisez la balise viewport meta et les media queries pour ajuster les styles en fonction de la largeur de l'écran.

## Résumé

Le CSS transforme le HTML brut en magnifiques pages web :

- **Syntaxe CSS** : `selector { property: value; }`
- **Trois options de placement** : Inline, interne, externe (externe recommandé)
- **Sélecteurs** : Élément, classe, ID pour cibler les éléments
- **Propriétés clés** : Couleur, police, espacement, bordures, dimensions
- **Design réactif** : Utilisez les media queries pour différentes tailles d'écran

Le CSS est le lien entre le contenu et le design !

## Prochaines Étapes

- Pratiquez la stylisation de divers éléments HTML
- Apprenez flexbox et CSS Grid pour les mises en page avancées
- Explorez les animations et transitions CSS
- Plongez dans JavaScript pour ajouter de l'interactivité à vos styles

---

*Vous êtes maintenant prêt à créer de magnifiques pages web ! Explorez davantage de leçons dans la section [Web Development](index-fr.md).*
