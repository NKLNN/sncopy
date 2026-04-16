# sncopy
Script para comparar dos archivos y realizar una copia en el destino en caso de que sean distintos. Básicamente compara sumas de comprobación "md5" (predeterminado), tambien se admite opcionalmente los algoritmos "sha256" y "sha512".

Esto lo he probado en Debian 13 pero deberia funcionar en cualquier distribución de Linux, incluso deberia funcionar en Termux y Windows si instala las dependencias necesarias.

# MODO DE USO
sncopy ORIGEN DESTINO [ALGO=md5sum]

Las copias de un archivo vacio a un archivo vacio o de un archivo vacio a una ubicación donde no hay nada siempre se realizaran, las copias entre carpetas no funcionaran.

# LAS DEPENDENCIAS USADAS SON:
* ``python3``
* ``file``
* ``grep``
* ``cat``
* ``md5sum``
* ``sha256sum``
* ``sha512sum``
* ``cp``

Si por alguna razon algunas dependencias no estuvieran ya instaladas en Debian ejecute ``sudo apt update && sudo apt install -y python3 grep file``.

# NOTA:
Si te gusta No me molesta recivir una estrella.
