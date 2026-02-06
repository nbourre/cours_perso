# Guide de démarrage rapide : Système de gestion des cours

**Objectif** : Se familiariser avec les cours et la création de contenu en 10 minutes  
**Public** : Nouveaux utilisateurs, éducateurs, créateurs de contenu

---

## 1. Parcourir les cours existants (2 minutes)

1. **Visitez le site de documentation** → URL GitHub Pages
2. **Cliquez sur un sujet** depuis la page d'accueil (par ex., « Python », « Développement Web »)
3. **Consultez les cours de ce sujet** avec le niveau de difficulté, la durée et les étiquettes
4. **Cliquez sur un cours** pour lire et apprendre
5. **Recherchez par étiquettes** en utilisant la fonction de filtrage/recherche (à venir)

---

## 2. Comprendre la structure d'un cours (2 minutes)

Chaque cours contient :

```markdown
---
title: "Titre du cours"
description: "Ce que vous apprendrez"
difficulty: "Beginner | Intermediate | Advanced"
duration: "30 minutes à 2 heures"
tags: [étiquette1, étiquette2, étiquette3]
learning_objectives: [objectif1, objectif2, objectif3]
---

# Titre du cours

## Objectifs d'apprentissage
- Ce que vous serez capable de faire

## Introduction
- Pourquoi c'est important

## Sections de contenu principal
- Concepts fondamentaux avec exemples

## Exercices
- Tâches pratiques

## Évaluation
- Questions d'auto-vérification

## Résumé et prochaines étapes
- Récapitulatif et suite
```

---

## 3. Créer votre premier cours (5 minutes)

### Méthode A : Entrée manuelle rapide

1. **Téléchargez le modèle** : Copiez [lesson-template.md](../templates/lesson-template.md)
2. **Remplissez les métadonnées** en haut :
   - Titre, description, difficulté, durée, étiquettes, objectifs d'apprentissage
3. **Rédigez le contenu** dans les sections fournies
4. **Enregistrez sous** : `docs/lessons/[subject]/lesson-[id]-[slug].md`
5. **Soumettez via GitHub** (créez une demande de fusion)

### Méthode B : Générer avec LLM (Recommandé)

1. **Copiez le modèle de prompt LLM** → Collez dans ChatGPT/Claude/etc.
2. **Personnalisez le prompt** :
   - Remplacez `[TOPIC]` par le sujet de votre cours
   - Remplacez `[LEVEL]` par la difficulté (Beginner/Intermediate/Advanced)
   - Remplacez `[DURATION]` par l'estimation de temps (par ex., « 1 heure »)
3. **Soumettez le prompt** à votre LLM
4. **Copiez la réponse** (cours entièrement généré)
5. **Collez dans un fichier** : `lesson-[id]-[slug].md`
6. **Vérifiez la précision** (corrigez les erreurs ou sections peu claires)
7. **Soumettez via GitHub** (créez une demande de fusion)

---

## 4. Soumettre votre cours au référentiel (3 minutes)

1. **Bifurquez le référentiel** sur GitHub (si c'est la première fois)
2. **Créez une nouvelle branche** : `git checkout -b add-lesson-votre-sujet`
3. **Ajoutez votre fichier** : `git add docs/lessons/[subject]/lesson-*.md`
4. **Validez** : `git commit -m "Add lesson: Titre de votre cours"`
5. **Poussez** : `git push origin add-lesson-votre-sujet`
6. **Créez une demande de fusion** sur GitHub avec description
7. **Attendez la révision** (généralement 24-48 heures)
8. **Terminé !** Votre cours est publié après la fusion

---

## 5. Fichiers clés et liens

| Quoi | Où | Lien |
|------|-----|------|
| **Créer un cours** | Guide de flux complet | [Guide de flux de cours](workflow-create-lesson.md) |
| **Structure du cours** | Modèle | [lesson-template.md](../templates/lesson-template.md) |
| **Champs de métadonnées** | Spécification | [Référence des métadonnées](metadata-reference.md) |
| **Modèle LLM** | Dans le dossier modèles | `docs/templates/llm-prompt-template.txt` |

---

## 6. Catégories de sujets

Sujets par défaut disponibles :

- 📘 **Bases de Python** → Concepts fondamentaux Python, syntaxe, bibliothèques
- 🌐 **Développement Web** → HTML, CSS, JavaScript, frameworks
- 📊 **Science des données** → Analytics, visualisation, apprentissage automatique

**Besoin d'un nouveau sujet ?** Mentionnez-le dans la description de votre demande de fusion. Les responsables créeront la catégorie.

---

## 7. Étiquettes (Pour l'organisation)

Utilisez les étiquettes pour rendre les cours découvrables entre les sujets. Exemples :

- **Technologie** : `python`, `javascript`, `database`, `api`
- **Concept** : `functions`, `loops`, `async`, `authentication`
- **Difficulté** : `beginner-friendly`, `intermediate`, `advanced`
- **Domaine** : `web`, `data`, `systems`, `security`

**Choisissez 1-5 étiquettes par cours** qui aident les apprenants à trouver du contenu connexe.

---

## 8. Feuille de triche des métadonnées

Requis pour chaque cours :

| Champ | Exemple | Notes |
|-------|---------|-------|
| `title` | « Fonctions Python 101 » | 3-100 caractères, titre clair |
| `description` | « Apprenez à écrire des fonctions réutilisables » | 1 phrase, non-technique |
| `difficulty` | « Beginner » | Un seul parmi : Beginner, Intermediate, Advanced |
| `duration` | « 45 minutes » | Inclure l'unité (minutes/heures/jours) |
| `tags` | [python, functions, reuse] | 1-5 éléments, minuscules, avec tirets |
| `learning_objectives` | Voir modèle | 3-5 résultats spécifiques |
| `created` | 2026-01-30 | Format AAAA-MM-JJ |

Optionnel :

| Champ | Exemple |
|-------|---------|
| `author` | « Claude 3.5 » ou « Jane Smith » |
| `prerequisites` | [lesson-001-intro] |

---

## Questions fréquemment posées

**Q : Est-ce gratuit?**  
Oui, tous les cours sont gratuits et open source.

**Q : Puis-je utiliser le contenu d'autres sources?**  
Oui, avec attribution. Assurez-vous d'avoir les droits d'utilisation.

**Q : Combien de temps faut-il pour créer un cours?**  
Environ 2-4 heures selon la complexité.

**Q : Puis-je éditer un cours après publication?**  
Oui, soumettez une nouvelle demande de fusion avec les modifications.

**Q : Comment demander une nouvelle catégorie de sujet?**  
Mentionnez-le dans la description de votre demande de fusion ou créez un problème GitHub.

---

**Prêt à créer votre premier cours ?** Consultez le [Guide complet de création de cours](workflow-create-lesson.md) ! 🚀
