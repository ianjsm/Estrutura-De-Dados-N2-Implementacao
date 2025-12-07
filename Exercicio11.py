from Exercicio01 import ArrayStack, ArrayQueue

def verificar_palindromo(texto):
    """
    Exercício 11: Verifica se uma string é um palíndromo usando Pilha e Fila.
    
    Lógica:
    - A Fila devolve os caracteres na ordem original (frente -> trás).
    - A Pilha devolve os caracteres na ordem inversa (trás -> frente).
    - Se for palíndromo, as duas sequências devem ser idênticas.
    """
    S = ArrayStack()
    Q = ArrayQueue()
    
    # Normalização básica: remover espaços e deixar minúsculo
    # Ex: "A cara rajada da jararaca" -> "acararajadadajararaca"
    texto_limpo = texto.replace(" ", "").lower()
    
    # 1. Preencher as estruturas
    for char in texto_limpo:
        S.push(char)
        Q.enqueue(char)
        
    # 2. Comparar elemento a elemento
    comprimento = len(texto_limpo)
    eh_palindromo = True
    
    for _ in range(comprimento):
        # Removemos das duas estruturas
        char_pilha = S.pop()     # Vem do fim (reverso)
        char_fila = Q.dequeue()  # Vem do início (original)
        
        if char_pilha != char_fila:
            eh_palindromo = False
            break # Já sabemos que não é, pode parar
            
    return eh_palindromo

def testar_exercicio_11():
    print("--- [Exercício 11] Verificador de Palíndromos ---")
    
    casos = [
        "arara",              # Sim
        "ovo",                # Sim
        "python",             # Não
        "Socorram me subi no onibus em Marrocos", # Sim (frase clássica)
        "Ame o poema",        # Sim
        "Estrutura de Dados"  # Não
    ]
    
    for texto in casos:
        resultado = verificar_palindromo(texto)
        status = "É Palíndromo" if resultado else "NÃO é"
        print(f"'{texto}' -> {status}")

if __name__ == "__main__":
    testar_exercicio_11()