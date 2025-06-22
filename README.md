# pile-stock-manager-hacs
Gestionnaire de Stock de Piles - Intégration personnalisée pour Home Assistant

# 🔋 Gestionnaire de Stock de Piles

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/votre-username/pile-stock-manager)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Une intégration personnalisée pour Home Assistant permettant de gérer un inventaire de piles avec des capteurs temps réel, des services de gestion et une persistance des données.

## ✨ Fonctionnalités

- **Capteurs temps réel** : Suivi automatique du stock pour chaque type de pile
- **Capteur de stock total** : Vue d'ensemble de l'inventaire complet
- **Services intégrés** : Ajouter, retirer et remettre à zéro le stock
- **Persistance des données** : Sauvegarde automatique dans un fichier JSON
- **Interface utilisateur** : Configuration simple via l'interface Home Assistant
- **Mise à jour forcée** : Capteurs avec `force_update = True` pour des données temps réel

## 🔧 Installation

### Via HACS (Recommandé)

1. Ouvrez HACS dans Home Assistant
2. Allez dans "Intégrations"
3. Cliquez sur les trois points et sélectionnez "Dépôts personnalisés"
4. Ajoutez l'URL : `https://github.com/votre-username/pile-stock-manager`
5. Sélectionnez "Intégration" comme type
6. Cliquez sur "Installer"
7. Redémarrez Home Assistant

### Installation Manuelle

