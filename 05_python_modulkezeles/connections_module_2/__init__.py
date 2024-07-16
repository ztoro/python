# Ez a file általában üres, ennek a file-nak a jelenléte jelzi a pythonnak hogy ez a mappa egy modul!
# Viszont itt tehetünk még pár dolgot, mondjuk definiáljunk egy változót:
PACKAGE_VERSION = "1.0.0"
# És definiáljuk, hogy milyen függvényeket szeretnénk kívülről meghívhatóvá tenni

from .connections import get_data, write_hello_world
from .errors import MyOwnError
