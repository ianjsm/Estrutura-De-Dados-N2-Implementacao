class Empty(Exception):
    """Erro ao tentar acessar elemento de container vazio."""
    pass

# ==========================================
# 1. LinkedStack (Pilha Encadeada)
# ==========================================
class LinkedStack:
    """
    Pilha LIFO usando lista simplesmente encadeada.
    Topo da pilha = Cabeça (Head) da lista.
    """

    # Classe aninhada _Node (Nó)
    class _Node:
        __slots__ = '_element', '_next' # Otimiza memória

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None # Topo da pilha
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        # Cria novo nó apontando para o antigo topo (head)
        # E atualiza o head para ser esse novo nó
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty("A pilha está vazia")
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty("A pilha está vazia")
        
        resposta = self._head._element
        self._head = self._head._next # O topo agora é o próximo da lista
        self._size -= 1
        return resposta


# ==========================================
# 2. LinkedQueue (Fila Encadeada)
# ==========================================
class LinkedQueue:
    """
    Fila FIFO usando lista simplesmente encadeada.
    Mantém ponteiro para Head (início) e Tail (fim).
    """
    
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("A fila está vazia")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("A fila está vazia")
        
        resposta = self._head._element
        self._head = self._head._next
        self._size -= 1
        
        if self.is_empty(): # Se esvaziou, tail também vira None
            self._tail = None
            
        return resposta

    def enqueue(self, e):
        novo_no = self._Node(e, None)
        
        if self.is_empty():
            self._head = novo_no # Se vazia, novo é head e tail
        else:
            self._tail._next = novo_no # O antigo último aponta para o novo
            
        self._tail = novo_no # O novo vira o tail oficial
        self._size += 1


# ==========================================
# 3. CircularQueue (Fila Circular)
# ==========================================
class CircularQueue:
    """
    Fila usando lista circularmente encadeada.
    Não precisamos de 'head', apenas 'tail'.
    O 'tail.next' é o head.
    """
    
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("A fila está vazia")
        # O "primeiro" é o vizinho do "último"
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("A fila está vazia")
        
        old_head = self._tail._next
        
        if self._size == 1:
            # Se só tinha 1, removendo ele a fila fica vazia
            self._tail = None
        else:
            # O tail "pula" a cabeça velha e aponta para a nova
            self._tail._next = old_head._next
            
        self._size -= 1
        return old_head._element

    def enqueue(self, e):
        novo_no = self._Node(e, None)
        
        if self.is_empty():
            novo_no._next = novo_no # Aponta para si mesmo (ciclo)
            self._tail = novo_no
        else:
            novo_no._next = self._tail._next # Novo aponta para head
            self._tail._next = novo_no       # Tail antigo aponta para novo
            self._tail = novo_no             # Novo vira tail
            
        self._size += 1

    def rotate(self):
        """Move o elemento da frente para o fim da fila."""
        if self._size > 0:
            # Basta avançar o ponteiro tail. O antigo head vira tail.
            self._tail = self._tail._next


# ==========================================
# 4. LinkedDeque (Deque Duplamente Encadeado)
# ==========================================
class LinkedDeque:
    """
    Deque usando lista duplamente encadeada com Sentinelas.
    Sentinelas (header/trailer) são nós vazios que facilitam a lógica
    para não precisarmos checar tantos 'if is_empty'.
    """

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        # Cria sentinelas
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        
        # Conecta sentinelas: header <-> trailer
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # --- Métodos Auxiliares Privados ---
    def _insert_between(self, e, predecessor, successor):
        """Insere elemento 'e' entre dois nós existentes."""
        novo = self._Node(e, predecessor, successor)
        predecessor._next = novo
        successor._prev = novo
        self._size += 1
        return novo

    def _delete_node(self, node):
        """Remove um nó e conecta seus vizinhos."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        
        elemento = node._element
        # Ajuda garbage collector limpando referências
        node._prev = node._next = node._element = None
        return elemento

    # --- Métodos Públicos ---
    def first(self):
        if self.is_empty():
            raise Empty("Deque vazio")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty("Deque vazio")
        return self._trailer._prev._element

    def insert_first(self, e):
        # Insere entre header e o vizinho do header
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        # Insere entre o vizinho do trailer e o trailer
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque vazio")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque vazio")
        return self._delete_node(self._trailer._prev)


# ==========================================
# Função de Teste
# ==========================================
def testar_exercicio_12():
    print("--- [Exercício 12] Estruturas Encadeadas ---")
    
    print("\n1. Testando LinkedStack (Pilha Encadeada)")
    S = LinkedStack()
    S.push(10)
    S.push(20)
    print(f"Topo: {S.top()} (Esperado: 20)")
    print(f"Pop: {S.pop()} (Esperado: 20)")
    
    print("\n2. Testando LinkedQueue (Fila Encadeada)")
    Q = LinkedQueue()
    Q.enqueue("A")
    Q.enqueue("B")
    print(f"Primeiro: {Q.first()} (Esperado: A)")
    print(f"Dequeue: {Q.dequeue()} (Esperado: A)")

    print("\n3. Testando CircularQueue")
    C = CircularQueue()
    C.enqueue(1)
    C.enqueue(2)
    C.enqueue(3)
    # Fila: [1, 2, 3] -> Rotate -> [2, 3, 1]
    print(f"Antes do rotate, primeiro: {C.first()} (Esperado: 1)")
    C.rotate()
    print(f"Após rotate, primeiro: {C.first()} (Esperado: 2)")

    print("\n4. Testando LinkedDeque (Duplamente Encadeado)")
    D = LinkedDeque()
    D.insert_first(5) # [5]
    D.insert_last(10) # [5, 10]
    D.insert_first(1) # [1, 5, 10]
    print(f"Primeiro: {D.first()} (Esperado: 1)")
    print(f"Último: {D.last()} (Esperado: 10)")
    print(f"Delete Last: {D.delete_last()} (Esperado: 10)")

if __name__ == "__main__":
    testar_exercicio_12()