import networkx as nx
from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.idMap = {}

    def buildGraph(self):
        nodi = DAO.getAllNodes()
        self.grafo.add_nodes_from(nodi)
        for n in nodi:
            self.idMap[n.GeneID] = n
        connessioni = DAO.getAllConnessioni(self.idMap)
        for c in connessioni:
            if self.idMap[c.gene1.GeneID].Chromosome == self.idMap[c.gene2.GeneID].Chromosome:
                self.grafo.add_edge(c.gene1, c.gene2, weight=2*abs(c.espressione))
            else:
                self.grafo.add_edge(c.gene1, c.gene2, weight=abs(c.espressione))

    def getPesiVicini(self, nodo):
        vicini = self.grafo.neighbors(nodo)
        mappa = {}
        for v in vicini:
            mappa[v.GeneID] = self.grafo[nodo][v]["weight"]
        # ordina un dizionario per valore decrescente
        vicini_ordinati = dict(sorted(mappa.items(), key=lambda x: x[1], reverse=True))
        return vicini_ordinati