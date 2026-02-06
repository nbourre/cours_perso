# Utilisation des modèles LLM pour la génération de cours

**Objectif** : Apprenez à utiliser les assistants IA pour générer efficacement du contenu de cours de haute qualité  
**Public** : Créateurs de contenu qui souhaitent utiliser ChatGPT, Claude ou d'autres LLM  
**Temps** : 15-30 minutes du prompt au cours publiable

---

## Vue d'ensemble

Au lieu de rédiger des cours à partir de zéro, vous pouvez utiliser des modèles de langage volumineux (LLM) tels que ChatGPT, Claude ou Gemini pour générer du contenu de cours qui suit notre modèle. Ce guide vous montre comment obtenir les meilleurs résultats.

**Avantages clés** :
- ✅ Générez des cours complets en 15-30 minutes
- ✅ Structure cohérente à chaque fois
- ✅ Le LLM gère les parties répétitives (exemples, exercices)
- ✅ Vous vous concentrez sur l'examen et l'affinement
- ✅ Aucun codage requis

---

## Démarrage rapide : Exemple de 5 minutes

### Étape 1 : Préparez votre sujet
```
Sujet : « Fonctions Python pour débutants »
Niveau : Débutant
Durée : 45 minutes
LLM préféré : ChatGPT 4
```

