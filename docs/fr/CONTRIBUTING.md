# Contribuer au Système de Gestion des Leçons

Merci de votre intérêt à contribuer à ce référentiel de leçons personnalisées! Nous accueillons les contributions de leçons, les corrections de bogues, les améliorations de documentation et les idées de fonctionnalités de la communauté.

---

## 🎯 Comment Contribuer

### 1. Créer une Leçon (Plus Courant)

**Pour créer et soumettre des leçons**, consultez le guide détaillé:

👉 **[Guide du Flux de Travail de Création de Leçon](guides/workflow-create-lesson.md)** ← Commencez ici!

Le guide du flux de travail couvre:

- Planifier votre leçon
- Écrire ou générer du contenu avec LLM
- Tester et vérifier la qualité
- Soumettre via une demande de tirage GitHub

**TL;DR**: Copier [modèle de leçon](templates/lesson-template.md) → Écrire le contenu → Soumettre PR

### 2. Signaler des Problèmes ou Demander des Fonctionnalités

- **Trouvé un bogue?** → [Ouvrir une Issue GitHub](../../issues/new?labels=bug)
- **Vous voulez une nouvelle fonctionnalité?** → [Ouvrir une Issue GitHub](../../issues/new?labels=enhancement)
- **Vous avez une question?** → [Ouvrir une Discussion GitHub](../../discussions/new)

### 3. Améliorer la Documentation

- Repéré une faute de frappe ou une explication peu claire?
- Avez-vous une meilleure façon d'expliquer un concept?
- Voulez-vous ajouter des exemples ou des clarifications?

Il suffit de soumettre une demande de tirage avec vos améliorations!

---

## 📋 Checklist de Soumission

Avant de soumettre votre demande de tirage de leçon, vérifiez:

### Qualité du Contenu
- [ ] La leçon enseigne un concept clair et unique
- [ ] Les objectifs d'apprentissage sont spécifiques et réalisables
- [ ] Le contenu aborde chaque objectif d'apprentissage
- [ ] Les exemples sont pertinents et clairs
- [ ] Au moins 2-3 exercices inclus
- [ ] Des questions d'auto-évaluation incluses
- [ ] Pas d'informations obsolètes ou dépréciées

### Métadonnées
- [ ] Tous les champs YAML obligatoires présents: `title`, `description`, `difficulty`, `duration`, `tags`, `learning_objectives`, `created`
- [ ] Le titre fait 3-100 caractères
- [ ] La description est 1 phrase, 10-200 caractères
- [ ] `difficulty` est: Beginner, Intermediate ou Advanced
- [ ] `duration` inclut un nombre et une unité (minutes/heures/jours)
- [ ] `tags` sont 1-5 éléments, minuscules, avec tirets
- [ ] `learning_objectives` sont 3-5 résultats spécifiques

### Technique
- [ ] Fichier nommé: `lesson-[id]-[slug].md`
- [ ] Fichier dans le répertoire de sujet correct: `docs/lessons/[subject]/`
- [ ] La syntaxe Markdown est valide
- [ ] Tous les liens fonctionnent et sont correctement formatés
- [ ] Les exemples de code sont syntaxiquement corrects
- [ ] Pas de références d'images brisées

---

## 🚀 Démarrage Rapide: Créer Votre Première Leçon

1. **Lisez l'aperçu 10 minutes**: [Guide de Démarrage Rapide](guides/quick-start.md)

2. **Choisissez votre approche**:
   - **Manuel**: Écrivez le vôtre en utilisant le [Modèle de Leçon](templates/lesson-template.md)
   - **Généré par l'IA**: Utilisez le [Modèle d'Invite LLM](templates/llm-prompt-template.txt) avec ChatGPT, Claude ou similaire

3. **Enregistrez votre leçon**:
   - Créer un fichier: `docs/lessons/[subject]/lesson-[id]-[slug].md`
   - Exemple: `docs/lessons/python/lesson-001-variables.md`

4. **Soumettre via GitHub**:
   - Forker le référentiel
   - Créer une branche: `git checkout -b add-lesson-your-topic`
   - Ajouter votre fichier de leçon
   - Commit: `git commit -m "Add lesson: Your Lesson Title"`
   - Pousser et créer une demande de tirage

---

## 📝 Flux de Travail Git

### Configuration

