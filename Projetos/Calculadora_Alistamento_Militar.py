from datetime import datetime 

def calculo_idade(ano_nascimento):

# Função Responsável por calcular a idade exata do Jovem
    ano_atual = datetime.now().year # Guarda o Ano Atual
    idade_do_jovem = ano_atual - ano_nascimento
    return idade_do_jovem

def calculo_alistamento(idade_do_jovem):
# Função que realiza o cálculo do Alistamento
    idade_alistamento = 18

    # laços de Condicionais para devolver a mensagem correta
    if idade_do_jovem < idade_alistamento:
        faltam = idade_alistamento - idade_do_jovem
        return f"Faltam: {faltam} ano(s) para o seu Alistamento Militar."
    
    elif idade_do_jovem == idade_alistamento:
        return "Chegou a Hora de se Alistar! Procure a Junta Militar."

    else:
        passaram =  idade_do_jovem - idade_alistamento 
        return f"Passaram {passaram} ano(s) do Alistamento Militar."
    
def main(): 
    print("---- Calculadora de Alistamento Militar ----")
    try: 
        ano_nascimento = int(input("Digite o Ano de seu Nascimento (Ex:2004): "))
        # Função calculo_idade faz o cálculo, e devolve o resultado que será guardado na variável idade_final
        idade_final = calculo_idade(ano_nascimento) 
        # Passamos a variável externa para a próxima função: calculo_alistamento
        resultado = calculo_alistamento(idade_final) 
        # Exibição do Programa:
        print(resultado)
    except ValueError:
        print("\nErro: Por favor, digite um ano válido com números.")

if __name__ == '__main__':
    main()