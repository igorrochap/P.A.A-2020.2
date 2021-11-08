class Grafo():
    def __init__(self, vertices):
        self.grafo = [[0 for coluna in range(vertices)] for linha in range(vertices)]
        self.v = vertices

    def valido(self, v, posicao, caminho):
        if self.grafo[caminho[posicao - 1]][v] == 0:
            return False
        for vertice in caminho:
            if vertice == v:
                return False
        return True

    def _verificar_caminho(self, caminho, posicao):
        if posicao == self.v:
            if self.grafo[caminho[posicao - 1]][caminho[0]] == 1:
                return True
            else:
                return False

        for v in range(1, self.v):
            if self.valido(v, posicao, caminho):
                caminho[posicao] = v
                if self._verificar_caminho(caminho, posicao + 1):
                    return True
                caminho[posicao] = -1
        return False

    def caminho_hamiltoniano(self):
        caminho = self.v * [-1]
        caminho[0] = 0

        if not self._verificar_caminho(caminho, 1):
            print('A solução não existe')
            return False
        
        print('A solução existe e o Caminho Hamiltoniano é:')
        for vertice in caminho:
            print(vertice, end=' ')
        print(caminho[0])


grafo = Grafo(5)
grafo.grafo = [[0, 1, 0, 1, 0],
               [1, 1, 1, 0, 1],
               [1, 1, 0, 0, 1],
               [1, 1, 0, 0, 1],
               [0, 1, 1, 1, 1]]

grafo.caminho_hamiltoniano()