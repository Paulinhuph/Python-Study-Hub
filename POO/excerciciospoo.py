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


# ex007
# Crie uma classe Aluno com nome e uma lista de notas.
# Adicione um método que calcule e retorne a média das notas.


# ex008
# Crie uma classe Calculadora que possua métodos para somar, subtrair,
# multiplicar e dividir dois números passados como argumento.


# ex009
# Crie uma classe Produto com nome, preco e quantidade_estoque.
# Adicione um método calcular_total_estoque().


# ex010
# Crie uma classe Funcionario com nome, cargo e salario.
# Adicione um método aumentar_salario(porcentagem).


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