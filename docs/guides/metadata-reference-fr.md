# Spécification des Métadonnées: En-tête YAML

**Objectif**: Définir les champs de métadonnées requis et optionnels pour toutes les leçons  
**Format**: En-tête YAML au début de chaque fichier Markdown de leçon  
**Emplacement**: Premières lignes de `docs/lessons/[sujet]/lesson-*.md`

---

## Structure de l'En-tête

Toutes les leçons DOIVENT inclure un bloc en-tête YAML au début, entouré de marqueurs `---`:

```yaml
---
title: "string"
description: "string"
difficulty: "enum"
duration: "string"
tags: [list]
learning_objectives: [list]
prerequisites: [list, optional]
created: "YYYY-MM-DD"
author: "string, optional"
updated: "YYYY-MM-DD, optional"
status: "enum, optional"
---
```

---

## Champs Obligatoires

### `title`
- **Type**: Chaîne de caractères
- **Obligatoire**: Oui
- **Description**: Le nom d'affichage de la leçon
- **Contraintes**:
  - Non vide
  - 3 à 100 caractères
  - Doit être descriptif et orienté vers l'action
  - Unique dans le sujet (recommandé)
- **Exemple**: `"Introduction aux Fonctions Python"`

### `description`
- **Type**: Chaîne de caractères
- **Obligatoire**: Oui
- **Description**: Résumé d'une phrase de la leçon
- **Contraintes**:
  - Non vide
  - 10 à 200 caractères
  - Une seule phrase (sans point implicite)
  - Décrit le résultat, pas le processus
- **Exemple**: `"Apprenez à définir, appeler et utiliser des fonctions pour organiser votre code"`

### `difficulty`
- **Type**: Enum
- **Obligatoire**: Oui
- **Description**: Niveau du public cible
- **Valeurs Autorisées**:
  - `"Beginner"`: Aucune connaissance préalable supposée
  - `"Intermediate"`: Compréhension de base requise
  - `"Advanced"`: Base solide requise
- **Exemple**: `difficulty: "Beginner"`

### `duration`
- **Type**: Chaîne de caractères
- **Obligatoire**: Oui
- **Description**: Temps estimé pour compléter la leçon
- **Contraintes**:
  - Doit inclure une valeur numérique et une unité
  - Unités: minutes, heures, jours
  - Estimation réaliste (tient compte des exercices)
- **Exemples Valides**:
  - `"30 minutes"`
  - `"1 heure"`
  - `"2 heures 30 minutes"`
  - `"1 jour"`

### `tags`
- **Type**: Liste de chaînes
- **Obligatoire**: Oui
- **Description**: Étiquettes catégoriques pour la découverte
- **Contraintes**:
  - 1 à 5 tags par leçon
  - Lettres minuscules, chiffres, tirets uniquement
  - Pas d'espaces
  - Significatif et réutilisable
  - Exemples: `api`, `async`, `authentication`, `backend`, `rest`
- **Exemple**: 
  ```yaml
  tags: [functions, python, code-organization, variables]
  ```

### `learning_objectives`
- **Type**: Liste de chaînes
- **Obligatoire**: Oui
- **Description**: Ce que les apprenants pourront faire
- **Contraintes**:
  - 3 à 5 objectifs
  - Commencez par un verbe d'action (comprendre, créer, appliquer, analyser, etc.)
  - Spécifique et mesurable
  - Réalisable dans la durée
- **Exemple**:
  ```yaml
  learning_objectives:
    - "Définir et appeler une fonction"
    - "Utiliser les paramètres et les valeurs de retour"
    - "Appliquer les fonctions pour organiser votre code"
  ```

### `created`
- **Type**: Date (ISO 8601)
- **Obligatoire**: Oui
- **Description**: Date de création de la leçon
- **Format**: `YYYY-MM-DD`
- **Exemple**: `created: 2026-01-30`

---

## Champs Optionnels

### `prerequisites`
- **Type**: Liste de chaînes (IDs de leçon)
- **Obligatoire**: Non
- **Description**: Leçons qui doivent être complétées en premier
- **Contraintes**:
  - 0 à 3 prérequis recommandés
  - Référencer les IDs de leçon valides
  - Peut être du même sujet ou d'un sujet différent
- **Exemple**:
  ```yaml
  prerequisites: [lesson-001-intro, lesson-002-basics]
  ```

### `author`
- **Type**: Chaîne de caractères
- **Obligatoire**: Non
- **Description**: Qui a créé ou contribué significativement
- **Contraintes**:
  - Nom ou identifiant (par exemple, "Jean Dupont", "Assistant LLM", "Claude 3.5")
  - S'il est omis, il revient par défaut aux mainteneurs du référentiel
- **Exemple**: `author: "Claude 3.5 (avec révision humaine)"`

### `updated`
- **Type**: Date (ISO 8601)
- **Obligatoire**: Non
- **Description**: Date de dernière modification
- **Format**: `YYYY-MM-DD`
- **Exemple**: `updated: 2026-02-15`
- **Note**: Mise à jour automatique par les mainteneurs; les auteurs n'ont pas besoin de le définir

### `status`
- **Type**: Enum
- **Obligatoire**: Non
- **Par Défaut**: `"published"`
- **Description**: Statut de publication de la leçon
- **Valeurs Autorisées**:
  - `"draft"`: Non prêt pour les apprenants; visible uniquement pour les mainteneurs
  - `"published"`: Prêt pour les apprenants; visible dans toutes les interfaces
  - `"archived"`: Pas plus maintenu; caché de la recherche/navigation
- **Exemple**: `status: "published"`

---

