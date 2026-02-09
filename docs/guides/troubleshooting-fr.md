# Guide de Dépannage

Problèmes courants et solutions lors de la création et de la contribution de leçons.

---

## 🛠️ Problèmes de Contenu et d'Écriture

### Ma leçon est trop longue

**Problème**: La leçon prend plus de temps que prévu ou couvre trop de concepts.

**Solutions**:

- **Divisez en plusieurs leçons**: Divisez les sujets complexes en leçons distinctes et ciblées
- **Concentrez-vous sur un concept clé**: Chaque leçon doit enseigner 1-2 idées principales
- **Déplacez le contenu avancé**: Sauvegardez les approfondissements optionnels pour la section "Lectures Complémentaires"
- **Réduisez les exemples**: Gardez les 3-4 meilleurs exemples, supprimez les redondants
- **Simplifiez les exercices**: Concentrez-vous sur la pratique essentielle, pas une couverture exhaustive

**Directives de Durée**:

- 30 min: 1 concept, 2 exercices simples
- 45 min: 1-2 concepts, 2-3 exercices
- 1 heure: 2-3 concepts, 3-4 exercices
- 1,5-2 heures: 3-4 concepts + projet

### Mes exemples de leçon ne fonctionnent pas

**Problème**: Les exemples de code contiennent des erreurs ou ne s'exécutent pas.

**Solutions**:

- **Testez chaque exemple de code**: Exécutez-le vous-même avant de soumettre
- **Vérifiez les dépendances**: Les bibliothèques requises sont-elles installées?
- **Vérifiez la syntaxe soigneusement**: Indentation Python, points-virgules JavaScript, etc.
- **Ajoutez des instructions de configuration**: Si une configuration spéciale est nécessaire, expliquez-la
- **Fournirez une sortie attendue**: Montrez ce que le code réussi doit produire
- **Incluez des explications d'erreurs**: Si vous montrez des erreurs, expliquez-les

**Pour Python**: Testez dans un shell interactif (Python REPL ou Jupyter)
**Pour JavaScript**: Testez dans la console du navigateur ou Node.js
**Pour HTML/CSS**: Testez dans un navigateur

### Les exercices sont confus

**Problème**: Les étudiants ne comprennent pas ce que demandent les exercices.

**Solutions**:

- **Instructions claires**: Commencez chaque exercice par "Écrivez une fonction qui..." ou "Créez un programme qui..."
- **Spécifiez l'entrée/sortie**: Montrez les exemples d'entrées et les résultats attendus
- **Ajoutez des indices**: Pour les exercices difficiles, fournissez des indices après les exercices
- **Difficulté progressive**: Facile → Moyen → Difficile
- **Incluez des solutions**: Fournissez des solutions/réponses (dans une section distincte)

### J'utilise des informations obsolètes

**Problème**: La leçon fait référence à des versions anciennes ou des fonctionnalités obsolètes.

**Solutions**:

- **Vérifiez les numéros de version**: Vérifiez que tous les numéros de version de bibliothèque/framework sont actuels
- **Recherchez des obsolescences**: Recherchez "[fonctionnalité] obsolète" dans la documentation
- **Testez sur la version actuelle**: Assurez-vous que les exemples fonctionnent avec la dernière version
- **Ajoutez des notes de version**: Si spécifique à la version, précisez-le: "Python 3.10+"
- **Incluez des notes de migration**: Pour les fonctionnalités obsolètes, suggérez des alternatives

---

## 📝 Problèmes de Métadonnées et de Structure

### Mon en-tête YAML a des erreurs

**Problème**: La validation des métadonnées échoue ou MkDocs ne construit pas.

**Erreurs courantes**:

- **Deux-points dans les titres**: Enveloppez avec des guillemets: `title: "Python: Fonctions et Organisation"`
- **Syntaxe de liste**: Utilisez le format de liste YAML approprié:
  ```yaml
  tags:
    - python
    - functions
    - basics
  ```
- **Valeurs booléennes**: Utilisez `true`/`false` pas `True`/`False`
- **Caractères échappés**: Utilisez des guillemets si caractères spéciaux: `description: "Qu'est-ce qu'une variable?"`

**Solutions**:

