from Exercicio01 import ArrayStack

def verificar_expressao(expressao):
    pilha = ArrayStack()

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    aberturas = "({["
    fechamentos = ")}]"

    for caractere in expressao:
        if caractere in aberturas:
            pilha.push(caractere)
            
        elif caractere in fechamentos:
            if pilha.is_empty():
                return False

            topo = pilha.pop()

            esperado = pares[caractere]
            
            if topo != esperado:
                return False 

    return pilha.is_empty()

def testar_exercicio_08():
    
    testes = [
        ("Correto simples", "(A+B)"),
        ("Correto aninhado", "{[A + (B*C)]}"),
        ("Errado (sobra abertura)", "((A+B)"),
        ("Errado (fecha errado)", "(A+B]"),
        ("Errado (começa fechando)", ")A+B("),
        ("Errado (ordem trocada)", "([A+B)]") 
    ]
    
    for nome, expr in testes:
        resultado = verificar_expressao(expr)
        status = "OK" if resultado else "ERRO"
        print(f"Teste '{nome}': {expr} -> {status}")

if __name__ == "__main__":
    testar_exercicio_08()