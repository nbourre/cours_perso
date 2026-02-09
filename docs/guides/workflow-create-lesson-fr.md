# Guide de flux de création de cours

**Objectif** : Guide étape par étape pour créer et publier de nouveaux cours  
**Public** : Créateurs de contenu, éducateurs, utilisateurs LLM  
**Temps requis** : 30-90 minutes selon la approche

---

## Table des matières

1. [Vue d'ensemble](#vue-densemble)
2. [Prérequis](#prérequis)
3. [Flux de travail étape par étape](#flux-de-travail-étape-par-étape)
4. [Utilisation du modèle LLM](#utilisation-du-modèle-llm)
5. [Liste de contrôle qualité](#liste-de-contrôle-qualité)
6. [Soumission et révision](#soumission-et-révision)
7. [FAQ](#faq)

---

## Vue d'ensemble

Ce flux décrit comment créer un nouveau cours pour le référentiel. Que vous rédigiez vous-même le contenu ou utilisiez un LLM (ChatGPT, Claude, etc.) pour le générer, ce guide vous aidera à produire un cours qui respecte les normes du référentiel.

**Niveau de compétence** : Connaître le Markdown et être à l'aise avec la ligne de commande serait utile mais n'est pas obligatoire

---

## Prérequis

- [ ] Compte GitHub (pour soumettre des demandes de fusion)
- [ ] Git installé sur votre ordinateur (téléchargez depuis [git-scm.com](https://git-scm.com))
- [ ] Éditeur de texte (VS Code, Sublime, Notepad++, etc.)
- [ ] Compréhension de base du Markdown (voir [Guide Markdown](https://www.markdownguide.org/basic-syntax/))
- [ ] Accès au LLM de votre choix si vous en utilisez un (optionnel)

---

## Flux de travail étape par étape

### Phase 1 : Planifier votre cours

**Temps** : 5-10 minutes

1. **Identifiez le sujet**

   - Quel concept ou compétence ce cours enseignera-t-il?
   - Exemples : « Conception API REST », « Fonctions Python », « Layout CSS Grid »

2. **Déterminez le niveau**

   - Est-ce pour des apprenants Débutant, Intermédiaire ou Avancé?
   - Quel savoir antérieur est supposé?

3. **Estimez le temps**

   - Combien de temps faut-il pour compléter (y compris les exercices)?
   - Estimations réalistes : 30 min, 45 min, 1 heure, 1,5 heure, 2 heures, etc.

4. **Identifiez la catégorie de sujet**

   - Quel sujet ce cours concerne-t-il? (Python, Développement Web, Science des données, etc.)
   - S'il ne correspond à aucun, proposez une nouvelle catégorie dans la description de votre RP

5. **Choisissez 3-5 étiquettes**

   - Quels mots-clés aideraient quelqu'un à découvrir ce cours?
   - Les étiquettes doivent être en minuscules et avec tirets (par ex., `api-design`, `rest`, `http`)

---

### Phase 2 : Rédiger ou générer le contenu

**Temps** : 30-60 minutes selon la approche

#### Option A : Rédiger le contenu vous-même

1. **Copiez le modèle de cours**

   - Téléchargez ou copiez [docs/templates/lesson-template.md](../templates/lesson-template.md)
   - Enregistrez sous : `lesson-[id]-[slug].md` (par ex., `lesson-001-python-intro.md`)

2. **Remplissez les métadonnées** (préambule YAML)

   - title, description, difficulty, duration, tags, learning_objectives, created, author
   - Voir [Spécification des métadonnées](metadata-reference.md) pour les détails

3. **Rédigez les sections de contenu**

   - Objectifs d'apprentissage, Introduction, Concepts principaux, Exemples, Exercices, Évaluation
   - Voir [Modèle de cours](../templates/lesson-template.md) pour la structure complète

4. **Passez à la Phase 3** → Vérifiez votre contenu

#### Option B : Générer avec LLM

1. **Préparez votre prompt**

   - Décidez de : sujet, niveau (Débutant/Intermédiaire/Avancé), durée
   - Exemple : « Je veux enseigner async/await JavaScript pour les développeurs Intermédiaires en 1 heure »

2. **Copiez le modèle de prompt LLM**

   - Voir [Utilisation du modèle LLM](#utilisation-du-modèle-llm) ci-dessous
   - Personnalisez-le pour votre cours

3. **Collez dans votre LLM** (ChatGPT, Claude, Gemini, etc.)

   - Utilisez le modèle de prompt
   - Incluez le modèle de structure de cours
   - Demandez des sections spécifiques : objectifs d'apprentissage, exemples, exercices

4. **Copiez le contenu généré**

   - Copiez la réponse du LLM (doit suivre la structure du modèle)
   - Collez dans un nouveau fichier : `lesson-[id]-[slug].md`

5. **Vérifiez et affinez**

   - Lisez pour vérifier la précision
   - Corrigez les incohérences avec votre sujet
   - Assurez-vous que les exemples sont clairs
   - Vérifiez que les objectifs d'apprentissage sont couverts

6. **Procédez à la Phase 3** → Vérifiez votre contenu

---

### Phase 3 : Vérifier votre contenu

**Temps** : 5-10 minutes

Utilisez la **Liste de contrôle qualité** ci-dessous pour vérifier votre cours :

**Vérification des métadonnées:**

- [ ] Tous les champs requis présents : title, description, difficulty, duration, tags, learning_objectives, created
- [ ] Le titre est clair et descriptif (3-100 caractères)
- [ ] La description est 1 phrase, non-technique (10-200 caractères)
- [ ] Difficulty est : Beginner, Intermediate ou Advanced
- [ ] Duration est réaliste et inclut l'unité (minutes/heures/jours)
- [ ] Tags sont 1-5 éléments, minuscules, avec tirets
- [ ] Les objectifs d'apprentissage sont 3-5 éléments, spécifiques et mesurables
- [ ] La date de création est au format AAAA-MM-JJ

**Vérification du contenu:**

- [ ] Toutes les sections requises présentes : Objectifs d'apprentissage, Introduction, Concepts principaux, Exercices, Évaluation
- [ ] Les objectifs d'apprentissage sont référencés dans le contenu
- [ ] Les exemples sont clairs, pertinents et incluent du code/des diagrammes
- [ ] Les exercices sont progressifs (simple → complexe, minimum 2-3 exercices)
- [ ] Les questions d'évaluation/auto-vérification vérifient la compréhension de chaque objectif
- [ ] La syntaxe Markdown est correcte
- [ ] Pas de liens ou références cassés
- [ ] L'écriture est claire et accessible pour le public cible

**Vérification de la structure:**

- [ ] Nommage du fichier : `lesson-[id]-[slug].md` (par ex., `lesson-001-functions.md`)
- [ ] Fichier situé dans le bon répertoire de sujet : `docs/lessons/[subject]/`
- [ ] Préambule YAML correctement formaté (entre les marqueurs `---`)
- [ ] Le contenu suit la structure du modèle

---

### Phase 4 : Créer une branche Git et valider

**Temps** : 5 minutes

1. **Clonez le référentiel** (première fois seulement)

   ```bash
   git clone https://github.com/[username]/[repo].git
   cd [repo]
   ```

2. **Créez une nouvelle branche**

   ```bash
   git checkout -b add-lesson-[slug]
   # Exemple : git checkout -b add-lesson-python-functions
   ```

3. **Ajoutez votre fichier de cours**

   ```bash
   git add docs/lessons/[subject]/lesson-[id]-[slug].md
   ```

4. **Validez vos modifications**

   ```bash
   git commit -m "Add lesson: [Title]"
   # Exemple : git commit -m "Add lesson: Introduction to Python Functions"
   ```

5. **Poussez vers votre fork**

   ```bash
   git push origin add-lesson-[slug]
   ```

---

### Phase 5 : Soumettre une demande de fusion

**Temps** : 5 minutes

1. **Allez sur GitHub**

   - Accédez au référentiel sur GitHub
   - Cliquez sur « Compare & pull request » (devrait apparaître après votre push)

2. **Remplissez les détails de la RP**

   - **Titre** : « Add lesson: [Title] »
   - **Description** : Incluez :
     - Résumé bref de ce que le cours enseigne
     - Niveau de difficulté et durée estimée
     - Catégorie de sujet
     - Toutes les notes pour les relecteurs

3. **Demandez une révision**

   - Assignez aux responsables du référentiel
   - Ajoutez l'étiquette : « lesson-submission »

4. **Attendez les commentaires**

   - Les responsables examineront la qualité et la conformité
   - Peuvent demander des modifications (ne vous inquiétez pas, c'est normal!)
   - Les cours approuvés sont fusionnés et automatiquement publiés sur GitHub Pages

---

## Utilisation du modèle LLM

### Démarrage rapide

Copiez et collez ce modèle dans votre LLM, en personnalisant les sections entre crochets :

```
Créez un cours éducatif sur [TOPIC] pour les apprenants [LEVEL].
Le cours devrait prendre environ [DURATION] pour être complété.

Utilisez cette structure Markdown exacte :

---
title: "[LESSON TITLE]"
description: "[Résumé d'une phrase]"
difficulty: "[LEVEL]"
duration: "[DURATION]"
tags: [tag1, tag2, tag3]
learning_objectives:
  - "Objectif 1"
  - "Objectif 2"
  - "Objectif 3"
created: 2026-01-30
author: "[Votre nom ou 'LLM Assistant']"
status: "published"
---

# [LESSON TITLE]

## Objectifs d'apprentissage

À la fin de ce cours, vous serez capable de :
- [Objectif 1]
- [Objectif 2]
- [Objectif 3]

## Introduction

[2-3 paragraphes introduisant le sujet, pourquoi c'est important, et quels problèmes cela résout]

## [Concept principal 1]

[Expliquez ce concept avec exemples et code]

## [Concept principal 2]

[Expliquez ce concept avec exemples]

## Exercices

### Exercice 1 : [Titre]
[Exercice pour débutant - tâche simple pour pratiquer le concept de base]

### Exercice 2 : [Titre]
[Exercice intermédiaire - appliquez le concept dans un scénario réaliste]

### Défi (Optionnel)
[Exercice avancé pour les apprenants motivés]

## Évaluation

### Questions d'auto-vérification
1. [Question pour vérifier la compréhension de l'objectif 1]
2. [Question pour vérifier la compréhension de l'objectif 2]
3. [Question pour vérifier la compréhension de l'objectif 3]

## Résumé

[Récapitulez les points clés]

---

Exigences importantes :
- Les explications doivent être claires et accessibles pour les apprenants [LEVEL]
- Incluez au moins 2-3 exemples pratiques avec code ou procédures
- Rendez les exercices progressifs (facile → difficile)
- Assurez-vous que le cours est réalisable en [DURATION]
- Utilisez un langage simple ; expliquez les termes techniques
- Le contenu doit être prêt à être collé directement dans un fichier Markdown
```

### Conseils de personnalisation

**Pour différents niveaux** :

- **Débutant** : Supposez aucune connaissance antérieure ; expliquez chaque terme ; utilisez des analogies
- **Intermédiaire** : Supposez une compréhension de base ; concentrez-vous sur l'application ; incluez les meilleures pratiques
- **Avancé** : Supposez une base solide ; plongez profond ; discutez des compromis et cas limites

**Pour différentes durées** :

- **30 minutes** : 1 concept principal, 2 exercices simples
- **1 heure** : 2-3 concepts, 2-3 exercices de difficulté croissante
- **2+ heures** : Concepts multiples, exercices, projet/capstone

**Pour différents sujets** :

- Remplacez [TOPIC] par une compétence spécifique (par ex., « Conception API REST »)
- Remplacez [LEVEL] par difficulté (par ex., « Intermédiaire »)
- Remplacez [DURATION] par estimation de temps (par ex., « 1 heure »)

---

## Liste de contrôle qualité

Avant de soumettre, vérifiez :

### Qualité du contenu

- [ ] Le cours enseigne un concept clair et unique (pas plusieurs sujets sans rapport)
- [ ] Les objectifs d'apprentissage sont spécifiques et réalisables
- [ ] Le contenu traite directement de chaque objectif d'apprentissage
- [ ] Les exemples sont pertinents pour le sujet et le public cible
- [ ] Les exercices renforcent les objectifs d'apprentissage
- [ ] Pas d'information obsolète ou d'outils dépréciés

### Exhaustivité

- [ ] Toutes les sections requises sont présentes
- [ ] Pas de texte d'espace réservé restant (par ex., « [VOTRE SUJET ICI] »)
- [ ] Tous les liens sont corrects et actifs
- [ ] Les exemples de code sont syntaxiquement corrects
- [ ] La mise en forme est cohérente dans tout le document

### Accessibilité

- [ ] Le langage est clair et évite le jargon (ou l'explique)
- [ ] Les concepts sont expliqués avant utilisation
- [ ] Les exemples construisent du simple au complexe
- [ ] Les cours prérequis suggérés sont exacts
- [ ] Le contenu est approprié pour le niveau de difficulté déclaré

### Technique

- [ ] La syntaxe Markdown est valide
- [ ] Le préambule YAML est correctement formaté
- [ ] Le fichier est au bon endroit : `docs/lessons/[subject]/`
- [ ] Le nommage du fichier suit la convention : `lesson-[id]-[slug].md`
- [ ] Les champs de métadonnées sont complets et valides

---

## Soumission et révision

### Que se passe-t-il après la soumission?

1. **Vérifications automatisées** (5-10 minutes)
   - GitHub Actions valide la syntaxe Markdown
   - Vérifie les champs de métadonnées requis
   - Vérifie le nommage et l'emplacement du fichier
   - Le statut apparaît dans la RP sous forme de coche ou ✗
2. **Révision du responsable** (24-48 heures)
   - Les relecteurs lisent votre cours
   - Vérifiez l'exactitude et la qualité
   - Vérifiez l'alignement avec le style du référentiel
   - Peuvent demander des modifications (c'est normal!)
3. **Commentaires et itération** (selon les besoins)
   - Répondez aux commentaires des relecteurs
   - Effectuez les modifications demandées
   - Poussez les mises à jour vers votre branche (la RP se met à jour automatiquement)
   - Les relecteurs revérifient
4. **Approbation et fusion** (24 heures après approbation)
   - Le cours est fusionné dans la branche principale
   - GitHub Actions construit et déploie le site
   - Votre cours est en direct sur GitHub Pages!

### Commentaires courants

**« Veuillez ajouter un exercice »** → Ajoutez 2-3 exercices pratiquant les concepts clés  
**« Cela suppose trop de connaissances antérieures »** → Ajoutez une explication ou un lien vers un prérequis  
**« L'exemple de code ne fonctionne pas »** → Testez et corrigez le code  
**« Métadonnées incomplètes »** → Ajoutez les champs manquants du modèle  
**« Le ton ne correspond pas au public »** → Simplifiez ou approfondissez selon le niveau

---

## FAQ

### Q : Puis-je utiliser un LLM pour générer l'ensemble du cours?
**R** : Oui! Utilisez le modèle LLM pour inviter ChatGPT, Claude, etc. Vérifiez toujours le contenu généré pour l'exactitude avant submission. Vous n'avez pas besoin de rédiger le contenu à partir de zéro.

### Q : Que faire si mon cours couvre plusieurs sujets?
**R** : Placez-le dans le sujet principal et mentionnez les sujets connexes dans la section « Prochaines étapes ». Nous pouvons ajouter des références croisées dans les futures mises à jour.

### Q : Quelle longueur devrait avoir un cours?
**R** : Visez 30 minutes à 2 heures de contenu. S'il devient plus long, envisagez de le diviser en plusieurs cours.

### Q : Puis-je utiliser des liens externes et des ressources?
**R** : Oui, mais vérifiez qu'ils fonctionnent avant submittre. Liez vers des sources faisant autorité (docs, guides officiels, contenu révisé par les pairs).

### Q : Que faire si je veux mettre à jour un cours après sa publication?
**R** : Soumettez une RP avec les modifications. Les responsables vérifieront et fusionneront. Le site se met à jour automatiquement.

### Q : Puis-je supprimer un cours?
**R** : Au lieu de supprimer, définissez `status: "archived"` afin qu'il soit masqué mais conservé dans le contrôle de version.

### Q : Que faire si je ne connais pas Git/GitHub?
**R** : GitHub a d'excellents tutoriels. Alternativement, envoyez votre cours par e-mail aux responsables et ils le soumettront pour vous.

### Q : Combien de cours puis-je soumettre?
**R** : Autant que vous le souhaitez! Un à la fois ou par lot. Chacun passe par le processus d'examen.

### Q : Puis-je réutiliser le contenu de mon blog/cours?
**R** : Oui, si vous possédez le contenu ou avez la permission. Fournissez la source originale dans le champ auteur (par ex., « Adapté de mon cours sur X »).

---

## Prochaines étapes

1. **Vérifiez la [Spécification des métadonnées](metadata-reference.md)** pour les détails des champs
2. **Choisissez votre approche** : Rédiger le contenu ou générer avec LLM
3. **Créez votre cours** en utilisant les étapes ci-dessus
4. **Soumettez en tant que demande de fusion** et attendez la révision
5. **Célébrez!** Votre cours fait maintenant partie du référentiel

Avez-vous des questions? Ouvrez un problème sur GitHub ou envoyez un e-mail aux responsables.
