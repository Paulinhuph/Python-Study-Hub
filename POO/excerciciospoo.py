# 🧱 Bloco 1: Classes, Atributos e Métodos Básicos
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
# Crie um método para verificar se o triângulo:
# Equilátero: Possui os três lados iguais.
# Isósceles: Possui dois lados iguais e um diferente.
# Escaleno: Possui três lados diferentes (nenhum igual)
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def verificar_trtiangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "O Triângulo é: Equilátero."
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "O Triângulo é: Isósceles!"
        else:
            return "O Triãngulo é: Escaleno"
        
tipo_triangulo = Triangulo(5, 4, 6)
print(tipo_triangulo.verificar_trtiangulo())


# ex012
# Crie uma classe Celular com marca, modelo e bateria (0 a 100).
# Adicione métodos para gastar_bateria() e carregar().
class Celular:
    def __init__(self, marca, modelo, bateria):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria

    def gastar_bateria(self, bateria_descarregada):
        self.bateria -= bateria_descarregada

    def carregar(self, bateria_carregada):
        self.bateria += bateria_carregada
        if self.bateria > 100:
            self.bateria = 100 # Número de carregamento não passa de 100%

meu_celular = Celular("Samsung", "Galaxy S25", 85)
print(f"Marca: {meu_celular.marca} | Modelo: {meu_celular.modelo} | Bateria Atual: {meu_celular.bateria}%")

meu_celular.gastar_bateria(20)
print(f"Valor após gasto de bateria: {meu_celular.bateria}%")

meu_celular.carregar(50)
print(f"Valor após carregamento de bateria: {meu_celular.bateria}%")


# ex013
# Crie uma classe Relogio com atributos hora, minuto e segundo.
# Adicione um método passar_tempo() que avança um segundo.
class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto 
        self.segundo = segundo

    def passar_tempo(self):
        # Método chamado, então é adicionado 1 segundo ao relógio
        self.segundo += 1

        # O Efeito dominó!
        # Primeiro: se os segundos chegarem a 60s
        # É reiniciado os segundos para 00
        # E jogamos mais um minuto para a próxima
        if self.segundo == 60:
            self.segundo = 0
            self.minuto += 1
        # Segundo: se os minutos chegarem a 60
        # Reiniciamos os minutos para 00
        # E "jogamos" 1 hora para a próxima casa
            if self.minuto == 60:
                self.minuto = 0 
                self.hora += 1
                # Terceiro: As horas chegaram ao limite de 24 (Meia-noite)?
                # (Esta checagem só acontece se os minutos também tiverem virado)
                if self.hora == 24:
                    self.hora = 0 # Reiniciamos as horas para 00, começando um novo dia!

# --- PROGRAMA PRINCIPAL ---
# Testando o caso extremo: 23:59:59 para 00:00:00
meu_relogio = Relogio(23, 59, 59)
print(f"Horário Inicial: {meu_relogio.hora:02d}:{meu_relogio.minuto:02d}:{meu_relogio.segundo:02d}")
# Chamando o método sem passar nada no parêntese
meu_relogio.passar_tempo()
print(f"Após 1 segundo:  {meu_relogio.hora:02d}:{meu_relogio.minuto:02d}:{meu_relogio.segundo:02d}")


# ex014
# Crie uma classe Paciente com nome e historico_medico (lista de strings).
# Adicione um método para registrar uma nova consulta.
class Paciente:
    def __init__(self, nome, historico_medico):
        self.nome = nome
        self.historico_medico = historico_medico

    def registrar_consulta(self, nova_consulta):
        # Adiciona o texto da nova consulta direto na lista do paciente
        self.historico_medico.append(nova_consulta)
# --- Programa Principal ---
meu_prontuario = Paciente("Lucas", [])
meu_prontuario.registrar_consulta("03 - 06 - 2026 | Hipertensão Arterial")
print(f"Nome: {meu_prontuario.nome}")
print(f"Histórico Médico: {meu_prontuario.historico_medico}")


