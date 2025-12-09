from Exercicio01 import Pilha

def validar(expr):
    p = Pilha()
    pares = {')':'(', ']':'[', '}':'{'}
    
    for char in expr:
        if char in "({[":
            p.empilhar(char)
        elif char in ")}]":
            if p.vazia() or p.desempilhar() != pares[char]:
                return False
    return p.vazia()

def executar():
    print("Exercício 8")
    expr = input("Digite a expressão matemática: ")
    if validar(expr):
        print("Expressão Correta!")
    else:
        print("Expressão Incorreta!")