import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._selected_gene = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.buildGraph()
        if self._model.grafo:
            self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente"))
            self._view.txt_result.controls.append(
                ft.Text(f"Grafo con {len(self._model.grafo.nodes)} nodi e {len(self._model.grafo.edges)} archi"))
            self.fillDDGenes()
            self._view.update_page()



    def handle_geni_adiacenti(self, e):
        nodo = self._selected_gene
        if nodo is None:
            self._view.txt_result.controls.append(
                ft.Text("Seleziona un gene!", color = "red"))
            self._view.update_page()
        else:
            vicini= self._model.getPesiVicini(nodo)
            self._view.txt_result.controls.append(
                ft.Text(f"Geni adiacenti a {nodo.GeneID}"))
            self._view.update_page()
            for k,v in vicini.items():
                self._view.txt_result.controls.append(
                    ft.Text(f"{k}: {v}"))
            self._view.update_page()


    def handle_simulazione(self, e):
        pass

    def fillDDGenes(self):
        allNodes = self._model.grafo.nodes
        for n in allNodes:
            self._view.ddGenes.options.append(ft.dropdown.Option(text=n.GeneID, data=n, on_click=self.readDDGenes))
        self._view.update_page()

    def readDDGenes(self, e):
        if e.control.data is None:
            self._selected_gene = None
        else:
            self._selected_gene = e.control.data