# ex015
# Crie uma classe Temperatura que armazene um valor em Celsius.
# Adicione métodos para retornar esse valor em Fahrenheit e Kelvin.
class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def valor_fahrenheit(self):
        return (self.celsius * 1.8) + 32
      
    def valor_kelvin(self):
        return self.celsius + 273.15
# --- Programa Principal ---
temp = Temperatura(30)
print(f"Temperatura em ºC: {temp.celsius}")
print(f"Temperatura em ºF: {temp.valor_fahrenheit()}")
print(f"Temperatura em ºK: {temp.valor_kelvin()}")


# ex016
# Crie uma classe Dado (jogo) com um atributo lados.
# Adicione um método rolar() que retorne um número aleatório.
import random
class Dado:
    def __init__(self, lados):
        self.lados = lados

    def rolar(self):
        return random.randint(1, self.lados)
# --- Programa Principal ---
jogar_dado_comum = Dado(6)
print(f"Dado foi jogado: {jogar_dado_comum.rolar()}")


# ex017
# Crie uma classe Agenda que armazene uma lista de contatos (nome e telefone).
# Adicione métodos para adicionar contatos e buscar telefones.
class Agenda:
    def __init__(self):
        self.contato = {}

    def adicionar_contato(self, nome, telefone):
        self.contato[nome] = telefone
        print(f"Contato '{nome}' adicionado com sucesso!")

    def buscar_telefones(self, nome):
        telefone = self.contato.get(nome) # get busca valores em dicionários, evita erros caso n exi sta
        return f"O Telefone de {nome} é: {telefone}"

# --- Programa Principal ---
minha_agenda = Agenda()
# Adiciona
minha_agenda.adicionar_contato("Paulo", "11-99999-0000")
# Busca
print(minha_agenda.buscar_telefones("Paulo"))

