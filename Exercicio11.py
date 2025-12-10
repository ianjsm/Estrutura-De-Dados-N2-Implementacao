from Exercicio01 import ArrayStack, ArrayQueue

def verificar_palindromo(texto):
    S = ArrayStack()
    Q = ArrayQueue()

    texto_limpo = texto.replace(" ", "").lower()
    
    for char in texto_limpo:
        S.push(char)
        Q.enqueue(char)

    comprimento = len(texto_limpo)
    eh_palindromo = True
    
    for _ in range(comprimento):
        char_pilha = S.pop()   
        char_fila = Q.dequeue() 
        
        if char_pilha != char_fila:
            eh_palindromo = False
            break
            
    return eh_palindromo

def testar_exercicio_11():
    print("--- [Exercício 11] Verificador de Palíndromos ---")
    
    casos = [
        "arara",           
        "ovo",             
        "python",            
        "Socorram me subi no onibus em Marrocos",
        "Ame o poema",       
        "Estrutura de Dados"  
    ]
    
    for texto in casos:
        resultado = verificar_palindromo(texto)
        status = "É Palíndromo" if resultado else "NÃO é"
        print(f"'{texto}' -> {status}")

if __name__ == "__main__":
    testar_exercicio_11()