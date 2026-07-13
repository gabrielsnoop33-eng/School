# School
Clean architecture final project
# EduCore

## Description

EduCore est une application de gestion universitaire développée dans le cadre d'un projet académique. Elle applique les principes de la **Clean Architecture** afin de produire un code modulaire, maintenable et facile à tester.

L'objectif principal est de gérer les étudiants, les cours, les enseignants et les inscriptions tout en respectant une séparation claire des responsabilités entre les différentes couches de l'application.

---

## Fonctionnalités

* Gestion des étudiants
* Gestion des cours
* Gestion des enseignants
* Inscription des étudiants aux cours
* Gestion des devoirs
* Attribution des notes
* Consultation des informations académiques

---

## Architecture

Le projet est organisé selon les principes de la Clean Architecture.

```
src/
│
├── entities/
│   ├── student.py
│   ├── course.py
│   ├── instructor.py
│   ├── enrollment.py
│   └── assignment.py
│
├── use_cases/
│
├── interfaces/
│
├── repositories/
│
└── main.py
```

### Les différentes couches

* **Entities** : Contient les objets métier et leurs règles.
* **Use Cases** : Contient la logique métier de l'application.
* **Interfaces** : Assure la communication entre les cas d'utilisation et l'extérieur.
* **Repositories** : Gère l'accès aux données.

---

## Technologies utilisées

* Python 3
* Git
* GitHub
* Visual Studio Code

---

## Installation

1. Cloner le dépôt :

```bash
git clone <url-du-repository>
```

2. Accéder au projet :

```bash
cd EduCore
```

3. Exécuter le projet :

```bash
python main.py
```

---

## Auteurs

Projet réalisé dans le cadre du cours de Computer Science.

---

## Licence

Ce projet est destiné à un usage académique et éducatif.
