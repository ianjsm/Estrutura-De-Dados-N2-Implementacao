class ArrayStack:
    """
    Exercício 1: Implementação de Pilha usando lista do Python (Array).
    LIFO: Last In, First Out (Último a entrar, primeiro a sair).
    """
    def __init__(self):
        # A lista interna que guarda os dados
        self._dados = []

    def __len__(self):
        # Retorna o tamanho da pilha
        return len(self._dados)

    def is_empty(self):
        # Retorna True se estiver vazia
        return len(self._dados) == 0

    def push(self, elemento):
        # Adiciona elemento no topo
        self._dados.append(elemento)

    def pop(self):
        # Remove e retorna o elemento do topo
        if self.is_empty():
            raise Exception("A pilha está vazia")
        return self._dados.pop()

    def top(self):
        # Apenas olha o elemento do topo sem remover
        if self.is_empty():
            raise Exception("A pilha está vazia")
        return self._dados[-1]


class ArrayQueue:
    """
    Exercício 1: Implementação de Fila usando lista do Python.
    FIFO: First In, First Out (Primeiro a entrar, primeiro a sair).
    Nota: Usar pop(0) em lista Python não é o mais performático (é O(n)), 
    mas é a implementação "mais simples possível" pedida.
    """
    def __init__(self):
        self._dados = []

    def __len__(self):
        return len(self._dados)

    def is_empty(self):
        return len(self._dados) == 0

    def enqueue(self, elemento):
        # Adiciona no final da fila
        self._dados.append(elemento)

    def dequeue(self):
        # Remove do início da fila
        if self.is_empty():
            raise Exception("A fila está vazia")
        return self._dados.pop(0) # Remove o índice 0 (primeiro da fila)

    def first(self):
        # Olha o primeiro da fila
        if self.is_empty():
            raise Exception("A fila está vazia")
        return self._dados[0]


class ArrayDeque:
    """
    Exercício 1: Implementação de Deque (Fila Dupla).
    Permite adicionar e remover de ambos os lados.
    """
    def __init__(self):
        self._dados = []

    def __len__(self):
        return len(self._dados)

    def is_empty(self):
        return len(self._dados) == 0

    def add_first(self, elemento):
        # Adiciona no início
        self._dados.insert(0, elemento)

    def add_last(self, elemento):
        # Adiciona no final
        self._dados.append(elemento)

    def delete_first(self):
        # Remove do início
        if self.is_empty():
            raise Exception("O deque está vazio")
        return self._dados.pop(0)

    def delete_last(self):
        # Remove do final
        if self.is_empty():
            raise Exception("O deque está vazio")
        return self._dados.pop()

    def first(self):
        if self.is_empty():
            raise Exception("O deque está vazio")
        return self._dados[0]

    def last(self):
        if self.is_empty():
            raise Exception("O deque está vazio")
        return self._dados[-1]