from Exercicio01 import ArrayDeque

def testar_exercicio_07():
    D = ArrayDeque()

    D.add_first(4)
    print("add_first(4)")
    print(f"Deque: {D._dados}")

    D.add_last(8)
    print("add_last(8)")
    print(f"Deque: {D._dados}")

    D.add_last(9)
    print("add_last(9)")
    print(f"Deque: {D._dados}")

    D.add_first(5)
    print("add_first(5)")
    print(f"Deque: {D._dados}")

    print("back()")
    print(f"Último: {D.last()}")
    print(f"Deque: {D._dados}")

    print("delete_first()")
    print(f"Saiu: {D.delete_first()}")
    print(f"Deque: {D._dados}")

    print("delete_last()")
    print(f"Saiu: {D.delete_last()}")
    print(f"Deque: {D._dados}")

    D.add_last(7)
    print("add_last(7)")
    print(f"Deque: {D._dados}")

    print("first()")
    print(f"Primeiro: {D.first()}")
    print(f"Deque: {D._dados}")

    print("last()")
    print(f"Último: {D.last()}")
    print(f"Deque: {D._dados}")

    D.add_last(6)
    print("add_last(6)")
    print(f"Deque: {D._dados}")

    print("delete_first()")
    print(f"Saiu: {D.delete_first()}")
    print(f"Deque: {D._dados}")

    print("delete_first()")
    print(f"Saiu: {D.delete_first()}")
    print(f"Deque: {D._dados}")

    print("\nEstado Final do Deque:")
    print(D._dados)

if __name__ == "__main__":
    testar_exercicio_07()