# ex018
# Crie uma classe Musica com titulo, artista e duracao_segundos.
# Adicione um método para exibir a duração no formato MM:SS.
class Musica:
    def __init__(self, titulo, artista, duracao_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracao_segundos = duracao_segundos

    def exibir_duracao(self):
        minutos = self.duracao_segundos // 60 # divisão inteira
        segundos_restantes = self.duracao_segundos % 60 # resto da divisão
        return f"{minutos}:{segundos_restantes}"
        
# --- Programa Principal ---
playlist = Musica("The Trooper", "Iron Maiden", 253)
print(f"Música: {playlist.titulo}")
print(f"Artista(s): {playlist.artista}")
print(f"Duração: {playlist.exibir_duracao()}")


# ex019
# Crie uma classe Televisao com atributos canal e volume.
# Adicione métodos para aumentar/diminuir volume e trocar de canal.
class Televisao: 
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def aumentar_volume(self):
        self.volume += 1
        if self.volume > 100:
            self.volume = 100 # Não passa de 100%

    def diminuir_volume(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0

    def trocar_canal(self, novo_canal):
        if self.canal != novo_canal:
            self.canal = novo_canal

# --- Programa Principal ---
assistir = Televisao(5, 80)
print(f"Canal Atual: {assistir.canal} ")
print(f"Volume Atual: {assistir.volume}")
# Aumentar Volume
assistir.aumentar_volume()
print(f"Volume Aumentado: {assistir.volume}")
# Diminuir Volume
assistir.diminuir_volume()
print(f"Volume Diminuido: {assistir.volume}")
# Mudar Canal
assistir.trocar_canal(7)
print(f"Novo Canal: {assistir.canal}")


# ex020
# Crie uma classe Fracao com numerador e denominador.
# Adicione um método para multiplicar duas frações.


# 🔒 Bloco 2: Construtores e Encapsulamento
# ex021: Crie uma classe Usuario onde a senha deve ser privada. 
# e só pode ser alterada se a senha antiga for informada corretamente.

# ex022: Crie uma classe ContaCorrente que possua um limite de cheque especial. 
# Garanta que o saldo nunca fique menor que o limite negativo permitido.

# ex023: Crie uma classe Cofre com um atributo privado codigo_seguranca. 
# Adicione um método para tentar abrir o cofre informando o código.

# ex024: Crie uma classe Termometro onde o atributo temperatura_celsius 
# possui métodos getters e setters que impedem valores abaixo do zero absoluto (-273.15°C).

# ex025: Crie uma classe Identificacao onde o atributo 
# cpf seja validado no construtor (deve ter exatamente 11 dígitos numéricos).

# ex026: Crie uma classe Ingresso com um preço base. 
# Use encapsulamento para garantir que o preço nunca seja alterado para um valor menor ou igual a zero.

# ex027: Crie uma classe Contador que possui um atributo privado valor. 
# Crie métodos para incrementar, decrementar e ver o valor atual, sem permitir alteração direta.

# ex028: Crie uma classe Filme onde a classificacao_indicativa (livre, 12, 14, 16, 18) 
# só possa ser alterada por métodos específicos que validem essas opções.

# ex029: Crie uma classe Luz com um atributo privado booleano ligada. 
# Crie o método alternar() que muda o estado atual da luz.

# ex030: Crie uma classe CartaoCredito que armazene o 
# numero, titular, limite e saldo_devedor de forma protegida ou privada.

# ex031: Crie uma classe Cronometro com métodos privados 
# de contagem e métodos públicos iniciar() e pausar().

# ex032: Crie uma classe Estudante onde a matricula é 
# gerada automaticamente pelo construtor e não pode ser alterada por ninguém.

# ex033: Crie uma classe ConfiguracaoSistema onde as 
# propriedades de idioma e tema sejam privadas, acessadas apenas por propriedades/getters.

# ex034: Crie uma classe Passaporte que receba o 
# nome do cidadão e o país de origem, gerando um número de registro privado imutável.

# ex035: Crie uma classe Playlist que possui uma lista privada 
# de músicas e métodos públicos para adicionar, remover e listar as faixas.

# ex036: Crie uma classe Previdencia que recebe depósitos mensais 
# privados e calcula o rendimento baseado em uma taxa interna oculta.

# ex037: Crie uma classe Robo com coordenadas privadas x e y. 
# Crie métodos públicos mover_norte(), mover_sul(), etc., atualizando as posições de forma controlada.

# ex038: Crie uma classe Relatorio com um atributo textual privado conteudo. 
# Permita apenas adicionar texto ao final do relatório, nunca apagar o que já foi escrito.

# ex039: Crie uma classe BancoDeDados que simule uma URL de conexão privada que só pode ser configurada uma vez no construtor.

# ex040: Crie uma classe BilheteUnico com saldo privado. Crie o método passar_na_catraca() que desconta um valor fixo se houver saldo suficiente.


# 🌿 Bloco 3: Herança e Associação entre Objetos
#  ex041: Crie uma classe base Veiculo e duas classes derivadas: Moto (com atributo cilindradas) e Caminhao (com atributo eixos).
#  ex042: Crie uma classe Animal com o método emitir_som(). Crie as classes filhas Cachorro e Gato que herdam de Animal.
# • [ ] ex043: Crie uma classe Funcionario e uma classe filha Gerente que possui um atributo adicional bonus_anual.
# • [ ] ex044: Crie uma classe Pessoa e uma filha Cliente que possui os atributos data_cadastro e total_compras.
# • [ ] ex045: Crie uma classe Imovel com endereco e preco_base. Crie ImovelNovo (com acréscimo no preço) e ImovelVelho (com desconto no preço) como subclasses.
# • [ ] ex046: Crie uma classe DispositivoEletronico. Crie as subclasses Smartphone e Laptop herdando características comuns da classe base.
# • [ ] ex047: Crie uma classe PassagemAerea. Crie a subclasse PassagemPrimeiraClasse que herda da classe base e inclui direito a despacho de bagagem extra gratuito.
# • [ ] ex048: Crie uma classe IngressoCinema e uma classe filha MeiaEntrada que calcula automaticamente metade do preço do ingresso base.
# • [ ] ex049: [Associação] Crie uma classe Motor e uma classe Carro. O Carro deve ter um atributo que recebe um objeto do tipo Motor.
# • [ ] ex050: [Associação] Crie uma classe Autor e uma classe Livro. A classe Livro deve receber um objeto da classe Autor em seu construtor.
# • [ ] ex051: [Associação] Crie uma classe ItemPedido (produto e quantidade) e uma classe Pedido que armazena uma lista de objetos ItemPedido.
# • [ ] ex052: Crie uma classe MembroUniversidade. Crie as subclasses Professor e Coordenador herdando dela.
# • [ ] ex053: Crie uma classe FormaGeometrica. Crie as subclasses Quadrado e Triangulo que herdam suas propriedades de localização espacial.
# • [ ] ex054: Crie uma classe Assinatura (serviço de streaming). Crie AssinaturaPremium como filha, adicionando suporte a telas simultâneas.
# • [ ] ex055: [Associação] Crie uma classe Bateria e uma classe Lanterna. A lanterna precisa de um objeto bateria para executar o método ligar().
# • [ ] ex056: Crie uma classe Atleta e uma subclasse Corredor que possui o atributo privado tempo_recorde.
# • [ ] ex057: Crie uma classe Restaurante e uma subclasse Pizzaria que possui uma lista específica de sabores de pizza disponíveis.
# • [ ] ex058: [Associação] Crie uma classe Endereco e uma classe Empresa. A empresa deve conter um objeto do tipo Endereco.
# • [ ] ex059: Crie uma classe Computador composta por objetos das classes Processador, MemoriaRAM e DiscoRigido.
# • [ ] ex060: Crie uma classe Hotel que gerencie uma lista de objetos do tipo Quarto.

# 🎭 Bloco 4: Polimorfismo e Classes Abstratas
# • [ ] ex061: Crie uma classe abstrata Forma com um método abstrato area(). Implemente as subclasses Retangulo e Circulo sobrescrevendo esse método.
# • [ ] ex062: Crie uma classe MeioDeTransporte com o método mover(). Sobrescreva o método nas classes Aviao (voando), Carro (andando) e Navio (navegando).
# • [ ] ex063: Crie uma classe abstrata Conta com o método abstrato atualizar_saldo(). Implemente ContaPoupanca (aplica rendimento) e ContaCorrente (desconta taxa).
# • [ ] ex064: Crie uma classe Impressora com o método imprimir(documento). Crie ImpressoraLaser e ImpressoraJatoEscore que executam a impressão de formas diferentes.
# • [ ] ex065: Crie uma classe abstrata Funcionario com o método calcular_folha(). Implemente as subclasses FuncionarioHorista e FuncionarioClt.
# • [ ] ex066: Crie uma lista contendo diferentes objetos que herdam de Animal. Percorra a lista fazendo todos emitirem som polimorficamente.
# • [ ] ex067: Crie uma classe abstrata Notificacao com o método enviar(mensagem). Implemente as subclasses EmailNotificacao, SmsNotificacao e PushNotificacao.
# • [ ] ex068: Crie uma classe Arquivo com o método abrir(). Crie subclasses ArquivoPdf e ArquivoZip que implementam suas próprias formas de abertura.
# • [ ] ex069: Crie uma classe abstrata Pagamento com o método processar(). Crie as subclasses PagamentoBoleto, PagamentoCartao e PagamentoPix.
# • [ ] ex070: Crie uma classe Bebida com o método preparar(). Crie subclasses Cafe e Cha que modificam as etapas de preparação do método original.
# • [ ] ex071: Crie uma classe abstrata Criptografia com os métodos abstratos encriptar() e decriptar(). Implemente uma subclasse que use uma lógica de inversão de texto.
# • [ ] ex072: Crie um sistema de jogos onde a classe base Personagem possui o método atacar(). Subclasses Guerreiro (ataca com espada) e Mago (ataca com magia) devem sobrescrever o método.
# • [ ] ex073: Crie uma classe abstrata Relatorio com o método gerar_cabecalho(). Crie subclasses RelatorioPdf e RelatorioHtml.
# • [ ] ex074: Crie uma classe Sensor com o método ler_dados(). Crie as subclasses SensorTemperatura e SensorUmidade retornando seus respectivos tipos de dados simulados.
# • [ ] ex075: Crie uma classe abstrata UsuarioSistema com o método verificar_permissao(). Implemente Admin (retorna True para tudo) e Operador (restrito).
# • [ ] ex076: Crie uma classe InstrumentoMusical com o método tocar(). Implemente as subclasses Violao, Piano e Flauta.
# • [ ] ex077: Crie uma classe abstrata Armazenamento com os métodos salvar() e deletar(). Implemente ArmazenamentoLocal e ArmazenamentoNuvem.
# • [ ] ex078: Crie uma classe Brinquedo com o método mover(). Crie as subclasses CarroControleRemoto e AviaoBrinquedo.
# • [ ] ex079: Crie uma classe abstrata Validador com o método validar(dados). Crie subclasses para validar e-mails e validar telefones.
# • [ ] ex080: Crie um método que receba uma lista de objetos do tipo FormaGeometrica e desenhe todos na tela chamando o método polimórfico desenhar().

# 🚀 Bloco 5: Métodos Estáticos, Interfaces e Recursos Avançados
# • [ ] ex081: Crie uma classe ConversorUnidades que possua apenas métodos estáticos para converter metros em centímetros, e quilômetros em milhas.
# • [ ] ex082: Crie uma classe ValidadorMatematico com um método estático para verificar se um número é primo.
# • [ ] ex083: Crie uma classe Config que use um atributo de classe (estático) para contar quantas instâncias da classe foram criadas no sistema.
# • [ ] ex084: Simule uma Interface chamada Autenticavel que obrigue a implementação do método login(). Implemente-a nas classes Diretor e Cliente.
# • [ ] ex085: Simule uma Interface chamada PegadaDeCarbono com o método calcular_impacto(). Implemente-a nas classes Predio, Carro e Escola.
# • [ ] ex086: Crie uma classe MatematicaUtil com um método estático para calcular o fatorial de um número.
# • [ ] ex087: Crie uma classe ConstantesSistema contendo apenas atributos estáticos de leitura (como VERSAO = "1.0" e TIMEOUT = 30).
# • [ ] ex088: Crie uma exceção personalizada chamada SaldoInsuficienteException. Use-a na classe ContaBancaria quando um saque falhar.
# • [ ] ex089: Crie uma exceção personalizada chamada ValorInvalidoException que deve ser lançada se tentarem definir a idade de uma Pessoa como um número negativo.
# • [ ] ex090: Simule uma Interface Imprimivel com o método exibir_dados(). Faça com que a classe Contrato e a classe NotaFiscal implementem essa interface.
# • [ ] ex091: Crie uma classe GeradorId que possua um método estático para gerar uma string aleatória única combinando letras e números.
# • [ ] ex092: Crie uma classe Estoque que use um método estático para verificar se um código de barras simulado está no padrão correto de tamanho.
# • [ ] ex093: Crie uma classe CupomDesconto que valide estaticamente se a data de validade de um cupom ainda está ativa.
# • [ ] ex094: Simule uma Interface Voador com o método voar(). Aplique nas classes Passaro e Drone.
# • [ ] ex095: Crie uma classe Fatura que lance uma exceção customizada FaturaJaPagaException se tentarem pagar uma fatura cujo status já seja "paga".
# • [ ] ex096: Crie um método de classe que atue como um construtor alternativo (Factory), permitindo criar um objeto Usuario a partir de uma linha de texto CSV.
# • [ ] ex097: Crie uma classe Log com um método estático registrar_erro(mensagem) que exiba uma mensagem de erro formatada com a data atual simulada.
# • [ ] ex098: Crie uma classe CarroEletrico que herde de Carro e implemente uma Interface chamada Recarregavel.
# • [ ] ex099: Crie uma classe Alerta que possua métodos estáticos para emitir mensagens de aviso visuais no terminal (linhas de asteriscos).
# • [ ] ex100: Crie um mini-sistema de e-commerce associando objetos das classes Cliente, Pedido, ItemPedido e Produto, tratando exceções caso o estoque fique negativo.