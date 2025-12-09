from Exercicio01 import Pilha

def esvaziar_recursivo(pilha):
    if pilha.vazia():
        return
    pilha.desempilhar()
    esvaziar_recursivo(pilha)

def executar():
    print("--- Exercício 4: Esvaziar Recursivo ---")
    p = Pilha()
    entrada = input("Preencha a pilha (espaços): ")
    for x in entrada.split():
        p.empilhar(x)
        
    print(f"Antes: {p._dados}")
    esvaziar_recursivo(p)
    print(f"Depois: {p._dados}")