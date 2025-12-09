from Exercicio01 import Pilha

def executar():
    print("Exercício 2")
    p = Pilha()
    while True:
        print(f"\Pilha atual: {p._dados}")
        op = input("1.Empilhar 2.Desempilhar 3.Topo 0.Voltar: ")
        if op == '1':
            v = input("Valor: ")
            p.empilhar(v)
        elif op == '2':
            print(f"Removido: {p.desempilhar()}")
        elif op == '3':
            print(f"Topo: {p.topo()}")
        elif op == '0':
            break