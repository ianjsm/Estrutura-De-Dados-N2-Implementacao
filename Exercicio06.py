from Exercicio01 import Fila

def executar():
    print("Exercício 6")
    f = Fila()
    while True:
        print(f"\nFila: {f._dados}")
        op = input("1.Inserir 2.Remover 3.Primeiro 0.Voltar: ")
        if op == '1':
            v = input("Valor: ")
            f.inserir(v)
        elif op == '2':
            print(f"Removido: {f.remover()}")
        elif op == '3':
            print(f"Primeiro: {f.primeiro()}")
        elif op == '0':
            break