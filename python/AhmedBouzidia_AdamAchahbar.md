# Analyse de code Python 1

## Les problèmes

### Code commenté
Aucun commentaire dans tout le code.

### Frontière métier technique floue
Présence de constantes magiques (des chiffres).
#### Pourquoi c'est illisible ?
On ne connaît pas le sens de ces constantes. Par exemple, dans la ligne 28 de la fonction score : `self.p1points > 4`.

### Good methods
La fonction score :
#### Pourquoi c'est illisible ?
Un long bloc avec des if et else imbriqués. On peut créer une fonction pour le cas d'égalité, et une fonction en cas de non égalité. Il suffit donc d'appeler ces fonctions dans la fonction.

### Good methods
Trop de if else dans la méthode score.
#### Pourquoi c'est illisible ?
On ne comprend pas trop la logique et c'est trop long.

### Pas de convention de style
Manque de consistance dans le nommage des variables.
#### Pourquoi c'est illisible ?
La convention de nommage n'est pas respectée. Ici, on utilise un nommage camelCase : `if playerName == "player1"`, et ici, on a un nommage différent : `self.p1points += 1`.
Utiliser les verbes pour les nom de fonctions comme Socore ,on peut nomer par getScore ou calculate Score.

### Exceptions mutables
Dans tout le code, pas de gestion d'exceptions.

 


[Un lien vers le code Python 1](https://github.com/Ahmed-Bouzidia/Tennis-Refactoring-Kata/blob/main/python/tennis1.py)