### Étape 2 : Copiez le modèle de prompt LLM
Voir [Guide de flux de travail - Utilisation du modèle LLM](workflow-create-lesson-fr.md#utilisation-du-modèle-llm) pour le modèle complet.

### Étape 3 : Personnalisez et collez
Remplacez les espaces réservés :
- [TOPIC] → « Fonctions Python »
- [LEVEL] → « Débutant »
- [DURATION] → « 45 minutes »

### Étape 4 : Exécutez dans votre LLM
- ChatGPT : Collez dans le chat
- Claude : Collez dans une nouvelle conversation
- Gemini : Collez dans composer

### Étape 5 : Vérifiez la sortie
- Lisez pour vérifier la précision
- Vérifiez que les exemples fonctionnent
- Vérifiez que les exercices sont clairs
- Corrigez les problèmes

### Étape 6 : Enregistrez et soumettez
Enregistrez sous `lesson-001-python-functions.md` et soumettez via RP.

---

## Flux de travail détaillé

### 1. Choisissez votre LLM

**ChatGPT (GPT-4)** :
- Avantages : Rapide, créatif, bon pour les explications
- Inconvénients : Nécessite un compte payant
- Meilleur pour : Contenu narratif, exemples

**Claude (Sonnet 3)** :
- Avantages : Contexte long, précis, gère bien les codes
- Inconvénients : Nécessite un compte
- Meilleur pour : Exemples de code, précision technique

**Gemini (Google)** :
- Avantages : Option gratuite, s'intègre avec les docs Google
- Inconvénients : La qualité peut varier
- Meilleur pour : Génération rapide, brouillons

**LLM locaux** (Ollama, LLaMA) :
- Avantages : Gratuit, privé, rapide
- Inconvénients : Peut nécessiter des ajustements
- Meilleur pour : Génération de brouillon, tests

**Recommandation** : Commencez avec ChatGPT 4 ou Claude pour les meilleurs résultats.

---

### 2. Préparez votre fiche de cours

Avant d'utiliser le modèle, rassemblez ces détails :

**Détails du sujet** :
- [ ] Nom de sujet spécifique (pas trop large, pas trop étroit)
- [ ] Exemple : « Compréhensions de liste Python » (bon) vs. « Python » (trop large)

**Public cible** :
- [ ] Difficulté : Débutant, Intermédiaire ou Avancé
- [ ] Savoir antérieur supposé
- [ ] Exemple : « Apprenants Python débutants qui connaissent les boucles et les listes »

**Contrainte de temps** :
- [ ] Durée : 30 min, 45 min, 1 heure, 1,5 heure, 2 heures
- [ ] Inclut les exercices et l'auto-évaluation
- [ ] Exemple : « 1 heure y compris les exercices »

**Catégorie de sujet** :
- [ ] Quel sujet : Python, Développement Web, Science des données, etc.
- [ ] Exemple : « Bases de Python »

**Étiquettes** (optionnel, vous pouvez ajouter plus tard) :
- [ ] 3-5 mots-clés pour la découverte
- [ ] Exemple : [python, lists, functional-programming, syntax]

---

### 3. Utilisez le modèle de prompt LLM

### Format : Prompt structuré avec exigences claires

```
Créez un cours éducatif sur [TOPIC] pour les apprenants [LEVEL].
Le cours devrait prendre environ [DURATION] pour être complété.

Utilisez cette structure Markdown exacte :

[MODÈLE COMPLET ICI]

Exigences importantes :
- Les explications doivent être claires et accessibles pour les apprenants [LEVEL]
- Incluez au moins 2-3 exemples pratiques avec code ou procédures
- Rendez les exercices progressifs (facile → difficile)
- Assurez-vous que le cours est réalisable en [DURATION]
- Utilisez un langage simple ; expliquez les termes techniques
- Le contenu doit être prêt à être collé directement dans un fichier Markdown
```

### Exemple : Prompt réel

```
Créez un cours éducatif sur « React Hooks » pour les apprenants Débutant
qui connaissent déjà les composants et l'état React.
Le cours devrait prendre environ 1 heure pour être complété.

Utilisez cette structure Markdown exacte :

---
title: « Maîtriser Async/Await en JavaScript »
description: « Apprenez à écrire du JavaScript asynchrone propre en utilisant la syntaxe async/await »
difficulty: « Intermediate »
duration: « 1 heure »
tags: [javascript, async, promises, es2017]
learning_objectives:
  - « Comprendre comment fonctionne async/await »
  - « Convertir les Promises en async/await »
  - « Gérer les erreurs dans les fonctions asynchrones »
created: 2026-01-30
author: « Assistant LLM »
status: « published »
---

# Maîtriser Async/Await en JavaScript

[... reste du modèle ...]

Exigences importantes :
- Les explications doivent être claires pour les apprenants Intermédiaires
- Incluez 2-3 exemples pratiques avec du code exécutable
- Rendez les exercices progressifs (facile → difficile)
- Assurez-vous que c'est réalisable en 1 heure
- Utilisez un langage simple
- Le contenu doit être prêt à être collé dans Markdown
```

---

### 4. Vérifiez le contenu généré

Après que le LLM génère le cours, vérifiez attentivement :

**Vérification de l'exactitude** :
- [ ] Les exemples de code sont-ils corrects et exécutables?
- [ ] Les explications sont-elles exactes pour le sujet?
- [ ] Y a-t-il des concepts obsolètes ou dépréciés?
- [ ] Les prérequis ont-ils du sens?

**Vérification de la structure** :
- [ ] Toutes les sections sont présentes (objectifs, introduction, concepts, exercices, évaluation)?
- [ ] La mise en forme Markdown est correcte?
- [ ] Les métadonnées YAML sont valides?
- [ ] Les objectifs d'apprentissage sont-ils traités dans le contenu?

**Vérification de la qualité du contenu** :
- [ ] Les explications sont-elles claires pour le public cible?
- [ ] Les exemples sont-ils pertinents et utiles?
- [ ] Les exercices sont-ils progressivement plus difficiles?
- [ ] L'évaluation vérifie-t-elle la compréhension?

**Verifi cation de l'exhaustivité** :
- [ ] Cours réalisable dans la durée indiquée?
- [ ] Aucun texte d'espace réservé restant?
- [ ] Les liens sont-ils au format Markdown approprié?

---

### 5. Edits communs nécessaires

### Après la génération, vous devrez peut-être :

**Corriger les exemples de code** :
```
❌ Original (peut avoir des erreurs) :
def process(data):
    return data.filter(x -> x > 0)

✅ Corrigé :
def process(data):
    return [x for x in data if x > 0]
```

**Clarifier les explications** :
```
❌ Trop technique :
« Exploiter les paradigmes fonctionnels permet de tirer parti des motifs de composition »

✅ Clair :
« Utiliser des fonctions comme valeurs vous permet de combiner des fonctions plus simples en d'autres plus complexes »
```

**Rendre les exemples exécutables** :
```
❌ Pseudo-code :
response = call API

✅ Code réel :
import requests
response = requests.get('https://api.example.com/data')
```

**Corriger les problèmes de mise en forme** :
- Lignes vides supplémentaires
- Indentation incohérente
- Niveaux de titre incorrects
- Marqueurs de bloc de code manquants

---

### 6. Ajoutez une touche personnelle

Après la génération LLM, considérez :

**Ajoutez votre expertise** :
- Corrigez les erreurs spécifiques au sujet
- Ajoutez vos propres exemples s'ils sont plus pertinents
- Ajustez le ton à votre style
- Ajoutez des mises en garde ou des conseils tirés de l'expérience

**Ajoutez du contexte local** :
- Liez aux normes de votre organisation
- Référencez les outils ou systèmes locaux
- Ajoutez des exemples spécifiques à l'entreprise
- Liez vers les ressources internes

**Ajoutez de l'interactivité** (si la plateforme le supporte) :
- Exemples de code interactifs
- Vidéos intégrées
- Questions de discussion
- Défis avec indices

---

## Conseils pour les meilleurs résultats

### Choisissez des sujets spécifiques

**Bons sujets** :
- « Compréhensions de liste Python » ✅
- « Construire des API REST avec Flask » ✅
- « Layout CSS Grid » ✅
- « Nettoyage de données avec Pandas » ✅

**Trop large** :
- « Python » ❌
- « Développement Web » ❌
- « JavaScript » ❌

### Soyez explicite sur le niveau

**Débutant** :
- Aucune hypothèse sur les connaissances antérieures
- Expliquez les concepts de base
- Utilisez des analogies
- Exemples simples et concrets

**Intermédiaire** :
- Supposez une compréhension de base
- Concentrez-vous sur l'application
- Inclure les meilleures pratiques
- Montrez les motifs courants

**Avancé** :
- Supposez une base solide
- Plongée technique approfondie
- Discutez des cas limites
- Inclure l'optimisation

### Faire correspondre la durée au contenu

**30 minutes** : 1 concept, 2 exercices simples  
**45 minutes** : 1-2 concepts, 2-3 exercices  
**1 heure** : 2-3 concepts, 2-3 exercices  
**2+ heures** : 4+ concepts, projet/capstone

---

## Dépannage de la sortie LLM

### Problème : Le contenu généré est trop simple
**Solution** : Demandez « pour les développeurs expérimentés » ou « techniques avancées »

### Problème : Les exemples de code ne fonctionnent pas
**Solution** : Testez-les vous-même, puis donnez un retour : « Cette syntaxe est incorrecte pour Python 3.9+ »

### Problème : Le contenu est trop long pour la durée
**Solution** : Demandez au LLM de « se concentrer sur les concepts fondamentaux et d'omettre les sujets avancés »

### Problème : Trop de sections d'espace réservé
**Solution** : Régénérez avec un prompt plus spécifique : « Incluez des exemples spécifiques de [X] »

### Problème : Ne correspond pas à votre style d'enseignement
**Solution** : C'est normal! Éditez pour correspondre à votre voix et à votre approche

---

## Exemple : Flux de travail complet

### Entrée
```
Sujet : Hooks React pour débutants
Niveau : Débutant (connaît les bases de React)
Durée : 1 heure
```

### Prompt LLM
```
Créez un cours éducatif sur « React Hooks » pour les développeurs React Débutant
qui connaissent déjà les composants et l'état.
Le cours devrait prendre environ 1 heure pour être complété.

[Modèle complet fourni]

Exigences importantes :
- Expliquez ce que sont les Hooks pour les débutants
- Incluez 3-4 exemples pratiques avec code complet
- Exercices progressifs des hooks de base à la combinaison des hooks
- Langage accessible, expliquez tous les termes techniques
```

### Vérification et édition
1. ✅ La structure du contenu est correcte
2. ❌ L'exemple de code pour useState a une erreur de syntaxe → Corriger
3. ❌ L'exercice 3 suppose la connaissance de useContext → Ajouter l'explication du contexte
4. ✅ Les métadonnées sont complètes
5. ✅ Durée réaliste

### Résultat final
Cours prêt à la publication en ~30 minutes (10 min prompt + 10 min génération + 10 min révision/édition)

---

## Liste de contrôle qualité pour le contenu LLM

Avant de soumettre un cours généré par LLM :

### Précision du contenu
- [ ] Tous les exemples de code sont corrects
- [ ] Les explications sont exactes
- [ ] Pas de motifs dépréciés utilisés
- [ ] Les liens vers la docs sont à jour

### Exhaustivité
- [ ] Toutes les sections requises présentes
- [ ] Pas de texte d'espace réservé
- [ ] Les objectifs d'apprentissage correspondent au contenu
- [ ] Les questions d'évaluation testent tous les objectifs

### Clarté
- [ ] Les explications utilisent un langage simple
- [ ] Les exemples démontrent clairement les concepts
- [ ] Le jargon est expliqué
- [ ] Le contenu est approprié pour le niveau de difficulté

### Structure
- [ ] Markdown est correctement formaté
- [ ] Les métadonnées YAML sont valides
- [ ] Le nommage du fichier suit la convention
- [ ] Le fichier est dans le bon répertoire

### Technique
- [ ] Les extraits de code sont syntaxiquement corrects
- [ ] Le code est exécutable (testé si possible)
- [ ] Les exemples suivent les meilleures pratiques
- [ ] Pas de liens cassés

---

## Voir aussi

- [Guide de flux de création de cours](workflow-create-lesson-fr.md) - Guide de création complet
- [Référence des métadonnées](metadata-reference-fr.md) - Spécifications des champs
- [Modèle de cours](../templates/lesson-template-fr.md) - Structure du modèle
- [Guide de démarrage rapide](quick-start-fr.md) - Vue d'ensemble de 10 minutes

---

## Prochaines étapes

1. **Choisissez votre LLM** (ChatGPT, Claude, Gemini, etc.)
2. **Préparez votre fiche de cours** (sujet, niveau, durée)
3. **Copiez le modèle de prompt** du [Guide de flux de travail](workflow-create-lesson-fr.md#utilisation-du-modèle-llm)
4. **Générez votre cours** (10-15 minutes)
5. **Vérifiez et éditez** (10-15 minutes)
6. **Soumettez en tant que demande de fusion** → Publié!

Prêt à créer votre premier cours? 🚀
