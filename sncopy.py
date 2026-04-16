#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Autor: NKL
Descripción: Solo hay una función, vea su documentación.
"""

from os import system as ossystem
from sys import argv as sysargv
from subprocess import Popen, PIPE

# VARs
DA = dict(md5sum="d41d8cd98f00b204e9800998ecf8427e", sha256sum="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", sha512sum="cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e")

def sncopy(ORIGEN, DESTINO, ALGO="md5sum", /):
    """Esta función copia y sobreescribe un archivo SOLO en caso de que sean distintos, esto se comprueba usando comparando sumas de comprobación md5."""

    if ossystem(f'file {ORIGEN} | grep "^.*: directory$\\|^.*: cannot open \\`.*\' (No such file or directory)" > /dev/null') == 0:
        print('El origen no existe o es un directorio')
        return

    elif ossystem(f'file {DESTINO} | grep "^.*: directory$" > /dev/null') == 0:
        print('No se puede operar sobre directorios')
        return

    # ORIGEN
    O0 = Popen(['cat', ORIGEN], stdout=PIPE)
    O1 = Popen([ALGO], stdin=O0.stdout, stdout=PIPE)
    O0.stdout.close()
    ORESULT = O1.communicate()[0].decode('utf-8')[:-4]

    # DESTINO
    D0 = Popen(['cat', DESTINO], stdout=PIPE)
    D1 = Popen([ALGO], stdin=D0.stdout, stdout=PIPE)
    D0.stdout.close()
    DRESULT = D1.communicate()[0].decode('utf-8')[:-4]

    # LOGICA
    if ORESULT != DRESULT or (ORESULT == DA[ALGO] and DRESULT == DA[ALGO]):
        print(f'Realizando la copia')
        ossystem(f'cp {ORIGEN} {DESTINO}')

if __name__ == "__main__":
    try:
        sncopy(sysargv[1], sysargv[2], sysargv[3] if "sha256sum" in sysargv or "sha512sum" in sysargv else "md5sum")
    except IndexError:
        print('''# USO:
1. ORIGEN
2. DESTINO''')