- **Validez YAML**: Utilisez le validateur YAML en ligne (yamllint.com)
- **Vérifiez les guillemets**: Les guillemets simples/doubles doivent être équilibrés
- **Vérifiez l'indentation**: YAML est sensible aux espaces (utilisez l'indentation 2 espaces)
- **Testez localement**: Construisez MkDocs: `mkdocs serve`

### Champs obligatoires manquants

**Problème**: Leçon manquant des champs de métadonnées comme `difficulty` ou `learning_objectives`.

**Champs obligatoires** (tous doivent être présents):

- `title`: Nom de la leçon
- `description`: Résumé d'une phrase
- `difficulty`: Beginner / Intermediate / Advanced
- `duration`: Estimation du temps avec unité (30 minutes, 1 heure, etc.)
- `tags`: 1-5 tags de sujet
- `learning_objectives`: 3-5 résultats spécifiques
- `created`: Date de création (YYYY-MM-DD)

**Solution**: Copiez le [modèle de leçon](../templates/lesson-template.md) et remplissez tous les champs.

### Les tags sont incohérents

**Problème**: Les tags ne correspondent pas aux tags existants ou ne sont pas formatés correctement.

**Solutions**:

- **Utilisez des minuscules**: `python` pas `Python`
- **Utilisez des tirets**: `machine-learning` pas `machine_learning`
- **Vérifiez les tags existants**: Voir [Référence des Tags](tags-reference.md)
- **Soyez spécifique**: `web-development` mieux que `web`
- **Limitez à 5**: Ne sur-marquez pas

**Tags disponibles**: Voir [Référence des Tags](tags-reference.md) pour la liste complète et l'utilisation.

---

## 🔧 Problèmes Techniques

### Mon fichier de leçon n'apparaît pas sur le site

**Problème**: Fichier créé mais la leçon n'apparaît pas après la construction.

**Checklist**:

- [ ] Le fichier est au bon endroit: `docs/lessons/[subject]/lesson-*.md`
- [ ] Le nom du fichier correspond au modèle: `lesson-NNN-slug.md`
- [ ] Le fichier a l'en-tête obligatoire (YAML en haut)
- [ ] La config MkDocs inclut ce sujet dans la navigation
- [ ] La construction s'est déroulée sans erreurs: Aucune erreur dans la sortie de construction
- [ ] Le cache du site a été effacé: Rafraîchissement difficile (Ctrl+Maj+R)

**Solutions**:

- **Vérifiez le chemin du fichier**: Assurez-vous que le répertoire du sujet existe
- **Vérifiez l'en-tête**: Vérifiez que le YAML est valide (voir les problèmes YAML ci-dessus)
- **Reconstruisez le site**: Supprimez le dossier `site/`, exécutez `mkdocs build`
- **Vérifiez la navigation**: Vérifiez que `mkdocs.yml` inclut votre sujet

### Les liens dans ma leçon sont brisés

**Problème**: Les liens dans la leçon ne fonctionnent pas ou apparaissent comme des liens rouges.

**Solutions**:

- **Vérifiez les chemins des liens**: Les liens doivent être relatifs au répertoire `docs/`
- **Utilisez la syntaxe correcte**: `[text](path/to/file.md)` pour les liens internes
- **Testez chaque lien**: Cliquez sur eux pour vérifier qu'ils fonctionnent
- **Vérifiez les noms de fichiers**: L'orthographe, la casse, les extensions doivent correspondre exactement
- **Utilisez les chemins absolus**: À partir de la racine `docs/`, pas du dossier actuel

**Exemples**:
```markdown
# Correct - à partir de la racine docs/
[template](templates/lesson-template.md)
[guide](guides/quick-start.md)

# Incorrect - ne fonctionnera pas
[template](./lesson-template.md)
[guide](../docs/guides/quick-start.md)
```

### Le formatage Markdown semble incorrect

**Problème**: Le formatage est rendu incorrectement (le gras ne fonctionne pas, les listes sont cassées, etc.).

**Problèmes courants**:

