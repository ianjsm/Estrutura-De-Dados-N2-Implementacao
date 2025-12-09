from Exercicio01 import Pilha, Fila

def executar():
    print("Exercício 11")
    texto = input("Digite a palavra/frase: ").replace(" ", "").lower()
    
    p = Pilha()
    f = Fila()
    
    for char in texto:
        p.empilhar(char)
        f.inserir(char)
        
    palindromo = True
    while not p.vazia():
        if p.desempilhar() != f.remover():
            palindromo = False
            break
            
    print("É palíndromo" if palindromo else "Não é palíndromo")