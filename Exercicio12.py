class No:
    def __init__(self, dado, proximo=None, anterior=None):
        self.dado = dado
        self.proximo = proximo
        self.anterior = anterior

class PilhaEncadeada:
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    def vazia(self):
        return self._tamanho == 0

    def empilhar(self, item):
        self.cabeca = No(item, self.cabeca)
        self._tamanho += 1

    def desempilhar(self):
        if self.vazia(): return None
        dado = self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        self._tamanho -= 1
        return dado

class FilaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self._tamanho = 0

    def vazia(self):
        return self._tamanho == 0

    def inserir(self, item):
        novo = No(item)
        if self.vazia():
            self.cabeca = novo
        else:
            self.cauda.proximo = novo
        self.cauda = novo
        self._tamanho += 1
    
    def remover(self):
        if self.vazia(): return None
        dado = self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        self._tamanho -= 1
        if self.vazia(): self.cauda = None
        return dado

class FilaCircular:
    def __init__(self):
        self.cauda = None
        self._tamanho = 0

    def vazia(self):
        return self._tamanho == 0

    def inserir(self, item):
        novo = No(item)
        if self.vazia():
            novo.proximo = novo
            self.cauda = novo
        else:
            novo.proximo = self.cauda.proximo
            self.cauda.proximo = novo
            self.cauda = novo
        self._tamanho += 1

    def rotacionar(self):
        if self._tamanho > 0:
            self.cauda = self.cauda.proximo

class DequeEncadeado:
    def __init__(self):
        self.cabeca = No(None)
        self.cauda = No(None)  
        self.cabeca.proximo = self.cauda
        self.cauda.anterior = self.cabeca
        self._tamanho = 0

    def vazia(self):
        return self._tamanho == 0

    def _inserir_entre(self, item, ant, prox):
        novo = No(item, prox, ant)
        ant.proximo = novo
        prox.anterior = novo
        self._tamanho += 1

    def _remover_no(self, no):
        ant = no.anterior
        prox = no.proximo
        ant.proximo = prox
        prox.anterior = ant
        self._tamanho -= 1
        return no.dado

    def inserir_final(self, item):
        self._inserir_entre(item, self.cauda.anterior, self.cauda)

def executar():
    print("Exercício 12")