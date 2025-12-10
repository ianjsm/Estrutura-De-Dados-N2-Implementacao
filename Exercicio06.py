from Exercicio01 import ArrayQueue

def testar_exercicio_06():
    Q = ArrayQueue()

    Q.enqueue(5)
    print("enqueue(5)")
    print(f"Fila: {Q._dados}")

    Q.enqueue(3)
    print("enqueue(3)")
    print(f"Fila: {Q._dados}")

    print("dequeue()")
    print(f"Saiu: {Q.dequeue()}")
    print(f"Fila: {Q._dados}")

    Q.enqueue(2)
    print("enqueue(2)")
    print(f"Fila: {Q._dados}")

    Q.enqueue(8)
    print("enqueue(8)")
    print(f"Fila: {Q._dados}")

    print("dequeue()")
    print(f"Saiu: {Q.dequeue()}")
    print(f"Fila: {Q._dados}")

    print("dequeue()")
    print(f"Saiu: {Q.dequeue()}")
    print(f"Fila: {Q._dados}")

    Q.enqueue(9)
    print("enqueue(9)")
    print(f"Fila: {Q._dados}")

    Q.enqueue(1)
    print("enqueue(1)")
    print(f"Fila: {Q._dados}")

    print("dequeue()")
    print(f"Saiu: {Q.dequeue()}")
    print(f"Fila: {Q._dados}")

    Q.enqueue(7)
    print("enqueue(7)")
    print(f"Fila: {Q._dados}")

    Q.enqueue(6)
    print("enqueue(6)")
    print(f"Fila: {Q._dados}")

    print("dequeue()")
    print(f"Saiu: {Q.dequeue()}")
    print(f"Fila: {Q._dados}")

    print("dequeue()")
    print(f"Saiu: {Q.dequeue()}")
    print(f"Fila: {Q._dados}")

    Q.enqueue(4)
    print("enqueue(4)")
    print(f"Fila: {Q._dados}")

    print("dequeue()")
    print(f"Saiu: {Q.dequeue()}")
    print(f"Fila: {Q._dados}")

    print("dequeue()")
    print(f"Saiu: {Q.dequeue()}")
    print(f"Fila: {Q._dados}")

    print("\nEstado Final da Fila:")
    print(Q._dados)
    print(f"Tamanho Final: {len(Q)}")

if __name__ == "__main__":
    testar_exercicio_06()
