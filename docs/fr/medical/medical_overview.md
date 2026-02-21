# Synthèse du paysage normatif — dispositifs médicaux

Ce document fournit une vue d'ensemble structurée du cadre réglementaire
applicable aux dispositifs médicaux. Il couvre les principales juridictions
(États-Unis, Union européenne, international), les normes de système de
management de la qualité (ISO 13485), les exigences logicielles (IEC 62304),
la cybersécurité et les articulations entre ces différents référentiels.
L'objectif est de servir de point d'entrée pour naviguer dans la collection
de documents indexés dans le RAG et de permettre une compréhension rapide
des obligations réglementaires à chaque étape du cycle de vie d'un
dispositif médical.

---

## Sommaire

1. [Introduction — pourquoi les normes importent](#1-introduction--pourquoi-les-normes-importent)
2. [Paysage réglementaire international — tableau comparatif](#2-paysage-réglementaire-international--tableau-comparatif)
3. [FDA 21 CFR 820 (QMSR) — design controls, CAPA, production, validation](#3-fda-21-cfr-820-qmsr--design-controls-capa-production-validation)
4. [ISO 13485 — QMS dispositifs médicaux, clauses 4-8](#4-iso-13485--qms-dispositifs-médicaux-clauses-4-8)
5. [EU MDR 2017/745 et IVDR 2017/746](#5-eu-mdr-2017745-et-ivdr-2017746)
6. [IEC 62304 — logiciel médical, classes A/B/C, cycle de vie](#6-iec-62304--logiciel-médical-classes-abc-cycle-de-vie)
7. [Cybersécurité — FDA premarket, SBOM, threat modeling](#7-cybersécurité--fda-premarket-sbom-threat-modeling)
8. [Articulations entre les normes — tableau croisé](#8-articulations-entre-les-normes--tableau-croisé)
9. [Documents indexés dans le RAG](#9-documents-indexés-dans-le-rag)

---

## 1. Introduction — pourquoi les normes importent

### 1.1 Rôle des normes dans le cycle de vie d'un dispositif médical

Les normes et réglementations encadrant les dispositifs médicaux existent
pour garantir la sécurité des patients, l'efficacité des produits et la
traçabilité tout au long de leur cycle de vie. Elles couvrent chaque étape,
depuis la conception initiale jusqu'à la surveillance après mise sur le
marché, en passant par la fabrication, la stérilisation, le conditionnement
et la distribution.

Un dispositif médical, qu'il s'agisse d'un simple pansement adhésif, d'un
implant orthopédique ou d'un logiciel d'aide au diagnostic, est soumis à
un ensemble d'exigences proportionnées au risque qu'il présente pour le
patient ou l'utilisateur. Cette proportionnalité est le fondement de
l'approche réglementaire moderne.

Les normes remplissent plusieurs fonctions essentielles :

- **Harmonisation** : elles fournissent un langage commun entre fabricants,
  organismes notifiés, autorités réglementaires et professionnels de santé.
- **Présomption de conformité** : le respect d'une norme harmonisée permet
  de présumer la conformité aux exigences essentielles d'un règlement.
- **État de l'art** : elles codifient les bonnes pratiques reconnues par
  la communauté scientifique et industrielle.
- **Accès au marché** : elles constituent un prérequis pour obtenir le
  marquage CE en Europe ou la clearance/approval FDA aux États-Unis.

### 1.2 Principaux organismes de réglementation et de normalisation

| Organisme | Juridiction | Rôle principal |
|-----------|-------------|----------------|
| FDA (Food and Drug Administration) | États-Unis | Autorité réglementaire. Évalue et autorise la mise sur le marché des dispositifs médicaux via les voies 510(k), PMA et De Novo. |
| Commission européenne | Union européenne | Édicte les règlements (EU MDR 2017/745, EU IVDR 2017/746) transposés directement dans le droit des États membres. |
| ISO (International Organization for Standardization) | International | Développe des normes consensuelles (ISO 13485, ISO 14971) utilisées mondialement comme référentiels de conformité. |
| IEC (International Electrotechnical Commission) | International | Normes pour les aspects électriques, électroniques et logiciels (IEC 62304, IEC 60601, IEC 62443). |
| IMDRF (International Medical Device Regulators Forum) | International | Forum de convergence réglementaire entre les principales autorités mondiales. |
| Santé Canada | Canada | Autorité réglementaire canadienne. Applique le règlement sur les instruments médicaux (DORS/98-282). |
| TGA (Therapeutic Goods Administration) | Australie | Autorité réglementaire australienne. Gère le registre ARTG. |
| PMDA (Pharmaceuticals and Medical Devices Agency) | Japon | Autorité réglementaire japonaise. Applique la loi PAL (Pharmaceutical Affairs Law). |

### 1.3 Approche fondée sur le risque

Le principe directeur de la réglementation des dispositifs médicaux est
l'approche fondée sur le risque. Plus le risque associé à un dispositif est
élevé, plus les exigences réglementaires sont strictes. Ce principe se
traduit concrètement par des systèmes de classification :

- **FDA** : classe I (risque faible, contrôles généraux), classe II (risque
  modéré, contrôles spéciaux + 510(k)), classe III (risque élevé, PMA).
- **EU MDR** : classe I, IIa, IIb, III selon les règles de l'annexe VIII.
- **EU IVDR** : classe A, B, C, D.
- **ISO 14971** : norme de gestion des risques applicable à tous les
  dispositifs médicaux, indépendamment de la classe.

La gestion des risques selon ISO 14971 constitue le fil conducteur qui
relie toutes les autres normes entre elles. Elle intervient dans la
conception (design controls), la validation logicielle (IEC 62304), la
cybersécurité (IEC 81001-5-1) et la surveillance post-marché (EU MDR
chapitre VII).

---

## 2. Paysage réglementaire international — tableau comparatif

### 2.1 Vue d'ensemble comparative

Le tableau ci-dessous compare les principaux cadres réglementaires
applicables aux dispositifs médicaux à travers six juridictions et le
cadre ISO international.

| Aspect | FDA (États-Unis) | EU MDR (Europe) | ISO (international) | Santé Canada | TGA (Australie) | PMDA (Japon) |
|--------|------------------|-----------------|---------------------|--------------|-----------------|--------------|
| **Cadre juridique** | Federal Food, Drug, and Cosmetic Act (FD&C Act) | Règlement (UE) 2017/745 (MDR) et 2017/746 (IVDR) | Normes volontaires (ISO 13485, ISO 14971) | Loi sur les aliments et drogues + DORS/98-282 | Therapeutic Goods Act 1989 | Pharmaceutical and Medical Device Act (PMD Act) |
| **Classification** | Classe I, II, III | Classe I, IIa, IIb, III | Non applicable (référentiel transversal) | Classe I, II, III, IV | Classe I, IIa, IIb, III | Classe I, II, III, IV |
| **Voie d'approbation principale** | 510(k), PMA, De Novo | Évaluation de conformité par organisme notifié (annexes IX, X, XI) | Certification ISO 13485 par organisme accrédité | Demande d'homologation (classe II-IV) | Inclusion au registre ARTG | Demande de shonin (approbation) |
| **Exigence QMS** | 21 CFR 820 (QMSR, aligné ISO 13485 depuis 2024) | ISO 13485 requis via annexe IX | ISO 13485:2016 | ISO 13485 requis (CMDR) | ISO 13485 requis | ISO 13485 requis (QMS ordinance) |
| **Gestion des risques** | ISO 14971 référencé dans QMSR | ISO 14971 norme harmonisée | ISO 14971:2019 | ISO 14971 requis | ISO 14971 requis | ISO 14971 requis |
| **Surveillance post-marché** | MDR (Medical Device Reporting), 21 CFR 803 | PMS plan, PSUR, rapports de vigilance (chapitres VII et VIII) | Non applicable directement | Déclaration obligatoire des incidents | Système de vigilance TGA | Rapports d'événements indésirables |
| **Identification unique (UDI)** | UDI Rule (21 CFR 801.20), base GUDID | Système UDI, base EUDAMED (article 27) | Non applicable | UDI obligatoire (harmonisé IMDRF) | UDI en cours de déploiement | UDI en cours d'implémentation |
| **Évaluation clinique** | Clinical trials (IDE), clinical data pour PMA | Évaluation clinique (article 61), investigations cliniques (chapitre VI) | ISO 14155 (investigations cliniques) | Preuves cliniques requises | Preuves cliniques requises | Données cliniques pour shonin |
| **Logiciel (SaMD)** | FDA guidance SaMD, IEC 62304 référencé | IEC 62304 norme harmonisée, MDCG guidances | IEC 62304:2006+A1:2015 | SaMD framework (IMDRF) | Réglementation SaMD spécifique | Réglementation SaMD spécifique |

### 2.2 Convergence internationale via IMDRF

L'IMDRF (International Medical Device Regulators Forum) joue un rôle
central dans l'harmonisation des approches réglementaires. Ses principaux
documents de convergence incluent :

- **IMDRF/SaMD N12** : cadre de classification des logiciels en tant que
  dispositif médical (SaMD), basé sur la signification de l'information
  fournie et l'état de santé visé.
- **IMDRF/UDI** : système d'identification unique des dispositifs, adopté
  progressivement par toutes les juridictions membres.
- **IMDRF/MDSAP** : programme d'audit unique (Medical Device Single Audit
  Program) reconnu par cinq autorités (FDA, Santé Canada, TGA, ANVISA,
  PMDA).

Le document IMDRF N47 sur le SaMD, indexé dans le RAG, détaille le cadre
de qualification et de classification des logiciels médicaux.

---

## 3. FDA 21 CFR 820 (QMSR) — design controls, CAPA, production, validation

### 3.1 Contexte et transition vers le QMSR

Le 21 CFR Part 820, historiquement connu sous le nom de Quality System
Regulation (QSR), constitue le fondement réglementaire du système de
management de la qualité pour les dispositifs médicaux commercialisés aux
États-Unis. En février 2024, la FDA a publié la règle finale établissant
le Quality Management System Regulation (QMSR), qui aligne le 21 CFR 820
sur la norme ISO 13485:2016.

Les points clés de cette transition sont les suivants :

- **Incorporation par référence** : le QMSR incorpore ISO 13485:2016
  comme exigence réglementaire, plutôt que de maintenir un texte
  réglementaire séparé et divergent.
- **Période de transition** : les fabricants disposent d'un délai pour se
  conformer au nouveau cadre (date d'entrée en vigueur : 2 février 2026).
- **Exigences FDA-spécifiques** : certaines exigences propres à la FDA
  subsistent et s'ajoutent à ISO 13485 (notamment les rapports de
  plaintes, les MDR et les exigences de traçabilité).
- **Gestion des risques** : ISO 14971 est explicitement référencée comme
  méthode de gestion des risques dans le QMSR.

### 3.2 Design controls (historiquement 21 CFR 820.30)

Les design controls représentent l'un des piliers du système qualité FDA.
Ils s'appliquent à tous les dispositifs de classe II et III, ainsi qu'à
certains dispositifs de classe I listés spécifiquement. Le diagramme en
cascade (waterfall) des design controls suit une séquence logique.

#### Éléments des design controls

| Étape | Référence historique | Correspondance ISO 13485 | Description |
|-------|---------------------|--------------------------|-------------|
| Design and development planning | 820.30(b) | 7.3.2 | Planification des activités de conception, incluant les revues, vérifications et validations prévues. |
| Design input | 820.30(c) | 7.3.3 | Exigences relatives au dispositif : performances, sécurité, compatibilité, normes applicables. |
| Design output | 820.30(d) | 7.3.4 | Résultats de la conception : spécifications, dessins, procédures de fabrication, critères d'acceptation. |
| Design review | 820.30(e) | 7.3.5 | Revues formelles et documentées à des étapes définies du processus de conception. |
| Design verification | 820.30(f) | 7.3.6 | Confirmation que les design outputs satisfont les design inputs (le produit est-il conforme aux spécifications ?). |
| Design validation | 820.30(g) | 7.3.7 | Confirmation que le dispositif final répond aux besoins de l'utilisateur et à l'usage prévu (le bon produit a-t-il été conçu ?). |
| Design transfer | 820.30(h) | 7.3.8 | Transfert des spécifications de conception vers la production, garantissant la reproductibilité. |
| Design changes | 820.30(i) | 7.3.9 | Maîtrise des modifications de conception, incluant évaluation, vérification et validation le cas échéant. |

#### Distinction vérification vs validation

La distinction entre vérification et validation est fondamentale :

- **Vérification** : « Avons-nous conçu le produit correctement ? » —
  tests, inspections, analyses démontrant que chaque design output est
  conforme au design input correspondant.
- **Validation** : « Avons-nous conçu le bon produit ? » — démonstration
  que le dispositif final répond aux besoins de l'utilisateur dans des
  conditions d'utilisation réelles ou simulées.

La FDA Design Controls Guidance, indexée dans le RAG, fournit des exemples
détaillés et des recommandations pour chaque étape.

### 3.3 CAPA (historiquement 21 CFR 820.90)

Le système de CAPA (Corrective and Preventive Action) est historiquement
le sous-système le plus fréquemment cité lors des inspections FDA. Avec
le QMSR, les exigences CAPA sont désormais alignées sur les clauses
8.5.2 (action corrective) et 8.5.3 (action préventive) d'ISO 13485.

Les étapes d'un processus CAPA complet sont les suivantes :

1. **Identification** : détection du problème via plaintes, audits, données
   de production, surveillance post-marché ou non-conformités internes.
2. **Évaluation** : détermination de la portée et de la gravité du problème.
3. **Investigation** : analyse des causes racines (root cause analysis)
   utilisant des outils tels que le diagramme d'Ishikawa, les 5 pourquoi
   ou l'analyse par arbre de défaillances.
4. **Plan d'action** : définition des actions correctives (éliminer la
   cause du problème existant) et/ou préventives (empêcher l'occurrence
   d'un problème potentiel).
5. **Mise en oeuvre** : exécution des actions planifiées avec des
   responsabilités et des échéances définies.
6. **Vérification d'efficacité** : confirmation que les actions mises en
   oeuvre ont résolu le problème et n'ont pas introduit de nouveaux risques.
7. **Clôture et documentation** : enregistrement complet du processus CAPA
   dans le système qualité.

### 3.4 Production et contrôles de processus

Les exigences relatives à la production couvrent :

- **Contrôles de production** : procédures documentées, environnements
  contrôlés, équipements qualifiés et personnel formé.
- **Validation des processus** : obligatoire pour tout processus dont le
  résultat ne peut pas être entièrement vérifié par une inspection ou un
  test ultérieur (par exemple : stérilisation, soudure, moulage par
  injection, sérigraphie).
- **Contrôles environnementaux** : salles propres, contrôle de la
  température et de l'humidité, selon les exigences du produit.
- **Contrôle des équipements** : maintenance préventive, étalonnage et
  qualification des équipements de production et de mesure.

### 3.5 Device master record et device history record

| Enregistrement | Contenu | Objectif |
|----------------|---------|----------|
| Device master record (DMR) | Spécifications du dispositif, procédures de fabrication, exigences du système qualité, spécifications d'emballage et d'étiquetage. | Définir « comment fabriquer » le dispositif. |
| Device history record (DHR) | Enregistrements de production pour chaque lot/unité : dates de fabrication, quantités, critères d'acceptation, résultats de tests, personnel impliqué. | Démontrer que chaque dispositif a été fabriqué conformément au DMR. |
| Quality system record (QSR) | Procédures, politique qualité, objectifs qualité, rapports d'audit, CAPA, revues de direction. | Documenter le fonctionnement du système qualité dans son ensemble. |
| Complaint files | Enregistrements de toutes les plaintes reçues, évaluations, investigations et actions entreprises. | Assurer la traçabilité et le traitement systématique des retours terrain. |

### 3.6 Tableau récapitulatif des sous-parties clés du 21 CFR 820

| Sous-partie | Sujet | Clauses ISO 13485 correspondantes |
|-------------|-------|------------------------------------|
| Subpart A | Dispositions générales, champ d'application | 1, 4.1 |
| Subpart B | Exigences du système qualité | 4.1, 4.2, 5.1, 5.4, 5.5, 5.6 |
| Subpart C | Design controls | 7.3 |
| Subpart D | Document controls | 4.2.3, 4.2.4 |
| Subpart E | Purchasing controls | 7.4 |
| Subpart F | Identification et traçabilité | 7.5.3, 7.5.9 |
| Subpart G | Production and process controls | 7.5.1, 7.5.2, 7.5.6 |
| Subpart H | Acceptance activities | 7.5.7, 8.2.4 |
| Subpart I | Nonconforming product | 8.3 |
| Subpart J | Corrective and preventive action | 8.5.2, 8.5.3 |
| Subpart K | Labeling and packaging control | 7.5.1 |
| Subpart L | Handling, storage, distribution | 7.5.5, 7.5.11 |
| Subpart M | Records | 4.2.4, 4.2.5 |
| Subpart N | Servicing | 7.5.4 |
| Subpart O | Statistical techniques | 8.2.3, 8.2.4 |

---

## 4. ISO 13485 — QMS dispositifs médicaux, clauses 4-8

### 4.1 Objet et domaine d'application

ISO 13485:2016 spécifie les exigences relatives au système de management
de la qualité (SMQ) pour les organismes qui doivent démontrer leur aptitude
à fournir des dispositifs médicaux et des services associés conformes aux
exigences des clients et aux exigences réglementaires applicables.

Points clés :

- La norme est applicable à tout organisme impliqué dans le cycle de vie
  d'un dispositif médical : conception, fabrication, stockage, distribution,
  installation, maintenance et mise hors service.
- Elle est indépendante de la taille de l'organisme et du type de
  dispositif médical produit.
- Contrairement à ISO 9001, ISO 13485 met l'accent sur la conformité
  réglementaire et la sécurité du produit plutôt que sur l'amélioration
  continue et la satisfaction client.
- Depuis le QMSR, ISO 13485 a une force réglementaire directe aux
  États-Unis en plus de son utilisation comme norme harmonisée en Europe.

### 4.2 Clause 4 — système de management de la qualité

#### 4.2.1 Exigences générales (clause 4.1)

L'organisme doit établir, documenter, mettre en oeuvre et entretenir un
système de management de la qualité et en maintenir l'efficacité. Cela
inclut :

- La détermination des processus nécessaires au SMQ et leur application
  dans tout l'organisme.
- La détermination de la séquence et de l'interaction de ces processus.
- La détermination des critères et méthodes nécessaires pour assurer
  l'efficacité du fonctionnement et de la maîtrise de ces processus.
- L'application d'une approche fondée sur le risque à la maîtrise des
  processus du SMQ.

#### 4.2.2 Exigences relatives à la documentation (clause 4.2)

| Type de document | Exigence | Exemples |
|------------------|----------|----------|
| Politique qualité | Obligatoire, approuvée par la direction. | Engagement envers la conformité réglementaire et l'efficacité du SMQ. |
| Objectifs qualité | Mesurables, cohérents avec la politique qualité. | Taux de CAPA clôturées dans les délais, taux de non-conformités récurrentes. |
| Manuel qualité | Domaine d'application du SMQ, procédures documentées ou références, description des interactions entre processus. | Document maître du système qualité. |
| Procédures documentées | Requises par la norme pour des processus spécifiques. | Maîtrise des documents, maîtrise des enregistrements, audit interne, CAPA. |
| Enregistrements | Preuves de conformité et de fonctionnement efficace du SMQ. | Rapports de revue de conception, résultats de validation, enregistrements de formation. |
| Dossier du dispositif médical | Pour chaque type ou famille de dispositif médical. | Spécifications, procédures de fabrication, dossier de gestion des risques. |

### 4.3 Clause 5 — responsabilité de la direction

La direction doit démontrer son engagement envers le SMQ par les actions
suivantes :

- **Engagement de la direction** (5.1) : communication de l'importance de
  satisfaire les exigences réglementaires et clients, établissement de la
  politique qualité et des objectifs qualité.
- **Orientation client** (5.2) : les exigences des clients et les exigences
  réglementaires sont déterminées et satisfaites.
- **Politique qualité** (5.3) : appropriée à la finalité de l'organisme,
  communiquée et comprise à tous les niveaux pertinents.
- **Planification** (5.4) : les objectifs qualité sont établis aux
  fonctions et niveaux pertinents ; la planification du SMQ est réalisée
  pour satisfaire les exigences de la clause 4.1 et les objectifs qualité.
- **Représentant de la direction** (5.5.2) : un membre de la direction est
  désigné pour s'assurer que les processus du SMQ sont établis, mis en
  oeuvre et entretenus.
- **Revue de direction** (5.6) : revue planifiée du SMQ à intervalles
  définis, incluant les éléments d'entrée (audits, retours clients,
  performance des processus, CAPA) et les éléments de sortie (amélioration,
  besoins en ressources).

### 4.4 Clause 6 — management des ressources

| Sous-clause | Sujet | Exigences clés |
|-------------|-------|----------------|
| 6.1 | Mise à disposition des ressources | L'organisme détermine et fournit les ressources nécessaires au SMQ. |
| 6.2 | Ressources humaines | Compétence basée sur la formation initiale, la formation professionnelle, le savoir-faire et l'expérience. Enregistrements de formation obligatoires. |
| 6.3 | Infrastructure | Bâtiments, équipements, services supports (transport, communication, systèmes d'information). Documentation des exigences de maintenance. |
| 6.4 | Environnement de travail et maîtrise de la contamination | Conditions de travail nécessaires pour la conformité du produit. Exigences spécifiques pour les salles propres et la prévention de la contamination. |

### 4.5 Clause 7 — réalisation du produit

Cette clause est la plus volumineuse de la norme et couvre l'ensemble du
processus de réalisation du dispositif médical.

#### 7.1 — Planification de la réalisation du produit

L'organisme planifie et développe les processus nécessaires à la
réalisation du produit, en cohérence avec les exigences du SMQ. La
planification doit inclure, selon le cas : les objectifs qualité et les
exigences relatives au produit, les processus et ressources spécifiques,
les activités de vérification et de validation, les critères d'acceptation
et les enregistrements nécessaires.

La gestion des risques selon ISO 14971 doit être intégrée à la
planification de la réalisation du produit.

#### 7.2 — Processus relatifs aux clients

Détermination des exigences relatives au produit (spécifiées par le client,
non formulées mais nécessaires, réglementaires) et revue de ces exigences
avant engagement de l'organisme.

#### 7.3 — Conception et développement

La clause 7.3 détaille les exigences relatives au processus de conception
et développement, en miroir des design controls FDA :

- 7.3.1 : Dispositions générales.
- 7.3.2 : Planification de la conception et du développement.
- 7.3.3 : Éléments d'entrée de la conception et du développement.
- 7.3.4 : Éléments de sortie de la conception et du développement.
- 7.3.5 : Revue de la conception et du développement.
- 7.3.6 : Vérification de la conception et du développement.
- 7.3.7 : Validation de la conception et du développement.
- 7.3.8 : Transfert de la conception et du développement.
- 7.3.9 : Maîtrise des modifications de la conception et du développement.
- 7.3.10 : Dossiers de conception et de développement.

#### 7.4 — Achats

Maîtrise des fournisseurs et des produits achetés : évaluation et sélection
des fournisseurs, spécifications d'achat, vérification du produit acheté.

#### 7.5 — Production et prestation de service

- 7.5.1 : Maîtrise de la production et de la prestation de service.
- 7.5.2 : Propreté du produit.
- 7.5.3 : Activités d'installation.
- 7.5.4 : Activités de service après-vente.
- 7.5.5 : Exigences particulières pour les dispositifs médicaux stériles.
- 7.5.6 : Validation des processus de production et de prestation de
  service.
- 7.5.7 : Exigences particulières pour la validation des processus de
  stérilisation et des systèmes de barrière stérile.
- 7.5.8 : Identification.
- 7.5.9 : Traçabilité.
- 7.5.10 : Propriété du client.
- 7.5.11 : Préservation du produit.

#### 7.6 — Maîtrise des équipements de surveillance et de mesure

Étalonnage, vérification à intervalles définis, enregistrements des
résultats d'étalonnage et traçabilité métrologique.

### 4.6 Clause 8 — mesure, analyse et amélioration

| Sous-clause | Sujet | Exigences clés |
|-------------|-------|----------------|
| 8.1 | Généralités | Planification des processus de surveillance, de mesure, d'analyse et d'amélioration. |
| 8.2.1 | Retour d'information | Système de collecte et d'analyse des retours d'information, y compris les plaintes, comme élément d'entrée de la surveillance post-marché. |
| 8.2.2 | Traitement des plaintes | Procédure documentée pour la réception, l'évaluation et l'investigation des plaintes en temps opportun. |
| 8.2.3 | Signalement aux autorités réglementaires | Procédure documentée pour le signalement des événements répondant aux critères de notification. |
| 8.2.4 | Audit interne | Programme d'audit à intervalles planifiés, auditeurs indépendants et compétents, suivi des actions correctives. |
| 8.2.5 | Surveillance et mesure des processus | Méthodes appropriées de surveillance des processus du SMQ. |
| 8.2.6 | Surveillance et mesure du produit | Vérification de la conformité du produit aux exigences à des étapes appropriées. |
| 8.3 | Maîtrise du produit non conforme | Identification, documentation, séparation et traitement du produit non conforme. Évaluation de la nécessité d'une investigation et notification aux parties responsables. |
| 8.4 | Analyse des données | Collecte et analyse des données pour démontrer la pertinence et l'efficacité du SMQ et identifier les opportunités d'amélioration. |
| 8.5.1 | Généralités (amélioration) | Identification et mise en oeuvre des modifications nécessaires pour l'adéquation et l'efficacité continues du SMQ. |
| 8.5.2 | Action corrective | Procédure documentée : détermination des non-conformités, causes, actions, vérification d'efficacité. |
| 8.5.3 | Action préventive | Procédure documentée : détermination des non-conformités potentielles, causes, actions, vérification d'efficacité. |

---

## 5. EU MDR 2017/745 et IVDR 2017/746

### 5.1 Transition de la MDD au MDR — chronologie

Le règlement (UE) 2017/745 relatif aux dispositifs médicaux (MDR) remplace
les directives antérieures 93/42/CEE (MDD) et 90/385/CEE (AIMDD). La
transition a suivi le calendrier suivant :

| Date | Événement |
|------|-----------|
| 5 avril 2017 | Publication du règlement EU MDR 2017/745 au Journal officiel de l'UE. |
| 25 mai 2017 | Entrée en vigueur du MDR (début de la période de transition). |
| 26 mai 2020 | Date d'application initialement prévue (reportée en raison de la COVID-19). |
| 26 mai 2021 | Date d'application effective du MDR. |
| 26 mai 2024 | Fin de la période de transition pour les dispositifs certifiés sous MDD (certificats MDD valides). |
| 31 décembre 2027 | Date limite étendue pour la mise sur le marché de dispositifs couverts par des certificats MDD (sous conditions). |
| 31 décembre 2028 | Date limite étendue pour les dispositifs de classe III et les implantables couverts par des certificats MDD. |

**Note** : les dates de transition ont été modifiées par le règlement
(UE) 2023/607 pour éviter des ruptures d'approvisionnement en dispositifs
médicaux sur le marché européen.

### 5.2 Règles de classification (annexe VIII)

Le MDR définit 22 règles de classification réparties en quatre catégories
de dispositifs.

| Classe | Niveau de risque | Exemples | Règles principales |
|--------|------------------|----------|--------------------|
| I | Faible | Pansements non stériles, fauteuils roulants manuels, stéthoscopes. | Règles 1-4 (dispositifs non invasifs). |
| I stérile / I avec fonction de mesurage / I réutilisable chirurgical | Faible (avec exigences supplémentaires) | Gants d'examen stériles, seringues, instruments chirurgicaux réutilisables. | Règles 1-4 avec conditions spéciales. |
| IIa | Modéré | Appareils auditifs, lentilles de contact, cathéters urinaires à court terme. | Règles 5-8 (invasifs à court terme), règles 9-13 (dispositifs actifs). |
| IIb | Modéré-élevé | Ventilateurs pulmonaires, hémodialyseurs, stents uretéraux. | Règles 5-8 (invasifs à long terme), règle 11 (logiciels diagnostiques). |
| III | Élevé | Valves cardiaques, prothèses de hanche, stents coronariens, implants mammaires. | Règle 6 (contact SNC/coeur), règle 8 (implantables à long terme). |

#### Règle 11 — classification des logiciels

La règle 11 du MDR est particulièrement importante pour les logiciels :

- Les logiciels destinés à fournir des informations utilisées pour prendre
  des décisions à des fins de diagnostic ou de traitement sont classés en
  classe IIa, sauf si ces décisions peuvent entraîner :
  - La mort ou une détérioration irréversible de l'état de santé → classe III.
  - Une détérioration grave de l'état de santé ou une intervention
    chirurgicale → classe IIb.
- Les logiciels destinés à surveiller des processus physiologiques sont
  classés en classe IIa, sauf s'ils surveillent des paramètres vitaux et
  que des variations peuvent présenter un danger immédiat → classe IIb.
- Tous les autres logiciels sont classés en classe I.

### 5.3 Voies d'évaluation de la conformité

| Annexe | Application | Organismes impliqués |
|--------|-------------|----------------------|
| Annexe IX | Évaluation de la conformité fondée sur un système de management de la qualité et sur l'évaluation de la documentation technique. Applicable à toutes les classes (chapitre I pour le QMS, chapitre II pour l'évaluation de la documentation technique, chapitre III pour l'examen de type). | Organisme notifié (pour classes Is, Im, Ir, IIa, IIb, III). |
| Annexe X | Évaluation de la conformité fondée sur l'examen de type. Combinée avec l'annexe XI. | Organisme notifié. |
| Annexe XI | Évaluation de la conformité fondée sur la vérification de la conformité du produit (partie A : assurance qualité de la production ; partie B : vérification du produit). | Organisme notifié. |

Pour les dispositifs de classe I (non stériles, sans fonction de mesurage,
non réutilisables chirurgicaux), le fabricant procède à une auto-évaluation
de la conformité sans intervention d'un organisme notifié.

### 5.4 Exigences générales en matière de sécurité et de performances (GSPR)

L'annexe I du MDR remplace les « exigences essentielles » de la MDD par
les « exigences générales en matière de sécurité et de performances »
(GSPR — General Safety and Performance Requirements). Elles sont organisées
en trois chapitres :

1. **Chapitre I — exigences générales** (GSPR 1-9) : sécurité générale,
   gestion des risques (acceptabilité du risque résiduel), performances
   cliniques, durée de vie, transport et stockage.
2. **Chapitre II — exigences relatives à la conception et à la fabrication**
   (GSPR 10-22) : propriétés chimiques, physiques et biologiques ;
   infection et contamination microbienne ; compatibilité avec
   l'environnement d'utilisation ; exigences pour les dispositifs actifs,
   logiciels et dispositifs connectés.
3. **Chapitre III — exigences relatives aux informations fournies avec le
   dispositif** (GSPR 23) : étiquetage, notice d'utilisation, langues.

### 5.5 Évaluation clinique (article 61)

L'évaluation clinique est un processus continu tout au long du cycle de vie
du dispositif. Elle doit être fondée sur :

- Des données cliniques provenant d'investigations cliniques sur le
  dispositif concerné.
- Des données cliniques provenant d'investigations cliniques ou d'autres
  études rapportées dans la littérature scientifique sur un dispositif
  équivalent démontré.
- Des données cliniques provenant de la surveillance post-marché (en
  particulier le suivi clinique après commercialisation — PMCF).

Le document MDCG 2020-6 (Sufficient Clinical Evidence), indexé dans le RAG,
fournit des orientations sur le niveau de preuves cliniques suffisant pour
chaque classe de dispositif.

### 5.6 Surveillance post-marché et vigilance

Le MDR renforce significativement les exigences de surveillance post-marché
par rapport à la MDD :

| Exigence | Description | Articles MDR |
|----------|-------------|--------------|
| Plan de surveillance post-marché | Document structuré décrivant les méthodes de collecte et d'analyse des données post-marché. | Article 84 |
| Rapport de surveillance post-marché | Résumé des résultats de la surveillance, mis à jour régulièrement. Requis pour les classes I. | Article 85 |
| Rapport périodique actualisé de sécurité (PSUR) | Rapport détaillé incluant les conclusions du rapport bénéfice-risque et le volume de ventes. Requis pour les classes IIa, IIb et III. | Article 86 |
| Suivi clinique après commercialisation (PMCF) | Processus continu de collecte de données cliniques pour confirmer la sécurité et les performances sur toute la durée de vie du dispositif. | Annexe XIV, partie B |
| Vigilance | Signalement des incidents graves et des mesures correctives de sécurité (FSCA) aux autorités compétentes. | Articles 87-92 |
| Analyse des tendances | Augmentation statistiquement significative de la fréquence ou de la gravité des incidents et effets indésirables. | Article 88 |

### 5.7 Identification unique des dispositifs (UDI) et EUDAMED

Le système UDI (Unique Device Identification) est défini aux articles 27
et 28 et à l'annexe VI du MDR. Il comprend :

- **UDI-DI** (Device Identifier) : code identifiant le fabricant et la
  version ou le modèle spécifique du dispositif.
- **UDI-PI** (Production Identifier) : code identifiant l'unité de
  production (numéro de série, numéro de lot, date de fabrication, date
  d'expiration).

EUDAMED (European Database on Medical Devices) est la base de données
européenne centralisée qui doit regrouper six modules : enregistrement des
acteurs économiques, UDI/enregistrement des dispositifs, organismes
notifiés et certificats, investigations cliniques, vigilance et surveillance
post-marché, surveillance du marché.

### 5.8 IVDR 2017/746 — spécificités pour les dispositifs de diagnostic in vitro

Le règlement (UE) 2017/746 (IVDR) s'applique aux dispositifs médicaux de
diagnostic in vitro. Il introduit un changement majeur par rapport à la
directive 98/79/CE (IVDD) : le passage d'un système de classification
basé sur des listes à un système de classification fondé sur des règles.

#### Classification IVDR

| Classe | Niveau de risque | Exemples |
|--------|------------------|----------|
| A | Faible | Milieux de culture généraux, réactifs de laboratoire sans finalité diagnostique spécifique. |
| B | Modéré-faible | Autotests de grossesse, tests de cholestérol, dispositifs de contrôle qualité. |
| C | Modéré-élevé | Tests de dépistage du VIH (pour diagnostic), tests de groupe sanguin ABO, tests de génétique humaine. |
| D | Élevé | Tests de dépistage du VIH (pour sécurité transfusionnelle), tests de détection d'agents transmissibles (sang, organes). |

#### Évaluation des performances (IVDR)

L'IVDR remplace le concept d'« évaluation clinique » (utilisé pour les
dispositifs médicaux au sens du MDR) par l'« évaluation des performances »
(performance evaluation), qui comprend :

- Les études de performances analytiques (sensibilité analytique,
  spécificité analytique, exactitude, répétabilité, reproductibilité).
- Les études de performances cliniques (sensibilité clinique, spécificité
  clinique, valeur prédictive positive et négative).
- L'évaluation des performances scientifiques (revue de la littérature
  et des données disponibles).

### 5.9 Tableau comparatif MDR vs MDD

| Aspect | MDD 93/42/CEE | MDR 2017/745 |
|--------|---------------|--------------|
| Type de texte | Directive (transposition nationale). | Règlement (application directe). |
| Classification | 18 règles, 4 classes. | 22 règles, 4 classes (reclassification de certains dispositifs). |
| Évaluation clinique | Exigence générale, peu détaillée. | Exigences renforcées (article 61), PMCF obligatoire. |
| Surveillance post-marché | Exigences minimales. | PMS plan, PSUR, PMCF, analyse des tendances. |
| UDI | Non requis. | Obligatoire (articles 27-28). |
| Personne responsable de la conformité réglementaire | Non explicitement requis. | Exigence explicite (article 15). |
| Transparence | Limitée. | EUDAMED, résumé de sécurité et de performances cliniques (SSCP). |
| Logiciels | Peu de dispositions spécifiques. | Règle 11 spécifique, GSPR 17 (logiciels). |
| Organismes notifiés | Surveillance limitée. | Surveillance renforcée, audits inopinés, examens de la documentation technique. |
| Dispositifs sur mesure | Exigences allégées. | Exigences renforcées (annexe XIII). |

---

## 6. IEC 62304 — logiciel médical, classes A/B/C, cycle de vie

### 6.1 Domaine d'application

IEC 62304:2006+A1:2015 (Software life cycle processes) définit les
exigences du cycle de vie pour le développement et la maintenance des
logiciels médicaux. Elle s'applique à deux catégories :

- **Software as a Medical Device (SaMD)** : logiciel qui est lui-même un
  dispositif médical (par exemple, un logiciel d'aide au diagnostic
  radiologique).
- **Software in a Medical Device (SiMD)** : logiciel intégré dans un
  dispositif médical (par exemple, le firmware d'un moniteur patient).

La norme est harmonisée au titre du règlement EU MDR 2017/745 et est
référencée dans le QMSR FDA. Elle est applicable conjointement avec
ISO 14971 pour la gestion des risques et ISO 13485 pour le système de
management de la qualité.

### 6.2 Classification de sécurité logicielle

IEC 62304 introduit un système de classification de sécurité propre au
logiciel, distinct de la classification réglementaire du dispositif
médical dans son ensemble.

| Classe logicielle | Définition | Conséquence sur le cycle de vie |
|-------------------|------------|----------------------------------|
| Classe A | Aucune blessure ou atteinte à la santé n'est possible. | Exigences minimales : planification du développement, gestion de la configuration, résolution des problèmes. |
| Classe B | Une blessure non grave est possible. | Exigences intermédiaires : ajout de l'analyse des exigences, de la conception architecturale, des tests d'intégration et de la vérification. |
| Classe C | La mort ou une blessure grave est possible. | Exigences complètes : ajout de la conception détaillée, des tests unitaires et de la traçabilité complète des exigences. |

**Important** : la classification de sécurité logicielle est déterminée par
le processus de gestion des risques (ISO 14971). Un système logiciel peut
être décomposé en sous-systèmes (software items), chacun pouvant avoir une
classification de sécurité différente, à condition que la séparation soit
suffisamment robuste pour éviter qu'un élément de classe inférieure
n'affecte un élément de classe supérieure.

### 6.3 Processus du cycle de vie de développement logiciel

#### 6.3.1 Planification du développement logiciel (clause 5.1)

Le plan de développement logiciel doit documenter :

- Les processus, activités et tâches du cycle de vie applicables.
- Les livrables de chaque activité et tâche.
- La traçabilité entre les exigences du système, les exigences logicielles,
  les tests et la gestion des risques.
- Le modèle de cycle de vie utilisé (en V, agile, itératif, etc.).
- Les standards et méthodes de développement, les outils et le langage
  de programmation.
- La classification de sécurité du logiciel et la stratégie de
  décomposition en sous-systèmes.

#### 6.3.2 Analyse des exigences logicielles (clause 5.2)

Cette étape consiste à définir les exigences logicielles à partir des
exigences système et des exigences de gestion des risques :

- Exigences fonctionnelles et de performance.
- Exigences d'entrée et de sortie (interfaces).
- Exigences de sécurité (résultant de l'analyse des risques).
- Exigences relatives à l'utilisation (ergonomie, aptitude à l'utilisation).
- Exigences relatives aux données et à leur intégrité.
- Exigences d'installation et de maintenance.

#### 6.3.3 Conception architecturale (clause 5.3)

Le logiciel est décomposé en éléments (software items) à un niveau de
détail suffisant pour permettre :

- L'identification de tous les éléments logiciels et de leurs interfaces.
- La description de la manière dont le logiciel est structuré pour
  répondre aux exigences.
- L'identification des éléments logiciels SOUP (Software of Unknown
  Provenance) — bibliothèques tierces, composants open source, systèmes
  d'exploitation.
- La classification de sécurité de chaque élément logiciel.

#### 6.3.4 Conception détaillée (clause 5.4)

Requise uniquement pour les éléments logiciels de classe C. Elle doit
détailler :

- Les algorithmes, structures de données et interfaces de chaque unité
  logicielle.
- Le niveau de détail permettant l'implémentation correcte et la
  vérification par tests unitaires.

#### 6.3.5 Implémentation et vérification des unités logicielles (clause 5.5)

- Implémentation du code source conformément à la conception détaillée.
- Vérification que chaque unité logicielle satisfait ses spécifications
  (tests unitaires pour classe C, stratégie de vérification pour classe B).
- Critères d'acceptation définis à l'avance pour chaque unité.

#### 6.3.6 Intégration et tests d'intégration (clause 5.6)

- Intégration progressive des éléments logiciels conformément au plan
  d'intégration.
- Tests d'intégration vérifiant que les interfaces entre éléments
  fonctionnent correctement.
- Vérification que les éléments SOUP sont intégrés correctement.
- Documentation des résultats de tests et des anomalies identifiées.

#### 6.3.7 Tests du système logiciel (clause 5.7)

- Tests au niveau du système logiciel complet.
- Vérification que le système logiciel satisfait les exigences logicielles.
- Tests réalisés dans un environnement représentatif de l'environnement
  d'utilisation prévu.
- Couverture des exigences par les tests documentée via une matrice de
  traçabilité.

#### 6.3.8 Libération du logiciel (clause 5.8)

- Vérification que toutes les activités et tâches planifiées ont été
  complétées.
- Documentation de la version libérée et des procédures de construction.
- Traçabilité complète entre exigences, conception, implémentation et
  tests.
- Évaluation des anomalies résiduelles connues (bugs connus et leur
  impact sur la sécurité).

#### 6.3.9 Maintenance logicielle (clause 6)

Le processus de maintenance couvre :

- La surveillance des retours d'information post-marché relatifs au
  logiciel.
- L'analyse et la résolution des problèmes signalés.
- La gestion des modifications du logiciel (évaluation de l'impact,
  reclassification de sécurité si nécessaire).
- La mise en oeuvre des mises à jour et correctifs.

### 6.4 Tableau des activités requises par classe de sécurité

| Activité / Processus | Classe A | Classe B | Classe C |
|-----------------------|----------|----------|----------|
| Planification du développement (5.1) | Requis | Requis | Requis |
| Analyse des exigences (5.2) | Non requis | Requis | Requis |
| Conception architecturale (5.3) | Non requis | Requis | Requis |
| Conception détaillée (5.4) | Non requis | Non requis | Requis |
| Implémentation (5.5.1) | Requis | Requis | Requis |
| Vérification des unités (5.5.2-5.5.5) | Non requis | Non requis | Requis |
| Intégration et tests d'intégration (5.6) | Non requis | Requis | Requis |
| Tests du système logiciel (5.7) | Non requis | Requis | Requis |
| Libération du logiciel (5.8) | Requis | Requis | Requis |
| Gestion de la configuration (clause 8) | Requis | Requis | Requis |
| Résolution des problèmes (clause 9) | Requis | Requis | Requis |
| Maintenance (clause 6) | Requis | Requis | Requis |
| Gestion des risques logiciels (clause 7) | Requis | Requis | Requis |
| Traçabilité des exigences | Non requis | Requis | Requis (complète) |

### 6.5 Gestion des SOUP (Software of Unknown Provenance)

Les SOUP représentent un défi particulier dans le développement de
logiciels médicaux. IEC 62304 exige :

- L'identification de tous les éléments SOUP utilisés (nom, version,
  fabricant).
- La définition des exigences fonctionnelles et de performance pour
  chaque SOUP.
- La vérification que chaque SOUP satisfait les exigences définies.
- La surveillance des anomalies publiées par les fournisseurs de SOUP.
- L'évaluation de l'impact des anomalies SOUP sur la sécurité du logiciel
  médical.

### 6.6 Relations avec les autres normes

| Norme associée | Relation avec IEC 62304 |
|----------------|-------------------------|
| ISO 14971 | Fournit le cadre de gestion des risques utilisé pour la classification de sécurité logicielle et l'identification des exigences de sécurité. |
| ISO 13485 | Fournit le cadre du système de management de la qualité dans lequel les processus IEC 62304 s'intègrent (design controls, CAPA). |
| IEC 62366-1 | Ingénierie de l'aptitude à l'utilisation (usability engineering). Fournit les exigences ergonomiques intégrées dans les exigences logicielles. |
| IEC 82304-1 | Norme pour les logiciels de santé autonomes (health software). Utilise IEC 62304 pour les exigences de cycle de vie. |
| IEC 81001-5-1 | Sécurité, efficacité et sûreté des logiciels de santé et des systèmes TI de santé — sécurité du cycle de vie. Complète IEC 62304 sur les aspects de cybersécurité. |
| IEC 62443 | Sécurité des systèmes d'automatisation industrielle. Référencé pour les aspects de cybersécurité des systèmes médicaux connectés. |

---

## 7. Cybersécurité — FDA premarket, SBOM, threat modeling

### 7.1 Contexte réglementaire

La cybersécurité des dispositifs médicaux est devenue un enjeu majeur avec
la connectivité croissante des systèmes de santé. Les incidents de
cybersécurité peuvent avoir des conséquences directes sur la sécurité des
patients : modification de doses, accès non autorisé aux données de santé,
indisponibilité de dispositifs critiques.

Plusieurs textes réglementaires et normatifs encadrent désormais la
cybersécurité des dispositifs médicaux :

- **FDA** : Premarket Cybersecurity Guidance (septembre 2023), Section 524B
  du FD&C Act (Consolidated Appropriations Act, 2023).
- **EU MDR** : GSPR 17.2 (exigences de cybersécurité), MDCG 2019-16 rev. 1.
- **IEC 81001-5-1** : sécurité dans le cycle de vie des logiciels de santé.
- **IEC 62443** : sécurité des systèmes de contrôle industriel, applicable
  par extension aux systèmes médicaux connectés.
- **AAMI TIR57** : principes de gestion des risques de sécurité pour les
  dispositifs médicaux.

### 7.2 FDA premarket cybersecurity guidance (2023)

Le document FDA « Cybersecurity in Medical Devices: Quality System
Considerations and Content of Premarket Submissions », publié en septembre
2023, constitue la référence principale pour les soumissions premarket aux
États-Unis. Il est indexé dans le RAG sous le nom
`FDA_Cybersecurity_Medical_Devices.pdf`.

Les points essentiels de ce document sont les suivants :

#### Secure Product Development Framework (SPDF)

La FDA recommande l'adoption d'un cadre de développement sécurisé (SPDF)
englobant l'ensemble du cycle de vie du produit. Le SPDF intègre :

- La gestion des risques de sécurité (security risk management).
- L'architecture et la conception sécurisées (secure by design).
- La vérification et la validation de la cybersécurité.
- La gestion de la cybersécurité en phase post-marché.

#### Contenu de la soumission premarket

Pour les dispositifs comportant des éléments logiciels ou connectés, la FDA
attend les informations suivantes dans la soumission premarket :

1. **Description du système** : architecture, composants, flux de données,
   interfaces réseau et protocoles de communication.
2. **Threat model** : identification des menaces potentielles, surfaces
   d'attaque, acteurs malveillants et scénarios de compromission.
3. **Évaluation des risques de cybersécurité** : probabilité et impact des
   menaces identifiées, mesures d'atténuation.
4. **Software Bill of Materials (SBOM)** : inventaire complet de tous les
   composants logiciels (propriétaires, open source, SOUP).
5. **Contrôles de sécurité** : authentification, chiffrement,
   journalisation, contrôle d'accès, intégrité des données.
6. **Plan de gestion de la cybersécurité** : procédures de réponse aux
   vulnérabilités, politique de mise à jour, fin de support.
7. **Tests de cybersécurité** : résultats des tests de pénétration,
   analyses de vulnérabilités, fuzzing, revue de code statique.

### 7.3 Threat modeling — modélisation des menaces

La modélisation des menaces est un processus structuré d'identification
et d'évaluation des risques de cybersécurité. Les méthodologies couramment
utilisées pour les dispositifs médicaux sont les suivantes.

| Méthodologie | Description | Application typique |
|--------------|-------------|---------------------|
| STRIDE | Classification des menaces en six catégories : Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. | Analyse systématique des composants et interfaces du dispositif. |
| CVSS | Common Vulnerability Scoring System. Évaluation quantitative de la gravité des vulnérabilités. | Priorisation des vulnérabilités identifiées et des correctifs. |
| Attack trees | Représentation arborescente des chemins d'attaque possibles pour atteindre un objectif malveillant. | Analyse approfondie de scénarios d'attaque spécifiques. |
| TARA | Threat Assessment and Remediation Analysis. Méthodologie MITRE pour l'identification et la priorisation des contre-mesures. | Évaluation systématique des contre-mesures de cybersécurité. |

Le processus de threat modeling comprend typiquement les étapes suivantes :

1. **Définition du périmètre** : identification des actifs à protéger
   (données patients, fonctions de sécurité, intégrité du dispositif).
2. **Décomposition de l'architecture** : identification des composants,
   interfaces, flux de données et limites de confiance (trust boundaries).
3. **Identification des menaces** : pour chaque composant et interface,
   identification systématique des menaces possibles.
4. **Évaluation des risques** : estimation de la probabilité d'exploitation
   et de l'impact potentiel de chaque menace.
5. **Définition des contre-mesures** : pour chaque menace jugée
   inacceptable, définition des contrôles de sécurité appropriés.
6. **Vérification** : tests de sécurité confirmant l'efficacité des
   contre-mesures.

### 7.4 Software Bill of Materials (SBOM)

Le SBOM est un inventaire structuré et lisible par machine de tous les
composants logiciels intégrés dans un dispositif médical. La FDA exige
un SBOM pour toute soumission premarket de dispositif comportant un
logiciel, conformément à la section 524B du FD&C Act.

Les éléments devant figurer dans un SBOM sont les suivants :

- **Composants propriétaires** : nom, version, fabricant.
- **Composants open source** : nom, version, licence, source.
- **Composants commerciaux tiers** : nom, version, fournisseur.
- **Dépendances** : relations entre composants.
- **Vulnérabilités connues** : CVE associées aux versions utilisées.

Les formats standards de SBOM sont :

- **SPDX** (Software Package Data Exchange) : format ISO/IEC 5962:2021.
- **CycloneDX** : format OWASP optimisé pour l'analyse de sécurité.

### 7.5 Gestion des vulnérabilités et correctifs

La gestion des vulnérabilités tout au long du cycle de vie du dispositif
comprend :

- **Surveillance continue** : veille sur les vulnérabilités publiées (NVD,
  CVE) affectant les composants du dispositif.
- **Évaluation d'impact** : analyse de l'exploitabilité et de l'impact
  potentiel sur la sécurité du patient pour chaque vulnérabilité.
- **Remédiation** : développement, validation et déploiement de correctifs
  dans des délais proportionnés à la criticité.
- **Communication** : notification aux utilisateurs et aux autorités
  (ICS-CERT/CISA pour la FDA, vigilance pour le MDR).

### 7.6 IEC 81001-5-1 — sécurité dans le cycle de vie des logiciels de santé

IEC 81001-5-1:2021 est la norme de référence pour la cybersécurité des
logiciels de santé. Elle est harmonisée sous le MDR et sera de plus en
plus référencée par les autorités réglementaires mondiales.

Les processus clés définis par IEC 81001-5-1 sont les suivants :

| Processus | Description | Lien avec IEC 62304 |
|-----------|-------------|---------------------|
| Planification de la sécurité | Intégration de la cybersécurité dans le plan de développement logiciel. | Extension de la clause 5.1. |
| Exigences de sécurité | Identification des exigences de sécurité à partir du threat model et de l'analyse des risques. | Alimentation de la clause 5.2. |
| Architecture sécurisée | Conception d'une architecture intégrant les principes de défense en profondeur, de moindre privilège et de séparation. | Extension de la clause 5.3. |
| Implémentation sécurisée | Pratiques de codage sécurisé, revue de code, analyse statique. | Extension de la clause 5.5. |
| Tests de sécurité | Tests de pénétration, fuzzing, analyse de vulnérabilités, vérification des contrôles de sécurité. | Extension des clauses 5.6 et 5.7. |
| Gestion de la configuration de sécurité | Gestion sécurisée du code source, des artefacts de build et des clés cryptographiques. | Extension de la clause 8. |
| Gestion des problèmes de sécurité | Processus spécifique de traitement des vulnérabilités de sécurité. | Extension de la clause 9. |
| Maintenance de sécurité | Gestion des correctifs de sécurité, désactivation sécurisée et fin de vie. | Extension de la clause 6. |

### 7.7 Tableau récapitulatif des livrables de cybersécurité

| Livrable | Description | Référence(s) |
|----------|-------------|--------------|
| Threat model | Documentation des menaces identifiées, surfaces d'attaque, scénarios de compromission. | FDA Cybersecurity Guidance, IEC 81001-5-1 clause 5.3.2 |
| Évaluation des risques de cybersécurité | Analyse des risques de sécurité avec probabilité, impact et mesures d'atténuation. | FDA Cybersecurity Guidance, ISO 14971, IEC 81001-5-1 |
| SBOM | Inventaire complet des composants logiciels au format SPDX ou CycloneDX. | FDA (Section 524B FD&C Act), IEC 81001-5-1 |
| Plan de gestion de la cybersécurité | Procédures de réponse aux vulnérabilités, politique de mise à jour, communication. | FDA Cybersecurity Guidance |
| Rapports de tests de sécurité | Résultats des tests de pénétration, analyses de vulnérabilités, revue de code. | FDA Cybersecurity Guidance, IEC 81001-5-1 clause 5.7 |
| Politique de mise à jour et de fin de support | Durée de support prévue, stratégie de mise à jour, procédure de fin de vie. | FDA Cybersecurity Guidance |
| Documentation de l'architecture de sécurité | Description des contrôles de sécurité : chiffrement, authentification, contrôle d'accès, journalisation. | IEC 81001-5-1 clause 5.4, AAMI TIR57 |
| Plan de réponse aux incidents | Procédure de gestion des incidents de cybersécurité, incluant la notification des autorités. | FDA Postmarket Guidance, IEC 81001-5-1 |

---

## 8. Articulations entre les normes — tableau croisé

### 8.1 Vue d'ensemble des interactions

Les normes régissant les dispositifs médicaux ne sont pas isolées les unes
des autres. Elles forment un écosystème interconnecté où chaque norme
s'appuie sur les autres ou les complète. Le tableau croisé ci-dessous
montre les correspondances entre les principaux référentiels.

### 8.2 Tableau croisé — correspondances par domaine

| Norme / Règlement | QMS | Conception | Gestion des risques | Logiciel | Cybersécurité | Évaluation clinique | Surveillance post-marché |
|--------------------|-----|------------|---------------------|----------|---------------|---------------------|--------------------------|
| **FDA 21 CFR 820 (QMSR)** | Incorpore ISO 13485 (intégralité). Exigences FDA-spécifiques en complément. | 7.3 (via ISO 13485). Historiquement 820.30. | Référence ISO 14971 dans le QMSR. | Référence IEC 62304 dans les guidances. | FDA Cybersecurity Guidance (2023). Section 524B FD&C Act. | Preuves cliniques pour PMA. Substantial equivalence pour 510(k). | 21 CFR 803 (MDR reporting). 21 CFR 806 (corrections et retraits). |
| **ISO 13485:2016** | Clauses 4-8 (norme dédiée au QMS). | Clause 7.3 (conception et développement). | Clause 7.1 (planification avec gestion des risques). Référence ISO 14971 en note. | Non spécifique au logiciel (couvert par IEC 62304). | Non spécifique (couvert par IEC 81001-5-1). | Non spécifique (couvert par ISO 14155 et MDR). | Clause 8.2.1 (retour d'information), 8.2.2 (plaintes), 8.2.3 (signalement). |
| **EU MDR 2017/745** | Annexe IX chapitre I (QMS requis, ISO 13485 comme référentiel). | GSPR 5 (performances), annexe II (documentation technique), annexe IX chapitre II. | GSPR 1-3 (gestion des risques). ISO 14971 norme harmonisée. | GSPR 17 (logiciels et dispositifs programmables). Règle 11 (classification). IEC 62304 harmonisée. | GSPR 17.2 (cybersécurité). MDCG 2019-16. | Article 61 (évaluation clinique). Chapitre VI (investigations). Annexe XIV partie A (évaluation) et B (PMCF). | Chapitre VII (vigilance et PMS). Articles 83-92. PSUR (article 86). |
| **IEC 62304:2006+A1:2015** | S'intègre dans le QMS (ISO 13485 clause 7.3 pour la partie conception). | Clauses 5.1-5.8 (cycle de vie de développement logiciel). | Clause 7 (gestion des risques logiciels). Utilise ISO 14971 comme cadre. | Norme dédiée au cycle de vie logiciel. Classes A, B, C. | Clause 5.2 (exigences de sécurité). Complétée par IEC 81001-5-1. | Non applicable directement. | Clause 6 (maintenance). Clause 9 (résolution des problèmes). |
| **IEC 81001-5-1:2021** | S'intègre dans le QMS (processus de sécurité ajoutés aux processus qualité). | Clauses 5.3-5.4 (conception sécurisée). Complète IEC 62304. | Clauses 5.2-5.3 (gestion des risques de sécurité). Utilise ISO 14971 étendu à la sécurité. | Étend les processus IEC 62304 avec des exigences de cybersécurité. | Norme dédiée à la cybersécurité des logiciels de santé. | Non applicable directement. | Clause 5.9 (maintenance de sécurité). Gestion post-marché des vulnérabilités. |
| **ISO 14971:2019** | S'applique dans le cadre du QMS (ISO 13485 clause 7.1). | Alimente les design inputs (exigences de sécurité issues de l'analyse des risques). | Norme dédiée à la gestion des risques. Processus complet : analyse, évaluation, maîtrise, suivi. | Fournit le cadre de classification de sécurité pour IEC 62304. | Cadre étendu par AAMI TIR57 pour les risques de cybersécurité. | Alimente l'évaluation du rapport bénéfice-risque. | Suivi continu des risques résiduels en phase post-marché (clause 10). |

### 8.3 Flux d'information entre les normes

Le flux d'information typique entre les normes suit le schéma suivant :

1. **ISO 14971** fournit l'analyse des risques initiale, qui détermine :
   - Les exigences de conception liées à la sécurité (ISO 13485 clause 7.3.3).
   - La classification de sécurité logicielle (IEC 62304 clause 4.3).
   - Les exigences de cybersécurité (IEC 81001-5-1 clause 5.2).

2. **ISO 13485** fournit le cadre structurel du système qualité dans lequel
   tous les autres processus s'intègrent :
   - Le processus de conception et développement (clause 7.3) encapsule
     les processus IEC 62304 et IEC 81001-5-1.
   - Le processus CAPA (clause 8.5) traite les problèmes identifiés par
     IEC 62304 (clause 9) et IEC 81001-5-1 (clause 5.8).

3. **EU MDR** ou **FDA 21 CFR 820** fournissent le cadre réglementaire
   qui rend ces normes obligatoires ou recommandées.

4. **IEC 62304** et **IEC 81001-5-1** détaillent respectivement le cycle
   de vie logiciel et les aspects de cybersécurité, en s'appuyant sur
   les cadres fournis par ISO 14971 et ISO 13485.

### 8.4 Points d'attention lors de l'implémentation intégrée

| Point d'attention | Explication | Normes concernées |
|-------------------|-------------|-------------------|
| Dossier de gestion des risques unifié | Un seul dossier de gestion des risques couvrant les risques liés à la sécurité du patient, à la cybersécurité et à l'utilisabilité. | ISO 14971, IEC 81001-5-1, IEC 62366-1 |
| Traçabilité bout en bout | De l'exigence système à l'exigence logicielle, en passant par la conception, l'implémentation et les tests. | ISO 13485 (7.3), IEC 62304 (5.1-5.8), EU MDR (annexe II) |
| Processus CAPA/SOUP/vulnérabilités intégré | Un processus unique de résolution des problèmes couvrant les non-conformités qualité, les anomalies logicielles, les vulnérabilités SOUP et les vulnérabilités de cybersécurité. | ISO 13485 (8.5), IEC 62304 (clause 9), IEC 81001-5-1 (5.8) |
| Surveillance post-marché intégrée | Plan de PMS couvrant les plaintes cliniques, les anomalies logicielles et les vulnérabilités de cybersécurité. | EU MDR (articles 83-86), IEC 62304 (clause 6), FDA 21 CFR 803 |
| Validation conjointe | La validation du logiciel médical doit couvrir les aspects fonctionnels, de sécurité patient et de cybersécurité. | ISO 13485 (7.3.7), IEC 62304 (5.7), IEC 81001-5-1 (5.7) |

---

## 9. Documents indexés dans le RAG

### 9.1 Collection médicale

Les documents suivants sont indexés dans la collection médicale du RAG et
peuvent être interrogés directement via l'interface Streamlit.

| Fichier | Description | Origine |
|---------|-------------|---------|
| `EU_MDR_2017_745_EN.pdf` | Règlement (UE) 2017/745 relatif aux dispositifs médicaux — version anglaise. Texte complet du règlement incluant les annexes I à XVII. | Journal officiel de l'UE (accès libre). |
| `EU_MDR_2017_745_FR.pdf` | Règlement (UE) 2017/745 — version française. Identique au document EN mais dans la version officielle en langue française. | Journal officiel de l'UE (accès libre). |
| `Règlement Européen (MDR) 2017_745.pdf` | Version complémentaire du règlement MDR en français. Peut correspondre à une version annotée ou reformatée. | Source publique. |
| `EU_IVDR_2017_746_EN.pdf` | Règlement (UE) 2017/746 relatif aux dispositifs médicaux de diagnostic in vitro — version anglaise. | Journal officiel de l'UE (accès libre). |
| `EU_IVDR_2017_746_FR.pdf` | Règlement (UE) 2017/746 — version française. | Journal officiel de l'UE (accès libre). |
| `FDA_Cybersecurity_Medical_Devices.pdf` | FDA guidance : « Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions » (2023). | FDA (accès libre). |
| `FDA_Guide_Inspections_Quality_Systems.pdf` | FDA guide pour les inspections des systèmes qualité. Utilisé par les inspecteurs FDA lors des audits d'établissements fabricants de dispositifs médicaux. | FDA (accès libre). |
| `FDA_MDQS_Manual.pdf` | FDA Medical Device Quality Systems Manual. Documentation de référence sur les exigences QMS de la FDA. | FDA (accès libre). |
| `FDA_Quality_System_Regulation_Overview.pdf` | Vue d'ensemble de la réglementation FDA sur les systèmes qualité (21 CFR 820). Couvre les principes fondamentaux du QSR/QMSR. | FDA (accès libre). |
| `FDA_QMSR_Risk_Management.pdf` | Document FDA sur la gestion des risques dans le cadre du QMSR. Articulation entre le QMSR et ISO 14971. | FDA (accès libre). |
| `IMDRF_N47_Software_SaMD.pdf` | Document IMDRF N47 : « Software as a Medical Device (SaMD): Clinical Evaluation ». Cadre de référence international pour l'évaluation clinique des logiciels qualifiés de dispositifs médicaux. | IMDRF (accès libre). |
| `ISO_IEC_Guide_99_International_Vocabulary_Metrology.pdf` | Guide ISO/IEC 99 : Vocabulaire international de métrologie (VIM). Définitions fondamentales utilisées dans les normes de mesure et de qualification des dispositifs. | ISO/IEC (accès libre pour le vocabulaire). |
| `MDCG_2020-6_Sufficient_Clinical_Evidence.pdf` | MDCG 2020-6 : « Guidance on Sufficient Clinical Evidence for Legacy Devices ». Orientations du Medical Device Coordination Group sur le niveau de preuves cliniques suffisant pour les dispositifs existants dans le cadre de la transition vers le MDR. | Commission européenne (accès libre). |

### 9.2 Remarques sur la collection

- Tous les documents indexés sont des textes réglementaires, des guidances
  ou des normes dont la version publique est librement accessible.
- Les normes ISO et IEC complètes (par exemple ISO 13485:2016 ou
  IEC 62304:2006+A1:2015) sont protégées par le droit d'auteur et ne sont
  pas incluses dans la collection. Les références à ces normes dans ce
  document sont basées sur les informations publiquement disponibles.
- La collection peut être enrichie au fil du temps avec de nouveaux
  documents (par exemple, MDCG guidances complémentaires, guidances FDA
  mises à jour, normes ASTM applicables aux dispositifs médicaux).
- Pour interroger ces documents, utilisez l'interface RAG de l'application
  Streamlit en sélectionnant la collection « medical ».

### 9.3 Normes non indexées mais référencées dans ce document

Les normes suivantes sont fréquemment mentionnées dans ce document mais ne
sont pas indexées dans le RAG en raison de leur statut de publication
protégée :

| Norme | Titre | Raison de l'absence |
|-------|-------|---------------------|
| ISO 13485:2016 | Dispositifs médicaux — Systèmes de management de la qualité — Exigences à des fins réglementaires. | Norme payante (ISO). |
| ISO 14971:2019 | Dispositifs médicaux — Application de la gestion des risques aux dispositifs médicaux. | Norme payante (ISO). |
| IEC 62304:2006+A1:2015 | Logiciels de dispositifs médicaux — Processus du cycle de vie du logiciel. | Norme payante (IEC). |
| IEC 81001-5-1:2021 | Sécurité, efficacité et sûreté des logiciels de santé et des systèmes TI de santé — Partie 5-1 : sécurité — Activités dans le cycle de vie du produit. | Norme payante (IEC). |
| IEC 62366-1:2015+A1:2020 | Dispositifs médicaux — Partie 1 : application de l'ingénierie de l'aptitude à l'utilisation aux dispositifs médicaux. | Norme payante (IEC). |
| ISO 14155:2020 | Investigation clinique des dispositifs médicaux pour sujets humains — Bonnes pratiques cliniques. | Norme payante (ISO). |
| IEC 62443 (série) | Sécurité des systèmes d'automatisation industrielle et de commande. | Série de normes payantes (IEC). |

---

*Document généré pour le module RAG normes médicales. Les informations
présentées reflètent l'état des réglementations et normes en vigueur.
Pour toute application réglementaire, se référer aux textes officiels
dans leur version la plus récente.*
