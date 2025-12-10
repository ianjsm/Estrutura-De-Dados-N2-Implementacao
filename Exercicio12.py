class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            print("pilha vazia")
        return self._head._element

    def pop(self):
        if self.is_empty():
            print("pilha vazia")
        
        resposta = self._head._element
        self._head = self._head._next
        self._size -= 1
        return resposta

class LinkedQueue:
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
            print("fila vazia")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            print("fila vazia")
        
        resposta = self._head._element
        self._head = self._head._next
        self._size -= 1
        
        if self.is_empty():
            self._tail = None
            
        return resposta

    def enqueue(self, e):
        novo_no = self._Node(e, None)
        
        if self.is_empty():
            self._head = novo_no 
        else:
            self._tail._next = novo_no 
            
        self._tail = novo_no 
        self._size += 1

class CircularQueue:
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
            print("fila vazia")
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            print("fila vazia")
        
        old_head = self._tail._next
        
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next
            
        self._size -= 1
        return old_head._element

    def enqueue(self, e):
        novo_no = self._Node(e, None)
        
        if self.is_empty():
            novo_no._next = novo_no 
            self._tail = novo_no
        else:
            novo_no._next = self._tail._next 
            self._tail._next = novo_no      
            self._tail = novo_no             
            
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next

class LinkedDeque:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        novo = self._Node(e, predecessor, successor)
        predecessor._next = novo
        successor._prev = novo
        self._size += 1
        return novo

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        
        elemento = node._element
        node._prev = node._next = node._element = None
        return elemento

    def first(self):
        if self.is_empty():
            print("deque vazio")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            print("deque vazio")
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            print("deque vazio")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            print("deque vazio")
        return self._delete_node(self._trailer._prev)