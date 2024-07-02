from dataclasses import dataclass

from model.gene import Gene


@dataclass
class Connessione:
    gene1: Gene
    gene2: Gene
    espressione: float