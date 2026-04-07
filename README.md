# sncopy
Script para comparar dos archivos y realizar una copia en el destino en caso de que sean distintos. Básicamente compara sumas de comprobación md5sum.

Esto lo he probado en Debian 13 pero deberia funcionar en cualquier Linux, incluso deberia funcionar en Termux y Windows si instala las dependencias necesarias.

# Dependencias usadas son:
* ``python3``
* ``file``
* ``grep``
* ``cat``
* ``md5sum``
* ``cp``

Si por alguna razon algunas no estuvieran ya instaladas en Debian ejecute ``sudo apt update && sudo apt install -y python3 grep file``.

# NOTA:
Ni idea si algo similar ya existe.
