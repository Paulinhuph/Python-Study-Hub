# ex001
# Crie uma classe Pessoa com os atributos nome e idade.
# Exiba esses dados na tela.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa("Paulo", 21)
print(f"Nome: {p1.nome}  idade: {p1.idade}")


# ex002
# Crie uma classe Livro com os atributos titulo, autor e paginas.
# Adicione um método para exibir os detalhes do livro.
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"
    
p1 = Livro("O Estrangeiro.", "Albert Camus", 165)
print(p1)


# ex003
# Crie uma classe Retangulo com os atributos largura e altura.
# Adicione um método chamado calcular_area().
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def calcular_area(self):
        return self.largura * self.altura
         
p1 = Retangulo(20, 10)
print(f"Área do Retângulo: {p1.calcular_area()}")


# ex004
# Crie uma classe Circulo com o atributo raio.
# Adicione um método para calcular o perímetro.
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_perimetro(self):
        return self.raio * (2 * 3.14)
    
p1 = Circulo(20)
print(f"O Perímetro é: {p1.calcular_perimetro()}")


# ex005
# Crie uma classe ContaBancaria com os atributos titular e saldo.
# Adicione métodos para depositar() e sacar().
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor_do_deposito):
        self.saldo += valor_do_deposito

    def sacar(self, valor_do_saque):
        self.saldo -= valor_do_saque
# ---- Programa Principal ----
minha_conta = ContaBancaria("Paulo", 2000)
print(f"Saldo Inicial do {minha_conta.titular}: R$ {minha_conta.saldo}")

minha_conta.depositar(50)
print(f"Saldo Após depósito: R$ {minha_conta.saldo}")

minha_conta.sacar(10)
print(f"Saldo Após saque: R$ {minha_conta.saldo}")


# ex006
# Crie uma classe Carro com os atributos marca, modelo e velocidade_atual.
# Adicione os métodos acelerar() e frear().
class Carro:
    def __init__(self, marca, modelo, velocidade_atual):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual

    def acelerar(self, valor_aceleracao):
        self.velocidade_atual += valor_aceleracao

    def frear(self, valor_frenagem):
        self.velocidade_atual -= valor_frenagem
# --- Programa Principal ---
meu_carro = Carro("Ford", "Ford Ka+", 120)
print(f"Marca: {meu_carro.marca}, Modelo: {meu_carro.modelo}, Velocidade_Atual: {meu_carro.velocidade_atual}")

meu_carro.acelerar(20)
print(f"Velocidade atual após acelerar: {meu_carro.velocidade_atual}")

meu_carro.frear(60)
print(f"Velocidade atual após frear: {meu_carro.velocidade_atual}")


# ex007
# Crie uma classe Aluno com nome e uma lista de notas.
# Adicione um método que calcule e retorne a média das notas.
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calculo_media(self):
        return sum(self.notas) / len(self.notas) # Len conta quantos elemento existem na lista
                                                 # Sum soma todos elementos da lista
a1 = Aluno("Paulo Ricardo", [9, 8.5, 6.9, 8])
print(f"Aluno: {a1.nome}, Média de Notas: {a1.calculo_media()}")


# ex008
# Crie uma classe Calculadora que possua métodos para somar, subtrair,
# multiplicar e dividir dois números passados como argumento.
class Calculadora:
    def somar(self, n1, n2):
        return n1 + n2
    
    def subtrair(self, n1, n2):
        return n1 - n2
    
    def multiplicar(self, n1, n2):
        return n1 * n2
    
    def dividir(self, n1 ,n2):
        return n1 / n2

minha_calculadora = Calculadora()
print(f"Soma: {minha_calculadora.somar(60, 40)}")
print(f"Subtração: {minha_calculadora.subtrair(60, 40)}")
print(f"Multiplicação: {minha_calculadora.multiplicar(60, 40)}")
print(f"Divisão: {minha_calculadora.dividir(60, 40)}")


# ex009
# Crie uma classe Produto com nome, preco e quantidade_estoque.
# Adicione um método calcular_total_estoque().
class Produto():
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome 
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    

    def calcular_total_estoque(self):
        return self.quantidade_estoque * self.preco 

# --- Programa Principal ---
total_estoque = Produto("Samsung Galaxy S25", 3000, 4)
print(f"Produto: {total_estoque.nome} | Preço: {total_estoque.preco} | Estoque: {total_estoque.quantidade_estoque}")
total_estoque.calcular_total_estoque()
print(f"Valor Total do Estoque: R$ {total_estoque.calcular_total_estoque()}")


# ex010
# Crie uma classe Funcionario com nome, cargo e salario.
# Adicione um método aumentar_salario(porcentagem).
# ex010
# Crie uma classe Funcionario com nome, cargo e salario.
# Adicione um método aumentar_salario(porcentagem).
class Funcionario: 
    def __init__(self, nome, cargo, salario):
        self.nome = nome 
        self.cargo = cargo
        self.salario = salario

    def aumentar_salario(self, porcentagem):
        calculo = (self.salario * porcentagem) / 100
        self.salario += calculo
        return self.salario
# --- Programa Principal ---
calculo_salario = Funcionario("Paulo", "T.I", 3500)
print(f"Salário Atual: R$ {calculo_salario.salario}")

print(f"Novo Salário: R$ {calculo_salario.aumentar_salario(0.5)}")


# ex011
# Crie uma classe Triangulo com três atributos representando seus lados.
# Crie um método para verificar se o triângulo é válido.


# ex012
# Crie uma classe Celular com marca, modelo e bateria (0 a 100).
# Adicione métodos para gastar_bateria() e carregar().


# ex013
# Crie uma classe Relogio com atributos hora, minuto e segundo.
# Adicione um método passar_tempo() que avança um segundo.


# ex014
# Crie uma classe Paciente com nome e historico_medico (lista de strings).
# Adicione um método para registrar uma nova consulta.


# ex015
# Crie uma classe Temperatura que armazene um valor em Celsius.
# Adicione métodos para retornar esse valor em Fahrenheit e Kelvin.


# ex016
# Crie uma classe Dado (jogo) com um atributo lados.
# Adicione um método rolar() que retorne um número aleatório.


# ex017
# Crie uma classe Agenda que armazene uma lista de contatos (nome e telefone).
# Adicione métodos para adicionar contatos e buscar telefones.


# ex018
# Crie uma classe Musica com titulo, artista e duracao_segundos.
# Adicione um método para exibir a duração no formato MM:SS.


# ex019
# Crie uma classe Televisao com atributos canal e volume.
# Adicione métodos para aumentar/diminuir volume e trocar de canal.


# ex020
# Crie uma classe Fracao com numerador e denominador.
# Adicione um método para multiplicar duas frações.