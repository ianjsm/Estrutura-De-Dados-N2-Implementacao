from Exercicio12 import LinkedDeque

def remover_duplicatas(lista):
    """
    Exercício 19: Remove elementos duplicados de uma lista duplamente encadeada.
    Complexidade: O(n) usando uma tabela hash (set) auxiliar.
    """
    vistos = set()
    
    # Começamos logo após o header (primeiro nó real)
    atual = lista._header._next
    
    # Enquanto não chegarmos no trailer (sentinela final)
    while atual is not lista._trailer:
        elemento = atual._element
        proximo_no = atual._next # Salva o próximo antes de talvez deletar o atual
        
        if elemento in vistos:
            # Já vimos esse valor antes! Removemos o nó atual.
            # Usamos o método protegido _delete_node da classe LinkedDeque
            lista._delete_node(atual)
        else:
            # Novo valor, adiciona ao conjunto de vistos
            vistos.add(elemento)
            
        atual = proximo_no

def imprimir_deque(deque):
    # Função auxiliar para visualizar a lista
    elementos = []
    atual = deque._header._next
    while atual is not deque._trailer:
        elementos.append(str(atual._element))
        atual = atual._next
    return " <-> ".join(elementos)

def testar_exercicio_19():
    print("--- [Exercício 19] Remover Duplicatas (Doubly Linked) ---")
    lista = LinkedDeque()
    
    # Inserindo dados com repetição: [A, B, A, C, B, D]
    lista.insert_last("A")
    lista.insert_last("B")
    lista.insert_last("A") # Duplicado
    lista.insert_last("C")
    lista.insert_last("B") # Duplicado
    lista.insert_last("D")
    
    print(f"Original:  {imprimir_deque(lista)}")
    
    remover_duplicatas(lista)
    
    print(f"Sem Dups:  {imprimir_deque(lista)}") # Esperado: A <-> B <-> C <-> D

if __name__ == "__main__":
    testar_exercicio_19()