from Exercicio01 import ArrayStack

def verificar_expressao(expressao):
    """
    Exercício 8: Verifica se parênteses, colchetes e chaves estão bem formados.
    Retorna True se estiver correto, False caso contrário.
    """
    pilha = ArrayStack()
    
    # Definindo os pares: quem fecha -> quem abre
    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    aberturas = "({["
    fechamentos = ")}]"

    for caractere in expressao:
        if caractere in aberturas:
            # Se é um símbolo de abrir, coloca na pilha
            pilha.push(caractere)
            
        elif caractere in fechamentos:
            # Se é um símbolo de fechar:
            
            # 1. Se a pilha estiver vazia, fechou algo sem abrir antes -> Erro
            if pilha.is_empty():
                return False
            
            # 2. Remove o último que abriu
            topo = pilha.pop()
            
            # 3. Verifica se o topo combina com o fechamento atual
            # pares[caractere] me dá o par de abertura esperado.
            # Ex: se caractere é '}', pares['}'] é '{'.
            esperado = pares[caractere]
            
            if topo != esperado:
                return False # Ex: abriu '(' mas tentou fechar '}'

    # Ao final, a pilha deve estar vazia. Se sobrou item, faltou fechar.
    return pilha.is_empty()

def testar_exercicio_08():
    print("--- [Exercício 08] Verificador de Delimitadores ---")
    
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