#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Autor: NKL
Descripción: Solo hay una función, vea su documentación.
"""

from os import system as ossystem
from sys import argv as sysargv
from subprocess import Popen, PIPE

def sncopy(ORIGEN, DESTINO):
    """Esta función copia y sobreescribe un archivo SOLO en caso de que sean distintos, esto se comprueba usando comparando sumas de comprobación md5."""

    if ossystem(f'file {ORIGEN} | grep "^.*: directory$\\|^.*: cannot open \\`.*\' (No such file or directory)" > /dev/null') == 0:
        print('El origen no existe o es un directorio.')
        return

    elif ossystem(f'file {DESTINO} | grep "^.*: directory$" > /dev/null') == 0:
        print('No se puede operar sobre directorios.')
        return

    # ORIGEN
    O0 = Popen(['cat', ORIGEN], stdout=PIPE)
    O1 = Popen(['md5sum'], stdin=O0.stdout, stdout=PIPE)
    O0.stdout.close()
    ORESULT = O1.communicate()[0].decode('utf-8')[0:32]

    # DESTINO
    D0 = Popen(['cat', DESTINO], stdout=PIPE)
    D1 = Popen(['md5sum'], stdin=D0.stdout, stdout=PIPE)
    D0.stdout.close()
    DRESULT = D1.communicate()[0].decode('utf-8')[0:32]

    # LOGICA
    if ORESULT != DRESULT or (ORESULT == "d41d8cd98f00b204e9800998ecf8427e" and DRESULT == "d41d8cd98f00b204e9800998ecf8427e"):
        print(f'Realizando la copia.')
        ossystem(f'cp {ORIGEN} {DESTINO}')

try:
    sncopy(sysargv[1], sysargv[2])
except IndexError:
    print('''# USO:
1. ORIGEN
2. DESTINO''')
