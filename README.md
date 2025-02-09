
# Description

Ce projet de cours a pour objectif de comprendre les bases de la cryptographie en développant, depuis une page blanche, une application en ligne de commande permettant de communiquer en utilisant l'algorithme RSA.


## Tuto

Commandes disponibles :

Générer une paire de clé RSA : 
    generate_keys 

Chiffre un message (utilise la clé publique enregistrée) :
    encrypt "<message>"

Déchiffre un message (utilise la clé privée enregistrée) :
    decrypt "<message_chiffré>"

  - Exemples :
  
    python rsa.py generate_keys

    python rsa.py encrypt "Kebab succulent"

    python rsa.py decrypt "2701 3225 1101 452 1101 1239 1668 1628 1268 1268 1628 463 3225 3376 471"

## Requirements

- [sys](https://docs.python.org/fr/3/library/sys.html)
- [math](https://docs.python.org/3/library/math.html)
- [random](https://docs.python.org/3/library/random.html)
- [json](https://docs.python.org/3/library/json.html)
- [Time](https://docs.python.org/3/library/time.html)

## Authors

- [@TsarRevan](https://github.com/TsarRevan)
- [@K4NT1](https://github.com/K4NT1)
