class Pilha:
    def __init__(self):
        self._dados = []

    def __len__(self):
        return len(self._dados)

    def vazia(self):
        return not self._dados

    def empilhar(self, item):
        self._dados.append(item)

    def desempilhar(self):
        if self.vazia():
            print("pilha vazia")
        return self._dados.pop()

    def topo(self):
        if self.vazia():
            print("pilha vazia")
        return self._dados[-1]


class Fila:
    def __init__(self):
        self._dados = []

    def __len__(self):
        return len(self._dados)

    def vazia(self):
        return not self._dados

    def inserir(self, item):
        self._dados.append(item)

    def remover(self):
        if self.vazia():
            print("fila vazia")
        return self._dados.pop(0)

    def primeiro(self):
        if self.vazia():
            print("fila vazia")
        return self._dados[0]


class Deque:
    def __init__(self):
        self._dados = []

    def __len__(self):
        return len(self._dados)

    def vazia(self):
        return not self._dados

    def inserir_inicio(self, item):
        self._dados.insert(0, item)

    def inserir_final(self, item):
        self._dados.append(item)

    def remover_inicio(self):
        if self.vazia():
            print("deque vazio")
        return self._dados.pop(0)

    def remover_final(self):
        if self.vazia():
            print("deque vazio")
        return self._dados.pop()

    def primeiro(self):
        if self.vazia():
            print("deque vazio")
        return self._dados[0]

    def ultimo(self):
        if self.vazia():
            print("deque vazio")
        return self._dados[-1]