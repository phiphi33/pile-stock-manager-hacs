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

text

**Paramètres :**
- `pile_type` (requis) : Type de pile à ajouter
- `quantity` (optionnel) : Quantité à ajouter (défaut: 1)

### `pile_stock_manager.remove_stock`
Retirer des piles du stock

service: pile_stock_manager.remove_stock
data:
pile_type: "AA"
quantity: 2

text

**Paramètres :**
- `pile_type` (requis) : Type de pile à retirer
- `quantity` (optionnel) : Quantité à retirer (défaut: 1)

### `pile_stock_manager.reset_stock`
Remettre à zéro tout l'inventaire

service: pile_stock_manager.reset_stock

text

**⚠️ Attention :** Cette action remet tous les stocks à zéro et ne peut pas être annulée.

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

text

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

text

## 💾 Stockage des Données

Les données de stock sont sauvegardées dans le fichier `pile_stock.json` situé dans le répertoire de configuration de Home Assistant.[5] Ce fichier est créé automatiquement lors de la première utilisation et mis à jour à chaque modification du stock.

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

text

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

text

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


---

**⭐ Si cette intégration vous est utile, n'hésitez pas à laisser une étoile sur GitHub !**
