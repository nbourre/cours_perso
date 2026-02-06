# Modèle de Leçon Contrat

**Objectif**: Structure Markdown standard pour toutes les leçons  
**Emplacement**: `docs/templates/lesson-template.md` (modèle accessible aux utilisateurs)  
**Obligatoire**: Toutes les leçons DOIVENT suivre cette structure

---

## Structure du Modèle

```markdown
---
title: "[Titre de la Leçon]"
description: "[Résumé d'une phrase de ce que les apprenants apprendront]"
difficulty: "Beginner"  # Options: Beginner, Intermediate, Advanced
duration: "30 minutes"  # Inclure l'unité (minutes, heures, jours)
tags: [tag1, tag2, tag3]  # 1-5 tags minuscules, avec tirets
prerequisites: []  # Optionnel: IDs de leçons à compléter en premier
learning_objectives:
  - "Objectif d'apprentissage 1"
  - "Objectif d'apprentissage 2"
  - "Objectif d'apprentissage 3"
created: 2026-01-30
author: "Votre Nom ou Assistant LLM"
status: "published"  # Options: draft, published, archived
---

# [Titre de la Leçon]

## Objectifs d'Apprentissage

À la fin de cette leçon, vous pourrez:
- [Objectif d'apprentissage 1]
- [Objectif d'apprentissage 2]
- [Objectif d'apprentissage 3]

## Prérequis

[Le cas échéant, énumérez les prérequis ou créez un lien vers les leçons préalables]

**Note**: Il est recommandé de compléter [Nom de la Leçon] avant de commencer cette leçon.

## Introduction

[Fournir le contexte et la motivation. Pourquoi les apprenants devraient-ils se soucier de ce sujet? Quel problème résout-il?]

## [Concept Principal/Module 1]

[Expliquez le premier concept clé avec des exemples et des explications clairs]

### Exemple 1: [Exemple Spécifique]

[Fournir un exemple concret et relatable]

### Exemple 2: [Un Autre Exemple]

[Fournir un autre exemple démontrant un aspect différent]

## [Concept Principal/Module 2]

[Expliquez le deuxième concept clé]

### Exemple 1: [Exemple Spécifique]

[Fournir des exemples avec code, diagrammes ou walkthroughs]

## [Concept Principal/Module 3] (Optionnel)

[Ajouter plus de modules au besoin]

## Exercices

### Exercice 1: [Titre Descriptif]

**Difficulté**: Beginner  
**Temps**: 5-10 minutes

[Décrivez l'exercice et ce que les apprenants doivent faire]

**Résultat attendu**: [Ce que l'apprenant doit pouvoir faire/créer]

### Exercice 2: [Titre Descriptif]

**Difficulté**: Intermediate  
**Temps**: 15-20 minutes

[Décrivez un exercice plus défi]

### Exercice Défi (Optionnel)

[Exercice avancé pour les apprenants motivés]

## Évaluation

### Questions d'Auto-Évaluation

1. [Question 1 pour vérifier la compréhension]
2. [Question 2]
3. [Question 3]

### Projet ou Capstone

[Optionnel: Décrivez un projet qui intègre tous les concepts de la leçon]

## Résumé

[Récapitulez les points clés appris dans cette leçon]

## Ressources Supplémentaires

- [Lien 1: Documentation connexe]
- [Lien 2: Tutoriel ou outil]
- [Lien 3: Matériel de référence]

## Prochaines Étapes

Après avoir complété cette leçon, vous voudrez peut-être explorer:
- [Leçon de suivi suggérée 1]
- [Leçon de suivi suggérée 2]
- [Concept connexe ou compétence]

---

## Checklist de Validation des Métadonnées

- [ ] Tous les champs de métadonnées obligatoires présents (title, description, difficulty, duration, tags, learning_objectives)
- [ ] Le titre est clair et descriptif
- [ ] La description est 1 phrase, non-technique
- [ ] La difficulté est l'une de: Beginner, Intermediate, Advanced
- [ ] La durée inclut l'unité (minutes, heures, jours)
- [ ] Les tags sont 1-5 éléments, minuscules, avec tirets
- [ ] Les objectifs d'apprentissage sont 3-5 résultats spécifiques et mesurables
- [ ] Le statut est l'un de: draft, published, archived
- [ ] La date de création est au format YYYY-MM-DD

## Checklist de Validation du Contenu

- [ ] Toutes les sections obligatoires présentes: Objectifs d'Apprentissage, Introduction, Concepts Clés, Exercices, Évaluation
- [ ] Les objectifs d'apprentissage sont référencés et abordés dans le contenu
- [ ] Les exemples sont clairs, pertinents et incluent le code/des diagrammes le cas échéant
- [ ] Les exercices sont progressifs (simple → complexe)
- [ ] L'évaluation vérifie l'apprentissage de tous les objectifs
- [ ] Les liens vers les leçons préalables et connexes sont corrects
- [ ] Pas de liens brisés ou de références
- [ ] La syntaxe Markdown est correcte (se rend correctement dans MkDocs)
```

---

## Instructions d'Utilisation

### Pour les Créateurs de Contenu

1. Copiez ce modèle dans un nouveau fichier: `lesson-[id]-[slug].md`
2. Remplissez tous les champs de métadonnées (titre, description, difficulté, tags, etc.)
3. Remplacez les sections placeholders par votre contenu
4. Assurez-vous que toutes les sections obligatoires sont présentes
5. Ajoutez des exemples et des exercices spécifiques à votre sujet
6. Testez en exécutant `mkdocs serve` et en visualisant la leçon rendue
7. Soumettez une demande de tirage avec votre nouvelle leçon

### Pour la Génération d'Invite LLM

Lorsque vous utilisez un LLM (ChatGPT, Claude, etc.) pour générer du contenu de leçon:

1. Remplissez uniquement la section de métadonnées avec les détails de votre leçon
2. Fournissez la structure du modèle au LLM avec instruction de remplir les sections
3. Collez l'invite suivante dans votre LLM:

**Modèle d'Invite LLM**:
```
Je veux que vous créiez une leçon éducative suivant cette structure Markdown exacte.
La leçon devrait être pour [public/niveau] et enseigner [sujet/concept].

Utilisez ce modèle:
[Collez le modèle ici]

Exigences importantes:
- Gardez les explications claires et accessibles pour le public cible
- Incluez 2-3 exemples pratiques avec code/diagrammes
- Créez 2-3 exercices (difficulté progressive)
- Incluez les questions d'auto-évaluation pour l'évaluation
- Utilisez un langage clair, évitez le jargon (ou expliquez-le)
- Assurez-vous que la leçon peut être complétée en environ [durée]

Le contenu généré doit être prêt à coller directement dans un fichier Markdown.
```

4. Copiez le contenu généré dans le fichier du modèle
5. Examinez l'exactitude et l'alignement avec les objectifs d'apprentissage
6. Soumettez pour publication

---

## Notes de Conformité

- Chaque leçon publiée DOIT être conforme à ce modèle
- Les leçons manquant des sections obligatoires seront marquées avec le statut "draft" jusqu'à leur achèvement
- La validation automatisée (GitHub Actions) vérifiera la conformité avant le déploiement
- Les mises à jour du modèle sont rétro-compatibles (les leçons existantes rendront toujours correctement)
