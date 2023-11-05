#Classe Operaçãoes contendo as operações básicas: 'desconto' e 'acréscimo'
class Operacoes:
    
    def calcula_preco_com_desconto(self, valor, porcentagem):
        if valor>= 0 and type(valor) == int or type(valor) == float:
            desconto = (valor * porcentagem) / 100
            return valor - desconto
        else:
            print("Entrada inválida, o valor deve ser maior ou igual a 0 e do tipo inteiro ou decimal!")
    
    
    def calcula_preco_com_acrescimo(self, valor, porcentagem):
        if valor>= 0 and type(valor) == int or type(valor) == float:
            acrescimo = (valor * porcentagem) / 100
            return valor + acrescimo
        else:
            print("Entrada inválida, o valor deve ser maior ou igual a 0 e do tipo inteiro ou decimal!")
