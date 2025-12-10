class ArrayStack:
    def __init__(self):
        self._dados = []

    def __len__(self):
        return len(self._dados)

    def is_empty(self):
        return len(self._dados) == 0

    def push(self, elemento):
        self._dados.append(elemento)

    def pop(self):
        if self.is_empty():
            print("pilha vazia")
        return self._dados.pop()

    def top(self):
        if self.is_empty():
            print("pilha vazia")
        return self._dados[-1]


class ArrayQueue:
    def __init__(self):
        self._dados = []

    def __len__(self):
        return len(self._dados)

    def is_empty(self):
        return len(self._dados) == 0

    def enqueue(self, elemento):
        self._dados.append(elemento)

    def dequeue(self):
        if self.is_empty():
            print("fila vazia")
        return self._dados.pop(0) 

    def first(self):
        if self.is_empty():
            print("fila vazia")
        return self._dados[0]


class ArrayDeque:
    def __init__(self):
        self._dados = []

    def __len__(self):
        return len(self._dados)

    def is_empty(self):
        return len(self._dados) == 0

    def add_first(self, elemento):
        self._dados.insert(0, elemento)

    def add_last(self, elemento):
        self._dados.append(elemento)

    def delete_first(self):
        if self.is_empty():
            print("deque vazio")
        return self._dados.pop(0)

    def delete_last(self):
        if self.is_empty():
            print("deque vazio")
        return self._dados.pop()

    def first(self):
        if self.is_empty():
            print("deque vazio")
        return self._dados[0]

    def last(self):
        if self.is_empty():
            print("deque vazio")
        return self._dados[-1]