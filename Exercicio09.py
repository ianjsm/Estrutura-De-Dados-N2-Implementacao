from Exercicio01 import Pilha

def converter_prefixa(expr):
    p = Pilha()
    tokens = expr.split()[::-1]
    
    for t in tokens:
        if t not in "+-*/":
            p.empilhar(t)
        else:
            op1 = p.desempilhar()
            op2 = p.desempilhar()
            infixa = f"({op1} {t} {op2})"
            posfixa = f"{op1} {op2} {t}"
            p.empilhar(infixa)
            
    return p.desempilhar()

def executar():
    print("Exercício 9")
    entrada = input("Digite expressão prefixa (exemplo: + 3 4): ")
    try:
        res = converter_prefixa(entrada)
        print(f"Infixa: {res}")
    except:
        print("Erro na expressão.")