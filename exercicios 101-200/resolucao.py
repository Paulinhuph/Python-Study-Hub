# Exc 101
import random
numero_secreto = random.randint(1, 5) # Devolve um número aleátorio de 1 a 5
def main():
    tentativas = 0
    limite_maximo = 5

    while tentativas < limite_maximo:    

        tentativas += 1 # Soma um a cada tentativa

        # --- Programa Principal ---
        numero_jogador = int(input("Tente Acertar o Número Secreto (1 a 5): "))

        if numero_jogador == numero_secreto:
            print(f"Parábens! Você acertou o número secreto: {numero_secreto}")
            print(f"Em {tentativas} tentativas.")
            break

    if numero_jogador != numero_secreto:
        print(f"Que Pena! Você não acertou, o número secreto era: {numero_secreto}")
if __name__ == '__main__':
    main()


# Exc 102
import random
numero_secreto = random.randint(1, 10) # Devolve um número aleátorio de 1 a 10
def main():
    tentativas = 0
    limite_maximo = 4

    while tentativas < limite_maximo:    

        tentativas += 1 # Soma um a cada tentativa

        # --- Programa Principal ---
        numero_jogador = int(input("Tente Acertar o Número Secreto (1 a 10): "))

        if numero_jogador == numero_secreto:
            print(f"Parábens! Você acertou o número secreto: {numero_secreto}")
            print(f"Em {tentativas} tentativas.")
            break

    if numero_jogador != numero_secreto:
        print(f"Que Pena! Você não acertou, o número secreto era: {numero_secreto}")
if __name__ == '__main__':
    main()


# Exc 103
def main():
    # --- Programa Principal ---
    nome_funcionario = input("Digite o Seu Nome: ")
    salario_funcionario = float(input("Digite o Seu Salário: "))

    print(f"Olá! Caro Colaborador(a) {nome_funcionario}")
    print(f"Salário refente a esse Mês: {salario_funcionario:.2f}")
if __name__ == '__main__':
    main()

# Exc 104
def main():
    # --- Programa ---
    with open("arquivo.txt", "r", encoding='UTF-8') as arquivo:
        total_linhas = sum(1 for linha in arquivo)
        # SUM conta linha por linha 
    print(f"Total de Linhas no Arquivo: {total_linhas}.")
   
if __name__ == '__main__':
    main()


# Exc 105
def main():
    # --- Programa Principal ---
    numero_digitado = int(input("Digite um número menor que (1000): "))
    
    if numero_digitado < 1000:
        # Lógica Matemática para Descobrir Centenas, Dezenas e Unidades
        unidade = numero_digitado % 10 # O resto será a unidade
        dezena = (numero_digitado // 10) % 10
        centena = numero_digitado // 100

        print(f"Temos {centena} centenas")
        print(f"Temos {dezena} dezenas")
        print(f"Temos {unidade} unidades")
    
    else:
        print("Erro! Digite um número válido menor que 1000.")
        
if __name__ == '__main__':
    main()

# Exc 106 
def palindromo(palavra):
    # Replace substitui uma ocorrência por outra, aqui é feito uma formatação para evitar erros
    formatada = palavra.replace(" ", "").lower()
    return formatada == formatada[::-1] # EXEMPLO: [Python] -> [nothyp]

def main():
    # --- Programa Principal ---
    while True:
        palavra = input("Digite uma Palavra ou Frase: ")
        # Faz a comparação da palavra digitada com ela mesma ao contrário
        if palindromo(palavra):
            print(f"A palavra ou Frase digitada: '{palavra}' é um Palíndromo!")
        else:
            print("A palavra NÃO é um Palíndromo!")

if __name__ == '__main__':
    main()


# Exc 107
def main():
    while True:
        letra_digitada = input("Digite uma Letra: ").lower().strip()
        if letra_digitada in ['a', 'e', 'i', 'o', 'u']:
            print(f"Letra Digitada é uma Vogal.")
        else:
            print("Letra Digitada é uma consoante.")
        
if __name__ == '__main__':
    main()


# Exc 108
def numero_palavras(texto):
    palavras = texto.split()
    quantidade = len(palavras)
    return quantidade

def main():
    while True:
        texto = input("Digite um Texto: ").lower().strip()

        resultado = numero_palavras(texto)

        print(f"O Texto contém {resultado} palavras.")

if __name__ == '__main__':
    main()

# Exc 109 
numeros_totais = []
numero_acima_5 = 0
numeros_divisiveis = 0

def main():
    import random
    for i in range(20):
        
        numeros_sorteados = random.randint(0, 10)
        numeros_totais.append(numeros_sorteados)
        
        if numeros_sorteados > 5:
            numero_acima_5 += 1

        if numeros_sorteados % 3 == 0 and numeros_sorteados > 0:
            numeros_divisiveis += 1

    print(f"a) Números Sorteados: {numeros_totais}")
    print(f"b) Total de Números acima de 5: {numero_acima_5}")
    print(f"c) Total de Números divisíveis por 3: {numeros_divisiveis}")

if __name__ == "__main__":
    main()


# Exc 110
lista = []
def elementos_nao_repetidos(lista):
    nao_repetidos = [item for item in lista if lista.count(item) == 1]
    return nao_repetidos


while True:
    elementos_lista = input("Digite os elementos da sua Lista: ").lower().strip()
    lista.append(elementos_lista)

    deseja_cadastrar = input("Deseja Cadastrar mais Itens? (sim/não): ").lower().strip()
    if deseja_cadastrar in ["n", "nao", "não"]:
        break
    
# --- Programa Principal --- 

resultado = elementos_nao_repetidos(lista)
print(f"Elementos não Repetidos: {resultado}")
