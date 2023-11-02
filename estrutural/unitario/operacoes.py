#Classe Operaçãoes contendo as operações básicas: 'desconto' e 'acréscimo'
class Operacoes:
    
    def calcula_preco_com_desconto(self, valor, porcentagem):
        desconto = (valor * porcentagem) / 100
        return valor - desconto
    
    def calcula_preco_com_acrescimo(self, valor, porcentagem):
        acrescimo = (valor * porcentagem) / 100
        return valor + acrescimo
    
