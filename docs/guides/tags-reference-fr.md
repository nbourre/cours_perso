# Référence des Tags

Bienvenue dans le guide de référence des tags! Cette page liste tous les tags disponibles utilisés dans le système de leçon et montre quelles leçons sont marquées avec chacun.

**Les tags permettent la découverte entre sujets**. Au lieu de naviguer par sujet, vous pouvez rechercher par sujet ou concept pour trouver des leçons connexes dans tous les sujets.

---

## Comment Fonctionnent les Tags

Chaque leçon est marquée avec 1-5 mots-clés qui décrivent son contenu. Les tags vous aident à:

- **Découvrir des leçons connexes** dans différents sujets
- **Trouver des leçons par technologie** (par exemple, "python", "javascript", "css")
- **Trouver des leçons par concept** (par exemple, "functions", "data-types", "async")
- **Trouver des leçons par domaine** (par exemple, "web", "backend", "data-analysis")

### Exemple: Trouver la Programmation Asynchrone

Si vous recherchez le tag **"async"**, vous trouverez des leçons sur la programmation asynchrone indépendamment du sujet dans lequel elles se trouvent. Actuellement, nous avons des leçons marquées avec des concepts individuels, mais cela aide lorsque nous avons des leçons de plusieurs sujets couvrant le même sujet.

---

## Tous les Tags Disponibles

### Tags Technologiques
Tags pour les langages de programmation, frameworks et bibliothèques spécifiques:

- **`python`** (3 leçons)
  - Leçon: Introduction aux Variables
  - Leçon: Fonctions: Réutilisation et Organisation du Code
  - Leçon: Pandas pour l'Analyse de Données

- **`javascript`** (0 leçons)
  - *À venir*

- **`html`** (1 leçon)
  - Leçon: Fondamentaux HTML: Construire des Pages Web

- **`css`** (1 leçon)
  - Leçon: Essentiels CSS: Styliser Vos Pages Web

- **`pandas`** (1 leçon)
  - Leçon: Pandas pour l'Analyse de Données

### Tags de Concepts
Tags pour les idées abstraites, les modèles et les concepts de programmation:

- **`variables`** (1 leçon)
  - Leçon: Introduction aux Variables

- **`data-types`** (1 leçon)
  - Leçon: Introduction aux Variables

- **`functions`** (1 leçon)
  - Leçon: Fonctions: Réutilisation et Organisation du Code

- **`code-organization`** (1 leçon)
  - Leçon: Fonctions: Réutilisation et Organisation du Code

- **`parameters`** (1 leçon)
  - Leçon: Fonctions: Réutilisation et Organisation du Code

- **`return-values`** (1 leçon)
  - Leçon: Fonctions: Réutilisation et Organisation du Code

- **`markup`** (1 leçon)
  - Leçon: Fondamentaux HTML: Construire des Pages Web

- **`semantic-html`** (1 leçon)
  - Leçon: Fondamentaux HTML: Construire des Pages Web

- **`elements`** (1 leçon)
  - Leçon: Fondamentaux HTML: Construire des Pages Web

- **`styling`** (1 leçon)
  - Leçon: Essentiels CSS: Styliser Vos Pages Web

- **`selectors`** (1 leçon)
  - Leçon: Essentiels CSS: Styliser Vos Pages Web

- **`layout`** (1 leçon)
  - Leçon: Essentiels CSS: Styliser Vos Pages Web

- **`responsive`** (1 leçon)
  - Leçon: Essentiels CSS: Styliser Vos Pages Web

- **`data-analysis`** (1 leçon)
  - Leçon: Pandas pour l'Analyse de Données

- **`dataframes`** (1 leçon)
  - Leçon: Pandas pour l'Analyse de Données

### Tags de Domaine
Tags pour les domaines d'application:

- **`web`** (2 leçons)
  - Leçon: Fondamentaux HTML: Construire des Pages Web
  - Leçon: Essentiels CSS: Styliser Vos Pages Web

- **`basics`** (1 leçon)
  - Leçon: Introduction aux Variables

- **`data-science`** (1 leçon)
  - Leçon: Pandas pour l'Analyse de Données

- **`frontend`** (0 leçons)
  - *À venir* - Leçons JavaScript, React, Vue

- **`backend`** (0 leçons)
  - *À venir* - Leçons Node.js, frameworks Python

