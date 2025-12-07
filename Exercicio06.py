from Exercicio01 import ArrayQueue

def testar_exercicio_06():
    """
    Executa a série de operações de fila pedida no Exercício 6.
    Operações: 
    enqueue(5), enqueue(3), dequeue(), enqueue(2), enqueue(8), dequeue(), dequeue(), 
    enqueue(9), enqueue(1), dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(), 
    enqueue(4), dequeue(), dequeue().
    """
    Q = ArrayQueue()
    print("--- [Exercício 06] Teste de Mesa (Fila) ---")

    # Lista de operações: (comando, valor ou None)
    operacoes = [
        ("enqueue", 5), ("enqueue", 3), ("dequeue", None),
        ("enqueue", 2), ("enqueue", 8), ("dequeue", None), ("dequeue", None),
        ("enqueue", 9), ("enqueue", 1), ("dequeue", None),
        ("enqueue", 7), ("enqueue", 6), ("dequeue", None), ("dequeue", None),
        ("enqueue", 4), ("dequeue", None), ("dequeue", None)
    ]

    for acao, valor in operacoes:
        if acao == "enqueue":
            Q.enqueue(valor)
            print(f"enqueue({valor}) -> Fila: {Q._dados}")
        elif acao == "dequeue":
            removido = Q.dequeue()
            print(f"dequeue()    -> Saiu: {removido} | Fila: {Q._dados}")

    print(f"\nEstado Final da Fila: {Q._dados}")
    print(f"Tamanho Final: {len(Q)}")

if __name__ == "__main__":
    testar_exercicio_06()