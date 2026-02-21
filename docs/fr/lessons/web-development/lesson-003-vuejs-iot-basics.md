---
title: "Bases de Vue.js pour interfaces web IoT"
description: "Apprenez à construire une interface Vue.js simple et réactive pour piloter et superviser des objets connectés"
difficulty: "Intermediate"
duration: "1 heure"
tags: [vuejs, javascript, frontend, iot, web]
prerequisites: [lesson-002-css-basics]
learning_objectives:
  - "Créer un composant Vue.js qui affiche l'état d'un appareil IoT"
  - "Utiliser les directives Vue (`v-bind`, `v-if`, `v-for`) pour rendre une interface dynamique"
  - "Connecter une interface Vue à des données simulées de capteurs et actions utilisateur"
created: 2026-02-21
author: "LLM Assistant"
status: "published"
---

# Bases de Vue.js pour interfaces web IoT

## Objectifs d'Apprentissage

À la fin de cette leçon, vous pourrez:
- Créer un composant Vue.js qui affiche l'état d'un appareil IoT
- Utiliser les directives Vue (`v-bind`, `v-if`, `v-for`) pour rendre une interface dynamique
- Connecter une interface Vue à des données simulées de capteurs et actions utilisateur

## Introduction

Quand on développe un projet IoT, on a souvent besoin d'une interface claire pour visualiser des mesures (température, humidité, batterie) et piloter des actionneurs (LED, relais, pompe). Vue.js est un excellent choix pour cela: léger, simple à prendre en main, et très efficace pour créer des interfaces réactives.

Dans cette leçon, vous allez construire un mini tableau de bord Vue.js pensé pour un contexte embarqué: données qui changent souvent, feedback utilisateur immédiat et composants réutilisables.

## Vue.js pour un tableau de bord IoT

Vue.js repose sur une idée centrale: **l'interface reflète automatiquement l'état des données**.

Pour l'IoT, cela signifie:

- une valeur de capteur change → l'écran se met à jour
- un appareil passe hors ligne → un indicateur visuel apparaît
- l'utilisateur clique sur un bouton → l'état de l'actionneur change

### Exemple 1: Premier composant Vue pour un capteur

```html
<div id="app">
  <h2>{{ deviceName }}</h2>
  <p>Température: {{ temperature }} °C</p>
</div>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  Vue.createApp({
    data() {
      return {
        deviceName: "Station Serre #1",
        temperature: 23.4
      };
    }
  }).mount("#app");
</script>
```

Ici, `{{ temperature }}` est automatiquement affiché. Si la valeur change dans `data`, l'UI se met à jour sans manipulation manuelle du DOM.

### Exemple 2: Indicateur d'état en ligne/hors ligne

```html
<div id="app">
  <h2>{{ deviceName }}</h2>
  <p v-if="isOnline" style="color: green;">Appareil en ligne</p>
  <p v-else style="color: red;">Appareil hors ligne</p>
</div>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  Vue.createApp({
    data() {
      return {
        deviceName: "Passerelle Atelier",
        isOnline: false
      };
    }
  }).mount("#app");
</script>
```

La directive `v-if` permet d'afficher une information opérationnelle critique selon l'état réel du device.

## Affichage de plusieurs mesures et interactions

Un dashboard IoT contient souvent plusieurs capteurs et commandes. Vue simplifie cela grâce aux listes et aux liaisons dynamiques.

### Exemple 1: Liste de capteurs avec `v-for`

```html
<div id="app">
  <h2>Capteurs - {{ deviceName }}</h2>
  <ul>
    <li v-for="sensor in sensors" :key="sensor.id">
      {{ sensor.label }}: {{ sensor.value }} {{ sensor.unit }}
    </li>
  </ul>
</div>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  Vue.createApp({
    data() {
      return {
        deviceName: "Module Environnement",
        sensors: [
          { id: 1, label: "Température", value: 24.1, unit: "°C" },
          { id: 2, label: "Humidité", value: 55, unit: "%" },
          { id: 3, label: "CO₂", value: 620, unit: "ppm" }
        ]
      };
    }
  }).mount("#app");
</script>
```

Avec `v-for`, on ajoute ou retire facilement des capteurs sans dupliquer le HTML.

## Cycle de mise à jour et commande utilisateur

Dans un cas réel, les données viennent d'une API, d'un WebSocket ou d'un broker MQTT. Pour cette leçon, on simule ces changements pour comprendre la logique côté UI.

```html
<div id="app">
  <h2>{{ deviceName }}</h2>
  <p>État LED: <strong>{{ ledOn ? "ON" : "OFF" }}</strong></p>
  <button @click="toggleLed">Basculer LED</button>
  <p>Dernière mesure: {{ temperature.toFixed(1) }} °C</p>
</div>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  Vue.createApp({
    data() {
      return {
        deviceName: "Node ESP32",
        ledOn: false,
        temperature: 22.0
      };
    },
    methods: {
      toggleLed() {
        this.ledOn = !this.ledOn;
      }
    },
    mounted() {
      setInterval(() => {
        this.temperature = 21 + Math.random() * 4;
      }, 3000);
    }
  }).mount("#app");
</script>
```

Le bouton appelle une méthode Vue et la valeur de température évolue périodiquement, simulant un flux capteur.

## Exercices

### Exercice 1: Carte d'appareil IoT

**Difficulté**: Débutant  
**Temps**: 5-10 minutes

Créez un composant Vue qui affiche:

- le nom d'un appareil
- son statut (`en ligne`/`hors ligne`) avec `v-if`
- une valeur de batterie en pourcentage

Ajoutez un bouton qui inverse l'état en ligne/hors ligne.

**Résultat attendu**: Une carte d'appareil réactive qui met à jour l'affichage immédiatement après clic.

### Exercice 2: Mini dashboard multi-capteurs

**Difficulté**: Intermédiaire  
**Temps**: 15-20 minutes

Construisez une page Vue avec un tableau de capteurs (`température`, `humidité`, `luminosité`) en utilisant `v-for`.

Ensuite:

1. Ajoutez un bouton "Actualiser" qui modifie les valeurs par JavaScript
2. Affichez une alerte visuelle si la température dépasse 30°C
3. Affichez l'heure de dernière mise à jour

## Évaluation

### Questions d'Auto-Évaluation

1. Quelle différence pratique y a-t-il entre modifier le DOM manuellement et utiliser la réactivité Vue pour un dashboard IoT?
2. Dans quel cas utilisez-vous `v-if` plutôt que `v-for` dans une interface de supervision?
3. Quelles parties du code doivent changer pour passer de données simulées à une API réelle?

## Résumé

Vous avez vu comment Vue.js permet de créer rapidement des interfaces IoT dynamiques: affichage de mesures, statut d'appareil et interactions utilisateur. En combinant `data`, directives (`v-if`, `v-for`) et méthodes, vous pouvez construire une base solide de dashboard prête à être connectée à des sources de données réelles.

## Ressources Supplémentaires

- [Vue.js Guide officiel](https://vuejs.org/guide/introduction.html)
- [Vue.js Essentials (template syntax, directives, reactivity)](https://vuejs.org/guide/essentials/template-syntax.html)
- [MDN - Introduction aux API Fetch](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch)

## Prochaines Étapes

Après avoir complété cette leçon, explorez:
- Connexion de Vue.js à une API REST pour récupérer des données capteurs
- Utilisation de WebSocket ou MQTT via backend pour des mises à jour temps réel
- Découpage du dashboard en composants Vue réutilisables