- **Gras**: Utilisez `**text**` ou `__text__`, pas `*text*`
- **Listes**: Doit avoir une ligne vierge avant le premier élément
- **Blocs de code**: Utilisez des backticks triples avec la langue: ` ```python `
- **Guillemets**: Utilisez `>` pour les citations
- **Échappement**: Utilisez `\` pour échapper les caractères spéciaux: `\*pas gras\*`

**Solutions**:

- **Testez localement**: Construisez avec `mkdocs serve` et vérifiez dans le navigateur
- **Comparez avec les exemples**: Regardez les leçons qui fonctionnent dans le même sujet
- **Utilisez un validateur**: Validateur Markdown en ligne
- **Vérifiez l'espacement**: YAML, les listes et les blocs de code ont besoin d'espacement approprié

### Les images ne s'affichent pas

**Problème**: Les images de la leçon ne s'affichent pas.

**Solutions**:

- **Utilisez le chemin correct**: `![alt text](../../assets/image.png)`
- **Vérifiez les chemins relatifs**: Comptez correctement les niveaux `../`
- **Vérifiez que le fichier existe**: Le fichier image est effectivement dans `docs/assets/`
- **Utilisez les formats pris en charge**: PNG, JPG, SVG, GIF
- **Ajoutez du texte alternatif**: `![description of image](path)`

**Meilleure pratique**: Stockez les images dans `docs/assets/images/` organisées par sujet

---

## 🔄 Problèmes Git et GitHub

### Je ne peux pas pousser mes changements

**Problème**: Git push échoue.

**Solutions**:

- **Vérifiez le remote**: `git remote -v` (doit afficher votre fork)
- **Tirez d'abord**: `git pull origin main` avant la poussée
- **Vérifiez la branche**: `git branch` (doit afficher votre branche)
- **Forcez si nécessaire**: `git push -f origin your-branch-name`

**Prévention**: Tirez toujours avant la poussée pour éviter les conflits.

### Ma PR a des conflits de fusion

**Problème**: La demande de tirage montre des conflits avec la branche principale.

**Solutions** (dans l'ordre de préférence):

1. **Rebasez sur main**: 
   ```bash
   git fetch upstream
   git rebase upstream/main
   git push -f origin your-branch-name
   ```

2. **Fusionnez main dans votre branche**:
   ```bash
   git fetch upstream
   git merge upstream/main
   git push origin your-branch-name
   ```

3. **Résolvez manuellement**: Corrigez les conflits dans votre éditeur, commitez, poussez

**Prévention**: Gardez la branche à jour, synchronisez avec main avant de soumettre

### Ma branche est derrière main

**Problème**: La branche est obsolète par rapport à main.

**Solutions**:
```bash
# Mettez à jour votre main local
git fetch upstream
git checkout main
git merge upstream/main