### Tags Spécifiques aux Sujets

- **`python`** - Sujets liés au langage Python
- **`html`** - Structure web et balisage
- **`css`** - Mise en style web et mise en page
- **`data-analysis`** - Analyse de données et manipulation

---

## Exemples d'Utilisation des Tags

### Exemple 1: Trouver du Contenu Convivial pour les Débutants
Parcourez les leçons marquées avec des concepts fondamentaux:

- `variables` (variables et types de données)
- `basics` (contenu introductif)
- `fundamentals` (concepts fondamentaux)

### Exemple 2: Trouver des Leçons de Développement Web
Parcourez toutes les leçons liées au web:

- `web` (leçons de développement web)
- `html` (structure web)
- `css` (mise en style web)
- `javascript` (interactivité web)

### Exemple 3: Trouver du Contenu d'Analyse de Données
Parcourez les leçons spécifiques aux données:

- `data-analysis`
- `data-science`
- `pandas`

---

## Statistiques des Tags

| Catégorie | Total des Tags | Total des Leçons Marquées |
|-----------|--------|------------------------|
| Technologie | 5 | 5 |
| Concept | 14 | 5 |
| Domaine | 4 | 3 |
| **TOTAL** | **23** | **5** |

---

## Directives de Marquage

Lors de la création de nouvelles leçons, respectez ces directives pour un marquage cohérent:

### À Faire ✅
- Utilisez des lettres minuscules et des tirets: `data-analysis`, pas `Data_Analysis`
- Choisissez 3-5 tags par leçon
- Utilisez des tags spécifiques et significatifs
- Pensez à la façon dont les apprenants chercheraient

### À Éviter ❌
- N'utilisez pas d'espaces ou de traits de soulignement: `async-await` pas `async_await`
- Ne marquez pas le même concept de plusieurs façons: utilisez soit `functions` soit `function-basics`, pas les deux
- N'utilisez pas de tags trop larges: `programming` est trop large, utilisez des tags spécifiques à la place
- Ne marquez pas les métadonnées (utilisez les champs de métadonnées à la place): la difficulté doit être dans le champ `difficulty`, pas comme tag

### Exemples de Bons Tags
```yaml
tags: [python, functions, scope]          # Spécifique et utile
tags: [javascript, async, promises]       # Clair et détectable
tags: [web, html, semantic-html]          # Domaine, technologie, concept
```

### Exemples à Éviter
```yaml
tags: [Python, JavaScript, learning]      # Capitalisation, trop générique
tags: [function, functions, func]         # Variations redondantes
tags: [beginner, intermediate]            # Doit utiliser metadata.difficulty à la place
```

---

## Ajouter des Tags Nouveaux

Les nouveaux tags sont automatiquement indexés lorsque vous les ajoutez à des leçons. Pour ajouter un nouveau tag:

1. Choisissez un nom significatif, minuscule, avec des tirets
2. Ajoutez-le à l'en-tête YAML d'une leçon: `tags: [existing, new-tag]`
3. Soumettez la leçon via une demande de tirage
4. Le nouveau tag apparaît dans cet index automatiquement

---

## Index Actuel des Tags

### Tags les Plus Utilisés
1. `python` (3 leçons)
2. `web` (2 leçons)
3. Tous les autres (1 leçon chacun)

### Tags les Plus Récents
- `return-values` (ajouté avec la leçon Fonctions)
- `semantic-html` (ajouté avec la leçon HTML)
- `responsive` (ajouté avec la leçon CSS)
- `dataframes` (ajouté avec la leçon Pandas)

---

## Voulez-vous Trouver des Leçons par Tag?

Actuellement, parcourez cette page pour voir quelles leçons ont chaque tag. À l'avenir, les leçons seront filtrables par tag avec:

- Nuage de tags sur la page d'accueil
- Filtre de tags sur les pages des sujets
- Recherche de tags mondiale
- Leçons connexes basées sur les tags partagés

---

## Voir aussi

- [Guide de Démarrage Rapide](quick-start.md) - Aperçu 10 minutes
- [Guide de Marquage](tagging-guide.md) - Comment marquer les leçons lors de leur création
- [Référence des Métadonnées](metadata-reference.md) - Spécifications complètes des champs

---

*Dernière mise à jour: 30 janvier 2026*  
*Total des leçons: 5 | Total unique des tags: 23*