## Exemple d'En-tête Complet

```yaml
---
title: "Méthodes Avancées des Tableaux en JavaScript"
description: "Maîtrisez les méthodes de tableau comme map, filter et reduce pour écrire du JavaScript fonctionnel"
difficulty: "Intermediate"
duration: "1 heure 15 minutes"
tags: [javascript, functional-programming, arrays, es6]
learning_objectives:
  - "Comprendre les concepts de programmation fonctionnelle"
  - "Utiliser efficacement map, filter et reduce"
  - "Chaîner les méthodes de tableau pour des transformations complexes"
prerequisites: [lesson-001-array-basics, lesson-002-es6-intro]
created: 2026-01-30
author: "Assistant LLM (ChatGPT-4)"
updated: 2026-02-10
status: "published"
---
```

---

## Règles de Validation

### Complétude des Métadonnées
- [ ] Tous les champs obligatoires présents: titre, description, difficulté, durée, tags, learning_objectives, created
- [ ] Aucun champ vide (sauf les champs optionnels)
- [ ] La syntaxe YAML est valide (pas d'erreurs de syntaxe)

### Validation des Valeurs de Champ

| Champ | Règle | Message d'Erreur |
|-------|-------|-----------------|
| `title` | Non vide, 3-100 caractères | "Le titre doit être entre 3 et 100 caractères" |
| `description` | Non vide, 10-200 caractères | "La description doit être entre 10 et 200 caractères" |
| `difficulty` | Une de: Beginner, Intermediate, Advanced | "La difficulté doit être Beginner, Intermediate ou Advanced" |
| `duration` | Contient nombre + unité (minutes, heures, jours) | "La durée doit inclure un nombre et une unité (ex. '30 minutes')" |
| `tags` | 1-5 éléments, minuscules, avec tirets | "Les tags doivent être 1-5 éléments, minuscules, avec tirets" |
| `learning_objectives` | 3-5 éléments, non vides | "Doit avoir 3-5 objectifs d'apprentissage" |
| `created` | Format YYYY-MM-DD | "La date de création doit être YYYY-MM-DD" |
| `difficulty` | Une de: Beginner, Intermediate, Advanced | "La difficulté doit être Beginner, Intermediate ou Advanced" |
| `status` | Une de: draft, published, archived | "Le statut doit être draft, published ou archived" |

---

## Intégration Recherche et Filtrage

### Par Tag
Les tags de métadonnées sont utilisés par l'interface de recherche/filtrage pour trouver les leçons:
```
L'utilisateur sélectionne le tag: "api"
→ Le système trouve toutes les leçons où tags contient "api"
→ Retourne les leçons correspondantes dans tous les sujets
```

### Par Difficulté
La difficulté des métadonnées permet un filtrage par niveau:
```
Filtre: Difficulté = "Intermediate"
→ Le système retourne toutes les leçons Intermediate
→ Les utilisateurs peuvent affiner par sujet + difficulté
```

### Par Durée
La durée des métadonnées aide les utilisateurs à trouver les leçons dont ils ont le temps:
```
L'utilisateur cherche: "leçons de moins d'1 heure"
→ Le système analyse le champ durée
→ Retourne les leçons où durée < 60 minutes
```

### Chaîne de Prérequis
Les prérequis des métadonnées permettent une visualisation des dépendances:
```
Leçon A → [prérequis: Leçon B]
Leçon B → [prérequis: Leçon C]
→ Le système affiche "Prérequis: Leçon B → Leçon C"
→ Les liens aident les apprenants à commencer au bon niveau
```

---

## Exemples par Contexte

### Leçon Générée par LLM
```yaml
---
title: "Comprehensions de Listes Python Expliquées"
description: "Apprenez à écrire des listes concises et lisibles en utilisant la syntaxe de compréhension de liste de Python"
difficulty: "Intermediate"
duration: "45 minutes"
tags: [python, lists, functional-programming, syntax]
learning_objectives:
  - "Comprendre la syntaxe de compréhension de liste"
  - "Convertir les boucles en compréhensions de liste"
  - "Utiliser les conditionnels dans les compréhensions de liste"
created: 2026-01-30
author: "Claude 3.5 (avec révision humaine)"
status: "published"
---
```

### Leçon Débutant
```yaml
---
title: "Débuter avec HTML"
description: "Créez votre première page web en utilisant les éléments HTML et la structure"
difficulty: "Beginner"
duration: "30 minutes"
tags: [html, web, markup, basics]
learning_objectives:
  - "Créer un document HTML valide"
  - "Utiliser les éléments HTML courants"
  - "Comprendre la structure des documents HTML"
created: 2026-01-28
author: "Sarah Chen"
status: "published"
---
```

### Leçon Avancée avec Prérequis
```yaml
---
title: "Concevoir une Architecture Microservices"
description: "Planifiez et concevez des systèmes microservices évolutifs pour les applications complexes"
difficulty: "Advanced"
duration: "3 heures"
tags: [architecture, microservices, system-design, distributed-systems]
learning_objectives:
  - "Évaluer quand les microservices sont appropriés"
  - "Concevoir les limites et les contrats des services"
  - "Prévoir la résilience et l'observabilité"
prerequisites: [lesson-005-apis, lesson-008-databases]
created: 2026-01-25
author: "Équipe DevOps"
status: "published"
---
```

---

## Voir aussi

- [Modèle de Leçon](../templates/lesson-template.md) - Structure de leçon complète
- [Guide du Flux de Travail](workflow-create-lesson.md) - Guide étape par étape de création
- [Guide de Démarrage Rapide](quick-start.md) - Intégration 10 minutes
