# Fiche Recap SQL

Forme générale d'une requête SQL:
``` 
SELECT
	... projection(s) ...
FROM
	... table(s), vue(s), sous-requête(s) ...
WHERE
	... filtre(s)
ORDER BY
	... critère(s) de tris ...
```

NB: à suivre les clauses GROUP BY et HAVING	


## Prédicats
```
code_metier = 'ASSO'
code_metier <> 'ASSO'
code_metier != 'ASSO'
code_metier IN ('ASSO', 'HAB')
code_metier NOT IN ('ASSO', 'HAB')
lib_ville LIKE '%TOULOUSE%'
lib_ville NOT LIKE '%TOULOUSE%'
mt_cial < 1000
mt_cial <= 1000
mt_cial > 1000
mt_cial >= 1000
mt_cial BETWEEN 1000 AND 2000
lib_ville IS NULL
lib_ville IS NOT NULL
```

Opérateurs de logique: AND, OR, NOT

## Fonctions et opérateurs en ligne
https://documentation.sas.com/doc/en/pgmsascdc/v_068/lefunctionsref/p1q8bq2v0o11n6n1gpij335fqpph.htm
https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/sqlproc/n1cq72kb6ab41in1pzngij4dhek1.htm

### texte
```
UPPER, UPCASE : minuscule
LOWER, LOWCASE : majuscule
SUBSTR : sous-chaîne
LENGTH : longueur chaîne
CATS, CATX, operateur || : concaténation
TRIM, STRIP, COMPRESS : suppression des blancs
REPLACE, PRXCHANGE : remplacement
INDEX : recherche
```

### numérique
```
+ - * / **
ROUND, FLOOR, CEIL
ABS
```
- fonctions aléatoires: `RAND, NORMAL, POISSON`, ...
- fonctions de trigo: `COS, SIN`, ...
- fonctions puissance, logarithme: `LOG, SQRT`, ...


### valeurs nulles
`COALESCE` : valeur de substitution de NULL ou 1ere valeur non nulle

NB: utiliser CASE

### temporel
3 types : number avec format dédié
- date : précision 1 jour
- datetime : précision 1 s
- time : précision 1 s

#### fonctions date-heure systeme:
```
DATE
DATETIME
TIME

fonctions d'extraction
DATEPART: datetime -> date
TIMEPART: datetime -> time
YEAR, MONTH, DAY, MINUTE, HOUR, MINUTE, SECOND : 1 composante
```

#### Formats de date
| Format        | Exemple    | Description                             |
| ------------- | ---------- | --------------------------------------- |
| **DATE.**     | 02JAN25    | Date abrégée                            |
| **DATE9.**    | 02JAN2025  | Format SAS le plus classique            |
| **DDMMYY8.**  | 02/01/25   | dd/mm/yy                                |
| **DDMMYY10.** | 02/01/2025 | dd/mm/yyyy                              |
| **MMDDYY8.**  | 01/02/25   | mm/dd/yy                                |
| **MMDDYY10.** | 01/02/2025 | mm/dd/yyyy                              |
| **YYMMDD6.**  | 250102     | yymmdd                                  |
| **YYMMDD8.**  | 20250102   | yyyymmdd                                |
| **YYMMDD10.** | 2025-01-02 | yyyy-mm-dd (ISO)                        |

#### Formats d'heure
| Format      | Exemple     | Description          |
| ----------- | ----------- | -------------------- |
| **TIME5.**  | 12:34       | hh:mm                |
| **TIME8.**  | 12:34:56    | hh:mm:ss             |
| **TIME11.** | 12:34:56.12 | secondes + décimales |
| **HHMM.**   | 1234        | hhmm                 |
| **HOUR.**   | 12          | Heure seule          |
| **MINUTE.** | 34          | Minute seule         |
| **SECOND.** | 56          | Seconde seule        |
| **TOD.**    | 12:34:56    | Alias de TIME8.      |

#### Formats de date-heure
| Format          | Exemple                    | Description     |
| --------------- | -------------------------- | --------------- |
| **DATETIME.**   | 02JAN25:12:34:56           |                 |
| **DATETIME15.** | 02JAN25:12:34              | Affichage court |
| **DATETIME18.** | 02JAN25:12:34:56           |                 |
| **DATETIME20.** | 02JAN2025:12:34:56         | Le plus utilisé |
| **E8601DT.**    | 2025-01-02T12:34:56        | Format ISO 8601 |
| **E8601DT26.**  | 2025-01-02T12:34:56.123456 |                 |
| **MDYAMPM.**    | 01/02/2025 12:34 PM        | AM/PM           |


## Fonctions d'agrégations (statistiques) : vertical
```
COUNT
```

à suivre, épisode 3 SQL




















