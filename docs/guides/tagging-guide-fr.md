# Guide de Marquage: Organisez les Leçons pour la Découverte

**Objectif**: Apprenez à utiliser les tags efficacement pour rendre les leçons découvrables  
**Public**: Créateurs de contenu, auteurs de leçons  
**But**: Aider les apprenants à trouver les leçons par le biais de la recherche basée sur les tags entre sujets

---

## Qu'est-ce que les Tags?

Les tags sont 1-5 mots-clés attachés à chaque leçon qui décrivent son contenu et la rendent découvrable. Contrairement au Sujet (Python, Développement Web, etc.), les tags permettent la **découverte entre sujets**.

**Exemple**: Une leçon sur "Conception de Bases de Données" en Développement Web pourrait être marquée avec:
- `database` (les apprenants peuvent trouver toutes les leçons DB)
- `system-design` (les apprenants peuvent trouver les leçons d'architecture)
- `scalability` (les apprenants intéressés par la performance)
- `sql` (les apprenants cherchant les langages de base de données)
- `schema` (les apprenants concevant des structures de données)

---

## Catégories de Tags

### Tags Technologiques
Les outils, langages ou frameworks spécifiques:
- `python`, `javascript`, `java`, `golang`, `rust`
- `react`, `vue`, `angular`
- `postgresql`, `mongodb`, `redis`
- `docker`, `kubernetes`
- `git`, `github`, `gitlab`

### Tags de Concepts
Des idées abstraites et des modèles:
- `functions`, `loops`, `conditionals`
- `async`, `promises`, `callbacks`
- `authentication`, `authorization`
- `api`, `rest`, `graphql`
- `recursion`, `sorting`, `searching`

### Tags de Domaine
Des domaines d'application:
- `web`, `backend`, `frontend`
- `data-analysis`, `visualization`
- `machine-learning`, `ai`
- `devops`, `infrastructure`
- `security`, `cryptography`

### Indicateurs de Difficulté** (optionnel, aussi dans les métadonnées):
- `beginner-friendly`, `intermediate-focused`, `advanced-concepts`

### Tags Transversaux
Méta-informations:
- `performance`, `optimization`
- `testing`, `debugging`
- `documentation`
- `best-practices`

---

## Règles de Marquage

### 1. Utilisez 1-5 Tags par Leçon
- **Minimum**: 1 tag (bien que 3+ recommandé)
- **Maximum**: 5 tags (évitez la surcharge de tags)
- **Zone idéale**: 3-4 tags par leçon

### 2. Format Minuscules et Avec Tirets
Les tags doivent être:
- ✅ Minuscules: `python-basics`, pas `Python_Basics`
- ✅ Avec tirets: `rest-api`, pas `rest_api` ou `restapi`
- ✅ Pas d'espaces: `machine-learning`, pas `machine learning`
- ✅ Pas de caractères spéciaux: `async-await`, pas `async/await`

### 3. Soyez Spécifique, Pas Redondant

**Bon**:
```yaml
tags: [python, functions, scope]
```

**Évitez la Redondance**:
```yaml
tags: [python, python-functions, python-scope]  # Trop spécifique, chevauchement
```

**Trop Vague**:
```yaml
tags: [programming, learning]  # Pas utile pour la découverte
```

### 4. Pensez Comme un Apprenant

Posez-vous la question: "Qu'est-ce que je chercherais pour trouver cette leçon?"

**Exemple de leçon**: "Async/Await en JavaScript"

**Recherches des Apprenants**:
- "async" → Trouvé ✅
- "javascript" → Trouvé ✅
- "callbacks" → Manquant ❌ (ajouter le tag: `callbacks`)
- "promises" → Manquant ❌ (ajouter le tag: `promises`)

**Tags Meilleurs**: `[javascript, async, promises, callbacks, es6]`

---

## Marquage par Sujet

### Bases de Python
Tags courants pour les leçons Python:
- Langage: `python`, `python3`
- Concepts: `variables`, `functions`, `loops`, `classes`, `modules`
- Domaines: `data-science`, `web`, `scripting`
- Techniques: `debugging`, `testing`, `performance`

**Exemple de leçon**: "Fonctions Python"
```yaml
tags: [python, functions, code-organization, scope, parameters]
```

### Développement Web
Tags courants pour les leçons Web:
- Langages: `html`, `css`, `javascript`, `typescript`
- Frameworks: `react`, `vue`, `angular`, `nextjs`
- Concepts: `dom`, `async`, `api`, `rest`, `graphql`
- Architecture: `ssr`, `spa`, `pwa`

**Exemple de leçon**: "Construire des APIs REST avec Node.js"
```yaml
tags: [nodejs, api, rest, express, backend]
```

### Science des Données
Tags courants pour les leçons de Science des Données:
- Langages: `python`, `sql`, `r`
- Bibliothèques: `pandas`, `numpy`, `matplotlib`, `sklearn`
- Concepts: `data-cleaning`, `visualization`, `statistics`, `machine-learning`
- Domaines: `analytics`, `prediction`, `classification`

**Exemple de leçon**: "Visualisation de Données avec Matplotlib"
```yaml
tags: [python, matplotlib, data-visualization, pandas, analysis]
```

---

## Exemples de Sélection de Tags

### Cas 1: Comprehensions de Listes Python

**Sujet**: "Utilisez les compréhensions de liste pour écrire du code Python concis"

**Tags Potentiels**:
- `python` ✅ (technologie primaire)
- `list-comprehensions` ✅ (concept spécifique)
- `functional-programming` ✅ (paradigme de programmation)
- `syntax` ✅ (type d'apprentissage)
- `code-organization` ✅ (bénéfice)

**Tags Finaux**:
```yaml
tags: [python, list-comprehensions, functional-programming, syntax]
```

### Cas 2: Conception d'API REST

**Sujet**: "Concevez des APIs RESTful en suivant les meilleures pratiques"

**Tags Potentiels**:
- `api` ✅ (concept primaire)
- `rest` ✅ (architecture spécifique)
- `http` ✅ (protocole sous-jacent)
- `web` ✅ (domaine)
- `backend` ✅ (composant)
- `system-design` ✅ (catégorie)
- `best-practices` ✅ (meta-tag)

**Tags Finaux** (choisissez 5 max):
```yaml
tags: [api, rest, http, backend, system-design]
```

### Cas 3: Crochets React

**Sujet**: "Apprenez les Crochets React pour gérer l'état dans les composants fonctionnels"

**Tags Potentiels**:
- `react` ✅ (framework primaire)
- `javascript` ✅ (langage)
- `hooks` ✅ (fonctionnalité spécifique)
- `state-management` ✅ (concept)
- `frontend` ✅ (domaine)
- `es6` ✅ (version JavaScript)

**Tags Finaux**:
```yaml
tags: [react, javascript, hooks, state-management, frontend]
```

---

## Découverte de Tags: Comment les Apprenants Utilisent les Tags

### Parcourir par Tag (Fonctionnalité Future)

```
Accueil → Nuage de Tags
Cliquez sur "python" → Voir toutes les leçons Python
  ├── Leçon 1: "Fonctions Python"
  ├── Leçon 2: "Compréhensions de Listes"
  └── Leçon 3: "Classes et POO"
```

### Filtre Multi-Tags

```
Filtre: ["python", "async"]
→ Affiche uniquement les leçons marquées AVEC les deux python ET async
→ Exemple: "Asyncio en Python"
```

### Pages de Tags

Chaque tag a sa propre page:
- `/tags/python/` → Toutes les leçons Python
- `/tags/react/` → Toutes les leçons React
- `/tags/testing/` → Toutes les leçons liées aux tests

---

## Erreurs Courantes de Marquage

### ❌ Erreur 1: Trop Spécifique/Imbriqué

```yaml
tags: [python, python-basics, python-functions, python-scope]
```

**Problème**: Redondant, duplique le sujet/les métadonnées  
**Correction**: `tags: [python, functions, scope]`

### ❌ Erreur 2: Trop Vague

```yaml
tags: [learning, tutorial, web]
```

**Problème**: Pas utile pour trouver cette leçon spécifique  
**Correction**: `tags: [javascript, react, hooks, state-management]`

### ❌ Erreur 3: Plusieurs Mots en Tant que Tag Unique

```yaml
tags: [machine learning, data visualization]
```

**Problème**: Markdown/YAML s'attend à des traits d'union  
**Correction**: `tags: [machine-learning, data-visualization]`

### ❌ Erreur 4: Capitalisation Incohérente

```yaml
tags: [Python, functions, LOOPS]
```

**Problème**: Casse l'agrégation des tags (Python ≠ python)  
**Correction**: `tags: [python, functions, loops]`

### ❌ Erreur 5: Mélange de Niveaux

```yaml
tags: [beginner, intermediate]
```

**Problème**: Les métadonnées spécifient déjà la difficulté  
**Correction**: Utilisez des tags de niveau unique comme `beginner-friendly` (optionnel) OU omettez et utilisez metadata.difficulty

---

## Maintenance des Tags

### Ajouter des Tags Nouveaux

C'est correct d'introduire de nouveaux tags au fur et à mesure que vous créez des leçons. Le système les indexe automatiquement.

**Processus**:
1. Utilisez un nouveau tag dans votre leçon: `tags: [python, decorators, ...]`
2. Soumettez PR
3. Les mainteneurs approuvent
4. Le tag apparaît dans le nuage de tags et les pages de tags

### Dépréciation des Tags

Si un tag devient obsolète (par exemple, Python 2 → Python 3):

**Processus**:
1. Créez un alias ou un tag de remplacement
2. Mettez à jour les leçons existantes vers le nouveau tag
3. Éliminez progressivement l'ancien tag
4. Supprimez de l'index des tags

### Standardisation des Tags

Occasionnellement, les mainteneurs peuvent standardiser les tags:
- `async-await` vs `asyncio` → Standardiser vers `async-await`
- `db` vs `database` → Standardiser vers `database`

Vos leçons existantes seront mises à jour automatiquement.

---

## Référence Rapide

### Format des Tags
```yaml
tags: [word1, word2-word3, word4]  # minuscules, avec tirets
```

### Tags Recommandés par Sujet

**Python**:
`python`, `functions`, `loops`, `classes`, `async`, `testing`, `data-science`

**Développement Web**:
`javascript`, `react`, `css`, `html`, `api`, `rest`, `frontend`, `backend`

**Science des Données**:
`python`, `pandas`, `data-analysis`, `visualization`, `machine-learning`, `statistics`

### Flux de Travail des Tags

1. Choisissez 3-5 tags qui répondent à: "Qu'est-ce que quelqu'un chercherait pour trouver ceci?"
2. Utilisez le format minuscules avec tirets
3. Soyez spécifique mais pas redondant
4. Vérifiez qu'il n'y a pas de chevauchement avec les métadonnées/sujets

---

## Voir aussi

- [Référence des Métadonnées](metadata-reference.md) - Spécifications complètes des champs
- [Guide du Flux de Travail des Leçons](workflow-create-lesson.md) - Flux de travail de création complet
- [Guide de Démarrage Rapide](quick-start.md) - Aperçu 10 minutes

---

## Exemples

**Leçon Fonctions Python**:
```yaml
tags: [python, functions, parameters, scope, code-organization]
```

**Leçon Conception d'API REST**:
```yaml
tags: [api, rest, http, web-services, backend]
```

**Leçon Crochets React**:
```yaml
tags: [react, javascript, hooks, functional-components, state]
```

**Leçon Introduction à l'Apprentissage Automatique**:
```yaml
tags: [machine-learning, python, scikit-learn, classification, data-science]
```

---

Prêt à marquer vos leçons? 🏷️