# Rebasez votre branche
git checkout your-branch
git rebase main
git push -f origin your-branch
```

---

## 📚 Problèmes de Génération LLM

### Le contenu généré par LLM est trop technique

**Problème**: Le contenu de ChatGPT/Claude utilise une terminologie au-dessus de la difficulté cible.

**Solutions**:

- **Régénérez avec une meilleure invite**: Spécifiez "Beginner" et "utilisez un langage simple"
- **Réécrivez les sections**: Utilisez vos propres explications plus simples
- **Ajoutez des définitions**: Définissez les termes techniques quand ils sont introduits pour la première fois
- **Utilisez des analogies**: Expliquez les idées complexes avec des comparaisons quotidiennes
- **Simplifiez les exemples**: Remplacez les exemples avancés par des exemples adaptés aux débutants

### Les exemples LLM ne fonctionnent pas

**Problème**: Le code de ChatGPT/Claude contient des erreurs.

**Solutions**:

- **Testez chaque exemple**: Exécutez-le avant de soumettre
- **Vérifiez les versions**: Assurez-vous que le code fonctionne avec les versions spécifiées
- **Demandez au LLM de corriger**: Collez l'erreur et demandez une version corrigée
- **Testez dans l'IDE**: Utilisez un IDE approprié pour détecter les erreurs tôt
- **Mettez à jour les dépendances**: Le code peut nécessiter des bibliothèques plus récentes

### Le contenu est trop générique

**Problème**: Le contenu généré ne correspond pas au style de votre cours.

**Solutions**:

- **Personnalisez fortement**: Ajoutez vos propres exemples et contexte
- **Remplacez les sections génériques**: Gardez la structure, personnalisez le contenu
- **Ajoutez des références locales**: Référencez votre cours/communauté spécifique
- **Incluez vos idées**: Mélangez le contenu IA avec votre expertise
- **Vérifiez l'exactitude**: Assurez-vous que les exemples correspondent à votre contexte

Voir [Instructions LLM](lesson-template-instructions.md) pour des techniques d'incitation meilleures.

---

## 📊 Problèmes de Qualité et d'Examen

### Ma leçon a été rejetée

**Problème**: La PR a été fermée ou des modifications ont été demandées.

**Raisons courantes**:

- **Métadonnées incomplètes**: Champs YAML manquants ou incorrects
- **Qualité du contenu**: Écriture peu claire, informations inexactes ou exemples brisés
- **Non-concordance de style**: Ne suit pas le modèle ou les leçons existantes
- **Informations obsolètes**: Références à des versions anciennes ou des fonctionnalités obsolètes
- **Test insuffisant**: Les exemples ou exercices ne fonctionnent pas

**Solutions**:

- **Lisez les commentaires**: Lisez attentivement les commentaires du relecteur
- **Abordez tous les points**: Apportez les modifications demandées
- **Soumettez une nouvelle PR**: Après avoir apporté les corrections
- **Demandez une clarification**: Si les commentaires ne sont pas clairs, commentez la PR ou créez une issue

### Ma leçon a été fusionnée mais a des problèmes

**Problème**: La leçon est en direct mais contient des erreurs ou a besoin de mises à jour.

**Solutions**:

- **Soumettez une nouvelle PR**: Corrigez les problèmes dans une nouvelle demande de tirage
- **Créez une issue**: Signalez les problèmes pour que d'autres les résolvent
- **Corrections rapides**: Pour les typos, les petits problèmes, vous pouvez éditer directement

---

## 🆘 Obtenir de l'Aide

**Impossible de trouver votre problème?**

1. **Vérifiez les issues existantes**: Recherchez les issues GitHub pour des problèmes similaires
2. **Demandez dans les discussions**: Démarrez une discussion GitHub pour obtenir de l'aide
3. **Commentez les issues pertinentes**: Votre question pourrait aider d'autres
4. **Vérifiez les docs des modèles**: Voir [Instructions du Modèle de Leçon](lesson-template-instructions.md)

**Toujours bloqué?**

- **Créez un exemple minimal**: Partagez juste le code/contenu qui est cassé
- **Fournissez les messages d'erreur**: Copiez le texte d'erreur complet
- **Décrivez ce que vous avez essayé**: Aide les relecteurs à vous aider mieux
- **Incluez les chemins des fichiers**: Spécifiez exactement ce sur lequel vous travaillez

---

## ✅ Checklist Rapide Avant de Soumettre

Avant de pousser votre PR, vérifiez:

- [ ] Tous les champs YAML présents et valides
- [ ] Les exemples de code testés et fonctionnels
- [ ] Les exercices incluent des instructions claires
- [ ] Au moins une question d'auto-évaluation incluse
- [ ] Le fichier dans le bon répertoire
- [ ] Le fichier nommé correctement: `lesson-NNN-slug.md`
- [ ] La syntaxe Markdown valide (gras, listes, blocs de code)
- [ ] Tous les liens testés et fonctionnels
- [ ] Pas de typos ou de problèmes de formatage
- [ ] Suit la structure du modèle
- [ ] Révisé le [Guide de Démarrage Rapide](quick-start.md)

**Prêt?** Soumettez votre PR! 🚀

---

## 📞 Besoin de Plus d'Aide?

- **Questions sur les Leçons**: Voir [Flux de Travail de Création de Leçon](workflow-create-lesson.md)
- **Référence des Métadonnées**: Voir [Référence des Métadonnées](metadata-reference.md)
- **Aide sur le Marquage**: Voir [Guide de Marquage](tagging-guide.md)
- **Processus de Contribution**: Voir [Guide de Contribution](../CONTRIBUTING-fr.md)
- **Démarrage Rapide**: Voir [Guide de Démarrage Rapide](quick-start.md)

**Bon création!** 📚✨
