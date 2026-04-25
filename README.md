# 📊 LogAnalyzer Pro

**LogAnalyzer Pro** est une solution d'orchestration modulaire conçue pour l'analyse automatisée de fichiers logs. Cet outil permet de transformer des données brutes en rapports exploitables tout en assurant l'archivage sécurisé de vos historiques.

---

## 🎯 Pourquoi utiliser LogAnalyzer Pro ?

Cet outil est indispensable pour tout administrateur système ou développeur souhaitant :

*   **🛡️ Renforcer la Sécurité** : Identifiez instantanément les adresses IP suspectes et les tentatives d'accès non autorisées (erreurs 403) ou les scans de vulnérabilités (erreurs 404 répétives).
*   **📈 Optimiser les Performances** : Découvrez quelles sont les pages les plus consultées pour mieux prioriser vos optimisations et comprendre le comportement de vos utilisateurs.
*   **🛠️ Faciliter la Maintenance** : Repérez rapidement les liens morts ou les ressources manquantes sur votre serveur grâce au tracking des codes d'erreur HTTP.
*   **🧹 Automatiser l'Entretien** : Ne laissez plus vos fichiers logs encombrer inutilement l'espace disque. Le système d'archivage automatique déplace et horodate vos fichiers après traitement.

---

## 🛠️ Architecture Modulaire

Le projet est divisé en 4 unités fonctionnelles distinctes :

1.  **🔍 Module d'Analyse (`analyser.py`)** : Extraction des statistiques (IP, Status Codes, Pages).
2.  **📄 Module de Rapport (`rapport.py`)** : Génération de synthèses textuelles structurées.
3.  **📂 Module d'Archivage (`archiver.py`)** : Gestion de la rotation et des backups.
4.  **🚀 Orchestrateur (`main.py`)** : Interface CLI pour coordonner le flux de travail.

---

## 🚀 Utilisation

```bash
# Analyse simple
python3 main.py access.log

# Analyse complète avec archivage automatique
python3 main.py access.log --archive
```

---

## 📄 Licence
Ce projet est sous licence MIT. Développé par **BELLOX**.
