# ComplexityPython
Performance des langages

Nous allons effectuer des recherches en groupe pour définir quel langage est le plus performant et
surtout comparé les langages compilés au langages interprétés et ceux qui sont "portables" utilisant
du bytecode.

Chaque team de candidats doit choisir un langage parmi l'un de ceux-ci :
- C#
- Javascript
- Java
- Python
- PHP
- C++
- C
- Delphi
- Ruby

Il faudra ensuite faire les opérations suivantes pour calculer la performance de celui-ci :
1. Performance de calcul
On effectue le calcul de la série harmonique jusqu'à 2'000'000'000 d'opérations (2 milliards).
Cette série est en fait l'addition des fractions de 1/n.
Exemple avec n=5 : 1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.2833333
Le résultat final doit être affiché, le temps d'exécution doit être comptabilisé avec des
timestamp pour plus de précision.
2. Performance mémoire
On créer un tableau (ou autre structure de données existante dans le langage) de 1'000'000
de cases (1 million) et on assigne les nombres 1 à n (n étant la longueur) à l'intérieur, on
inverse ensuite toutes les valeurs en parcourant la moitié du tableau et en échangeant les
valeurs des cases n et length(tab)-n.
Exemple avec un tableau de 4 cases :

Création du tableau
1 2 3 4 Echange
=>
4 3 2 1

Pour garantir le bon fonctionnement on peut afficher le premier élément du tableau ainsi
que le dernier. Attention ce programme ne fonctionne qu'avec une longueur de tableau
paire.
3. Performance d'accès disque
On fait une boucle qui ouvre un fichier dans lequel on écrit la valeur n, puis qui ferme le
fichier. La boucle doit faire au moins 1'000'000 de tours (1 millions) et donc d'accès disque.
En Javascript on peut utiliser le localStorage car certains langages ne permettent pas d'accès
direct aux fichiers.