1. Téléchargez la dernière version depuis les [Releases](https://github.com/votre-username/pile-stock-manager/releases)
2. Copiez le dossier `custom_components/pile_stock_manager` dans votre dossier `config/custom_components/`
3. Redémarrez Home Assistant
4. Ajoutez l'intégration via **Configuration** → **Intégrations** → **Ajouter une intégration**

## ⚙️ Configuration

1. Allez dans **Configuration** → **Intégrations**
2. Cliquez sur **Ajouter une intégration**
3. Recherchez "Gestionnaire de Stock de Piles"
4. Suivez les instructions de configuration

Aucune configuration supplémentaire n'est requise. L'intégration se configure automatiquement.

## 🔋 Types de Piles Supportées

L'intégration supporte 8 types de piles couramment utilisées :

| Type | Description | Utilisation courante |
|------|-------------|---------------------|
| **CR2450** | Pile bouton lithium 3V | Télécommandes, capteurs IoT |
| **CR2032** | Pile bouton lithium 3V | Cartes mères, montres |
| **CR2025** | Pile bouton lithium 3V | Petits appareils électroniques |
| **CR1620** | Pile bouton lithium 3V | Clés de voiture, appareils médicaux |
| **CR2016** | Pile bouton lithium 3V | Calculatrices, montres |
| **LR44** | Pile bouton alcaline 1.5V | Jouets, appareils photo |
| **AA** | Pile cylindrique standard | Télécommandes, radios |
| **AAA** | Pile cylindrique standard | Petits appareils portables |

## 📊 Capteurs Créés

Après installation, les capteurs suivants sont automatiquement créés :

### Capteurs Individuels
- `sensor.stock_cr2450` - Stock des piles CR2450
- `sensor.stock_cr2032` - Stock des piles CR2032  
- `sensor.stock_cr2025` - Stock des piles CR2025
- `sensor.stock_cr1620` - Stock des piles CR1620
- `sensor.stock_cr2016` - Stock des piles CR2016
- `sensor.stock_lr44` - Stock des piles LR44
- `sensor.stock_aa` - Stock des piles AA
- `sensor.stock_aaa` - Stock des piles AAA

### Capteur Global
- `sensor.stock_total_piles` - Stock total de toutes les piles

Tous les capteurs utilisent l'unité "unités" et sont mis à jour en temps réel.

## 🛠️ Services Disponibles

### `pile_stock_manager.add_stock`
Ajouter des piles au stock
service: pile_stock_manager.add_stock
data:
pile_type: "CR2032"
quantity: 5


**Paramètres :**
- `pile_type` (requis) : Type de pile à ajouter
- `quantity` (optionnel) : Quantité à ajouter (défaut: 1)

### `pile_stock_manager.remove_stock`
Retirer des piles du stock
service: pile_stock_manager.remove_stock
data:
pile_type: "AA"
quantity: 2

**Paramètres :**
- `pile_type` (requis) : Type de pile à retirer
- `quantity` (optionnel) : Quantité à retirer (défaut: 1)

### `pile_stock_manager.reset_stock`
Remettre à zéro tout l'inventaire
service: pile_stock_manager.reset_stock

**⚠️ Attention :** Cette action remet tous les stocks à zéro et ne peut pas être annulée.

## 🎨 Configuration des Cartes Lovelace

### 🏠 Carte Entities - Vue Complète
type: entities
title: 📦 Stock de Piles
icon: mdi:battery-outline
entities:

    entity: sensor.stock_total_piles
    name: Stock Total
    icon: mdi:battery-check

    type: divider

    entity: sensor.stock_cr2450
    name: CR2450
    icon: mdi:battery-outline

    entity: sensor.stock_cr2032
    name: CR2032
    icon: mdi:battery-outline

    entity: sensor.stock_cr2025
    name: CR2025
    icon: mdi:battery-outline

    entity: sensor.stock_cr1620
    name: CR1620
    icon: mdi:battery-outline

    entity: sensor.stock_cr2016
    name: CR2016
    icon: mdi:battery-outline

    entity: sensor.stock_lr44
    name: LR44
    icon: mdi:battery-outline

    entity: sensor.stock_aa
    name: Piles AA
    icon: mdi:battery

    entity: sensor.stock_aaa
    name: Piles AAA
    icon: mdi:battery
    show_header_toggle: false

### 📊 Carte Glance - Vue Compacte
type: glance
title: 🔋 Aperçu Stock Piles
entities:

    entity: sensor.stock_cr2450
    name: CR2450

    entity: sensor.stock_cr2032
    name: CR2032

    entity: sensor.stock_cr2025
    name: CR2025

    entity: sensor.stock_cr1620
    name: CR1620

    entity: sensor.stock_cr2016
    name: CR2016

    entity: sensor.stock_lr44
    name: LR44

    entity: sensor.stock_aa
    name: AA

    entity: sensor.stock_aaa
    name: AAA
    columns: 4
    show_name: true
    show_state: true

### 📈 Carte Gauge - Indicateurs Visuels
type: vertical-stack
cards:

    type: horizontal-stack
    cards:

        type: gauge
        entity: sensor.stock_cr2032
        name: CR2032
        min: 0
        max: 20
        severity:
        green: 10
        yellow: 5
        red: 0

        type: gauge
        entity: sensor.stock_aa
        name: Piles AA
        min: 0
        max: 30
        severity:
        green: 15
        yellow: 8
        red: 0

    type: horizontal-stack
    cards:

        type: gauge
        entity: sensor.stock_aaa
        name: Piles AAA
        min: 0
        max: 30
        severity:
        green: 15
        yellow: 8
        red: 0

        type: gauge
        entity: sensor.stock_total_piles
        name: Stock Total
        min: 0
        max: 100
        severity:
        green: 50
        yellow: 25
        red: 0

### 🎛️ Carte avec Boutons de Gestion
ype: vertical-stack
cards:

    type: entities
    title: 🔋 Gestion Stock Piles
    entities:

        entity: sensor.stock_total_piles
        name: Stock Total
        icon: mdi:battery-check

        type: divider

        entity: sensor.stock_cr2032
        name: CR2032
        secondary_info: last-updated

        entity: sensor.stock_aa
        name: Piles AA
        secondary_info: last-updated

        entity: sensor.stock_aaa
        name: Piles AAA
        secondary_info: last-updated

    type: horizontal-stack
    cards:

        type: button
        name: Ajouter CR2032
        icon: mdi:plus
        tap_action:
        action: call-service
        service: pile_stock_manager.add_stock
        service_data:
        pile_type: "CR2032"
        quantity: 1

        type: button
        name: Retirer CR2032
        icon: mdi:minus
        tap_action:
        action: call-service
        service: pile_stock_manager.remove_stock
        service_data:
        pile_type: "CR2032"
        quantity: 1


### 📋 Carte Grid Layout
type: grid
title: 🔋 Inventaire Piles
columns: 2
square: false
cards:

    type: statistic
    entity: sensor.stock_cr2450
    name: CR2450
    icon: mdi:battery-outline

    type: statistic
    entity: sensor.stock_cr2032
    name: CR2032
    icon: mdi:battery-outline

    type: statistic
    entity: sensor.stock_cr2025
    name: CR2025
    icon: mdi:battery-outline

    type: statistic
    entity: sensor.stock_cr1620
    name: CR1620
    icon: mdi:battery-outline

    type: statistic
    entity: sensor.stock_cr2016
    name: CR2016
    icon: mdi:battery-outline

    type: statistic
    entity: sensor.stock_lr44
    name: LR44
    icon: mdi:battery-outline

    type: statistic
    entity: sensor.stock_aa
    name: AA
    icon: mdi:battery

    type: statistic
    entity: sensor.stock_aaa
    name: AAA
    icon: mdi:battery

## 💡 Exemples d'Utilisation

### 🏠 Cas d'Usage Domestiques

**Gestion Proactive des Capteurs IoT**
Automatisation : Décrémenter automatiquement le stock lors du changement

automation:

    alias: "Changement Pile Capteur Porte"
    trigger:

        platform: state
        entity_id: binary_sensor.capteur_porte_entree_batterie_faible
        to: 'off'
        from: 'on'
        action:

        service: pile_stock_manager.remove_stock
        data:
        pile_type: "CR2032"
        quantity: 1

        service: notify.mobile_app
        data:
        message: "Pile CR2032 changée sur capteur porte. Stock restant: {{ states('sensor.stock_cr2032') }}"

**Planification des Achats**
Automatisation : Alerte d'achat avec liste de courses

automation:

    alias: "Liste Courses Piles"
    trigger:

        platform: time
        at: "09:00:00"
        condition:

        condition: template
        value_template: >
        {{ states('sensor.stock_cr2032')|int < 3 or
        states('sensor.stock_aa')|int < 5 or
        states('sensor.stock_aaa')|int < 5 }}
        action:

        service: shopping_list.add_item
        data:
        name: >
        Piles à acheter:
        {% if states('sensor.stock_cr2032')|int < 3 %}CR2032 ({{ states('sensor.stock_cr2032') }} restantes) {% endif %}
        {% if states('sensor.stock_aa')|int < 5 %}AA ({{ states('sensor.stock_aa') }} restantes) {% endif %}
        {% if states('sensor.stock_aaa')|int < 5 %}AAA ({{ states('sensor.stock_aaa') }} restantes) {% endif %}

### 📊 Tableau de Bord Avancé

**Carte Vue d'Ensemble avec Indicateurs Visuels**
type: vertical-stack
title: 🔋 Centre de Gestion Piles
cards:

    type: horizontal-stack
    cards:

        type: statistic
        entity: sensor.stock_total_piles
        name: "Stock Total"
        icon: mdi:battery-check

        type: statistic
        entity: sensor.stock_cr2032
        name: "CR2032 (IoT)"
        icon: mdi:chip

        type: statistic
        entity: sensor.stock_aa
        name: "AA (Télécommandes)"
        icon: mdi:remote

    type: custom:bar-card
    entities:

        entity: sensor.stock_cr2450
        name: "CR2450"
        max: 10

        entity: sensor.stock_cr2032
        name: "CR2032"
        max: 20

        entity: sensor.stock_aa
        name: "AA"
        max: 30

        entity: sensor.stock_aaa
        name: "AAA"
        max: 25
        severity:

        from: 0
        to: 2
        color: red

        from: 3
        to: 5
        color: orange

        from: 6
        to: 100
        color: green

### 🔄 Intégrations Avancées

**Synchronisation avec Battery Notes**
Template sensor pour combiner stock et état des capteurs

sensor:

    platform: template
    sensors:
    batterie_critique_count:
    friendly_name: "Capteurs Critiques"
    value_template: >
    {% set ns = namespace(count=0) %}
    {% for state in states.sensor %}
    {% if 'battery' in state.entity_id and state.state|int < 20 %}
    {% set ns.count = ns.count + 1 %}
    {% endif %}
    {% endfor %}
    {{ ns.count }}

    stock_suffisant_cr2032:
    friendly_name: "Stock CR2032 Suffisant"
    value_template: >
    {% set stock = states('sensor.stock_cr2032')|int %}
    {% set critique = states('sensor.batterie_critique_count')|int %}
    {{ stock >= critique * 2 }}

**Historique et Statistiques**
Capteur pour suivre la consommation mensuelle

sensor:

    platform: history_stats
    name: "Piles CR2032 Utilisées ce Mois"
    entity_id: sensor.stock_cr2032
    state: 'decreasing'
    type: count
    start: "{{ now().replace(day=1).replace(hour=0).replace(minute=0).replace(second=0) }}"
    end: "{{ now() }}"

### 🚨 Notifications Intelligentes

**Système d'Alertes Multi-Canal**
automation:

    alias: "Alerte Stock Critique Multi-Canal"
    trigger:

        platform: numeric_state
        entity_id:

            sensor.stock_cr2032

            sensor.stock_aa
            below: 2
            action:

        choose:

            conditions:

                condition: time
                after: "08:00:00"
                before: "22:00:00"
                sequence:

                service: notify.mobile_app
                data:
                title: "🔋 Stock Critique"
                message: "{{ trigger.to_state.attributes.friendly_name }} : {{ trigger.to_state.state }} restantes"
                data:
                actions:
                - action: "add_stock"
                title: "Commander"

            conditions:

                condition: time
                after: "22:00:00"
                before: "08:00:00"
                sequence:

                service: persistent_notification.create
                data:
                title: "Stock Piles Faible"
                message: "Vérifier le stock au réveil"

### 🎯 Cas d'Usage Spécialisés

**Gestion pour Maintenance Préventive**
Input datetime pour planifier les maintenances

input_datetime:
prochaine_maintenance_piles:
name: "Prochaine Vérification Piles"
has_date: true
has_time: true

automation:

    alias: "Maintenance Préventive Piles"
    trigger:

        platform: time
        at: input_datetime.prochaine_maintenance_piles
        action:

        service: script.verification_complete_piles

        service: input_datetime.set_datetime
        target:
        entity_id: input_datetime.prochaine_maintenance_piles
        data:
        date: "{{ (now() + timedelta(months=3)).strftime('%Y-%m-%d') }}"

script:
verification_complete_piles:
sequence:
- service: notify.family
data:
message: >
📋 Maintenance Piles Programmée:
- CR2032: {{ states('sensor.stock_cr2032') }} unités
- AA: {{ states('sensor.stock_aa') }} unités
- AAA: {{ states('sensor.stock_aaa') }} unités
- Total: {{ states('sensor.stock_total_piles') }} piles

**Intégration avec Système de Courses**
Script pour génération automatique de liste de courses

script:
generer_liste_courses_piles:
sequence:
- service: shopping_list.clear_completed_items
- repeat:
for_each:
- { type: "CR2450", min: 5, pack: 2 }
- { type: "CR2032", min: 8, pack: 5 }
- { type: "AA", min: 12, pack: 8 }
- { type: "AAA", min: 10, pack: 8 }
sequence:
- condition: template
value_template: >
{{ states('sensor.stock_' + repeat.item.type.lower())|int < repeat.item.min }}
- service: shopping_list.add_item
data:
name: >
🔋 {{ repeat.item.type }} - Pack de {{ repeat.item.pack }}
({{ states('sensor.stock_' + repeat.item.type.lower()) }} restantes)

### 📱 Interface Mobile Optimisée

**Widget pour Companion App**
Configuration pour widget Android/iOS

sensor:

    platform: template
    sensors:
    widget_piles_resume:
    friendly_name: "Résumé Piles"
    value_template: >
    CR2032:{{ states('sensor.stock_cr2032') }}
    AA:{{ states('sensor.stock_aa') }}
    AAA:{{ states('sensor.stock_aaa') }}
    icon_template: >
    {% if states('sensor.stock_total_piles')|int < 10 %}
    mdi:battery-alert
    {% else %}
    mdi:battery-check
    {% endif %}

## 🔄 Automatisations Exemple

### Alerte Stock Faible
automation:

    alias: "Alerte Stock Piles Faible"
    trigger:

        platform: numeric_state
        entity_id: sensor.stock_cr2032
        below: 3
        action:

        service: notify.mobile_app
        data:
        message: "Stock de piles CR2032 faible : {{ states('sensor.stock_cr2032') }} restantes"

### Mise à Jour Stock Automatique
automation:

    alias: "Changement Pile Télécommande"
    trigger:

        platform: state
        entity_id: binary_sensor.telecommande_batterie_faible
        to: 'on'
        action:

        service: pile_stock_manager.remove_stock
        data:
        pile_type: "CR2032"
        quantity: 1

## 💾 Stockage des Données

Les données de stock sont sauvegardées dans le fichier `pile_stock.json` situé dans le répertoire de configuration de Home Assistant. Ce fichier est créé automatiquement lors de la première utilisation et mis à jour à chaque modification du stock.

**Structure du fichier :**
{
"CR2450": 5,
"CR2032": 12,
"CR2025": 3,
"CR1620": 0,
"CR2016": 2,
"LR44": 8,
"AA": 16,
"AAA": 20
}

## 🐛 Dépannage

### Les capteurs ne se mettent pas à jour
- Vérifiez les logs Home Assistant pour les erreurs
- Redémarrez Home Assistant
- Les capteurs utilisent `force_update = True` pour garantir les mises à jour

### Perte des données de stock
- Vérifiez la présence du fichier `pile_stock.json` dans le dossier de configuration
- Vérifiez les permissions d'écriture sur le dossier de configuration

### Service non disponible
- Assurez-vous que l'intégration est correctement installée et configurée
- Vérifiez que le domaine `pile_stock_manager` apparaît dans **Outils de développement** → **Services**

## 📝 Logs et Debug

Pour activer les logs de debug, ajoutez cette configuration dans `configuration.yaml` :
logger:
logs:
custom_components.pile_stock_manager: debug

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

- Signaler des bugs via les [Issues](https://github.com/votre-username/pile-stock-manager/issues)
- Proposer de nouvelles fonctionnalités
- Soumettre des Pull Requests
- Améliorer la documentation

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- Communauté Home Assistant pour l'inspiration
- HACS pour simplifier les installations d'intégrations personnalisées















