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

# EXPLICACIÓN DE LO QUE HACE ESTE PROGRAMA PARA UN NIÑO DE 5 AÑOS
# sncopy

## SUMA DE COMPROBACIÓN
Digamos que un archivo es una persona, al igual que las personas tiene una identificación, se podria decir que sus caracteristicas son su identificación inequivoca, sin importar donde se encuentre o cuantas copias de si misma haya, pero pasa que esa identificacion puede ser muy compleja de leer por lo que necesitamos un resumen, ahi entra la "suma de comprobación", lo que seria como hacer un resumen de un gran libro, cuento o algo similar, hay varias maneras de hacer estos resumenes, a estas maneras de resumir las llamamos "algoritmos de suma de comprobación", uno de ellos es md5. md5 devuelve una identificación de 32 caracteres siempre.

## COMPARACIÓN
Entonces comparando la suma de comprobación (identificación) de dos archivos podemos saber si se trata o no de el mismo archivo.

## LÓGICA COMPLETA
Entonces el programa obtuvo la identificación de dos archivos, se da cuenta que son distintos y decide realizar la copia en la ubicación de destino, en la cual se encontraba uno de los archivos comparados. Si bien un archivo puede tener varias copias (como clones) en distintos lugares no puede haber varios archivos en un lugar muy especifico, digamos que cada archivo vive en una hábitación y no se permite que haya más de un archivo en cada hábitación, entonces al realizar una copia de un archivo sobre la ubicación donde estaba otro, el que antes ocupaba esa ubicación (hábitación) desaparece en el acto.