```bash
# Forker le référentiel sur GitHub, puis:
git clone https://github.com/YOUR-USERNAME/cours_perso.git
cd cours_perso
git remote add upstream https://github.com/ORIGINAL-OWNER/cours_perso.git
```

### Créer une Leçon

```bash
# Créer une nouvelle branche
git checkout -b add-lesson-your-topic

# Créer votre leçon au bon endroit
# Exemple: docs/lessons/python/lesson-001-variables.md

# Stage et commit
git add docs/lessons/[subject]/lesson-*.md
git commit -m "Add lesson: Your Lesson Title"

# Pousser vers votre fork
git push origin add-lesson-your-topic
```

### Soumettre une Demande de Tirage

1. Aller au [référentiel original](../../)
2. Cliquer sur "New Pull Request"
3. Sélectionner votre branche
4. Remplir le modèle PR (voir ci-dessous)
5. Soumettre!

---

## 📄 Modèle de Demande de Tirage

Lorsque vous soumettez une PR, utilisez ce modèle:

```markdown
## Informations de Leçon

**Titre de la Leçon**: [Votre Titre de Leçon]
**Sujet**: [Bases Python / Développement Web / Science des Données]
**Difficulté**: [Beginner / Intermediate / Advanced]
**Durée**: [30 minutes / 1 heure / etc.]

## Description

[Brève résumé de ce que la leçon enseigne et pourquoi c'est utile]

## Checklist

- [ ] La leçon suit la structure du modèle
- [ ] Les métadonnées sont complètes et valides
- [ ] Toutes les sections obligatoires présentes
- [ ] Les exemples sont testés et fonctionnent correctement
- [ ] Les exercices sont clairs et progressifs
- [ ] Les questions d'auto-évaluation vérifient les objectifs d'apprentissage
- [ ] La syntaxe Markdown est valide
- [ ] Les liens fonctionnent

## Changements

- Ajouté: `docs/lessons/[subject]/lesson-*.md`

## Issues Connexes

[Référencez les issues connexes, le cas échéant]
```

---

## 🏷️ Normes des Leçons

### Niveaux de Difficulté

**Beginner**: Aucune connaissance préalable supposée
- Expliquer tous les concepts et termes
- Utiliser des exemples simples et concrets
- Construire à partir des bases
- Inclure des analogies utiles

**Intermediate**: Compréhension de base supposée
- Se déplacer plus rapidement à travers les concepts
- Se concentrer sur l'application
- Montrer les meilleures pratiques et les modèles
- Inclure certaines techniques avancées

**Advanced**: Base solide requise
- Supposer une connaissance préalable importante
- Plongée technique profonde
- Discuter des compromis et des cas limites
- Inclure l'optimisation et la performance

### Estimations de Durée

- **30 minutes**: 1 concept, 2 exercices simples
- **45 minutes**: 1-2 concepts, 2-3 exercices
- **1 heure**: 2-3 concepts, 2-3 exercices
- **1,5-2 heures**: 3-4 concepts, projet ou pierre de touche

### Nommage des Fichiers

```
lesson-[id]-[slug].md

Exemples:
lesson-001-variables.md
lesson-002-functions.md
lesson-003-lists-and-loops.md
lesson-010-async-await.md
```

- **[id]**: Nombre séquentiel (3 chiffres, rempli de zéros)
- **[slug]**: Nom adapté aux URL (minuscules, tirets)

---

## 🤖 Utiliser LLM pour Générer du Contenu

Consultez [Instructions du Modèle LLM](guides/lesson-template-instructions.md) pour:

- Comment utiliser ChatGPT, Claude ou d'autres LLM
- Modèles d'invite pour différents sujets
- Comment examiner et affiner le contenu généré
- Checklist de qualité pour les leçons générées par LLM

---

## 💡 Idées de Leçons et Inspiration

**Qu'est-ce qui fait une bonne leçon?**
- Enseigne un concept ou une compétence claire
- Inclut des exemples pratiques et fonctionnels
- Fournit des exercices pratiques
- Teste la compréhension avec des évaluations
- Se connecte aux cas d'usage du monde réel
- Suit la structure de notre modèle

**Vous avez besoin d'idées?**
- Enseigner une compétence de votre travail?
- Appris quelque chose de nouveau récemment?
- Vous voulez aider quelqu'un à comprendre un concept délicat?
- Trouvé un grand tutoriel et voulez l'adapter?

Tous sont les bienvenus! Soumettez comme une issue pour discuter d'abord si vous n'êtes pas sûr.

---

## 🔍 Processus d'Examen du Code

Lorsque vous soumettez une PR:

1. **Vérifications Automatisées** (5-10 minutes)
   - GitHub Actions valide la syntaxe Markdown
   - Vérifier les champs de métadonnées obligatoires
   - Vérifier le nommage et la structure des fichiers
   - Le statut apparaît comme une coche ou ✗

2. **Examen du Mainteneur** (24-48 heures)
   - Les relecteurs lisent votre leçon
   - Vérifier l'exactitude et la qualité
   - Vérifier l'alignement avec le style
   - Peut demander des améliorations

3. **Commentaires et Itération**
   - Répondre aux commentaires d'examen
   - Apporter les modifications demandées
   - Pousser les mises à jour vers votre branche (PR se met à jour automatiquement)
   - Les relecteurs revérifieront

4. **Approbation et Fusion**
   - Leçon approuvée et fusionnée
   - GitHub Actions reconstruit et déploie le site
   - Votre leçon est en direct! 🎉

---

## 📚 Ressources

- [Guide de Démarrage Rapide](guides/quick-start.md) — Aperçu 10 minutes
- [Flux de Travail de Création de Leçon](guides/workflow-create-lesson.md) — Guide détaillé étape par étape
- [Modèle de Leçon](templates/lesson-template.md) — Modèle à copier et utiliser
- [Instructions LLM](guides/lesson-template-instructions.md) — Comment utiliser l'IA pour générer du contenu
- [Référence des Métadonnées](guides/metadata-reference.md) — Spécifications complètes des champs
- [Guide de Marquage](guides/tagging-guide.md) — Comment marquer les leçons
- [Référence des Tags](guides/tags-reference.md) — Tags disponibles et leur utilisation

---

## ❓ FAQ

### Q: Puis-je réutiliser le contenu de mon blog ou de mon cours?

**A**: Oui, si vous en êtes propriétaire ou avez la permission. Inclure la source dans le champ auteur.
Exemple: `author: "Adapté de mon cours sur les APIs REST"`

### Q: Que faire si je veux créer plusieurs leçons?

**A**: Super! Soumettez-les une à la fois ou en PR séparées. Chacune sera examinée et fusionnée indépendamment.

### Q: Puis-je utiliser du contenu d'autres sources?

**A**: Oui, avec attribution. Assurez-vous que vous avez le droit de l'utiliser et créditez l'auteur original.

### Q: Que faire si ma leçon est rejetée?

**A**: Ne vous inquiétez pas! Nous fournirons des commentaires clairs sur ce qui doit changer. La plupart des rejets sont des corrections mineures. Soumettez à nouveau après avoir apporté les modifications demandées.

### Q: Combien de temps prend l'examen?

**A**: Généralement 24-48 heures pour l'examen initial. Certaines leçons nécessitent plus de discussion et peuvent prendre plus de temps.

### Q: Puis-je être un contributeur régulier?

**A**: Absolument! Si vous contribuez régulièrement, nous pouvons discuter de vous donner le statut de mainteneur pour des fusions plus rapides.

### Q: Comment mettre à jour une leçon après sa publication?

**A**: Soumettez une nouvelle PR avec des modifications. Les mainteneurs examinent et fusionnent. Le site se met à jour automatiquement.

---

## 📞 Des Questions?

- **Bloqué sur quelque chose?** → [Ouvrir une discussion](../../discussions/new)
- **Trouvé un problème?** → [Le signaler](../../issues/new)
- **Vous voulez discuter?** → Créer une issue avec l'étiquette `discussion`

---

## 🙏 Merci!

Merci de contribuer au référentiel de leçons! Votre travail aide les autres à apprendre et à grandir. Nous apprécions vos efforts dans:

- Créer du contenu éducatif de qualité
- Rendre les sujets complexes accessibles
- Aider à construire une communauté d'apprentissage
- Soutenir les autres dans leur parcours éducatif

---

**Prêt à créer votre première leçon?** Commencez par le [Guide de Démarrage Rapide](guides/quick-start.md)! 🚀
