from test import *
# impotação da biblioteca 'unittest' que possibilita o teste de unidade
import unittest

#Classe Operaçãoes contendo as operações básicas: 'desconto' e 'acréscimo'
class Operacoes:

    def calcula_preco_com_desconto(self, valor, porcentagem):
        desconto = (valor * porcentagem) / 100
        return valor + desconto
    
    def calcula_preco_com_acrescimo(self, valor, porcentagem):
        acrescimo = (valor * porcentagem) / 100
        return valor + acrescimo
    
# Classe de teste que herda de unittest.TestCase
class TestCalculaDesconto(unittest.TestCase):
    def test_calcula_preco_com_desconto(self):
        valor = 100
        porcentagem = 20
        operacoes = Operacoes()
        resultado = operacoes.calcula_preco_com_desconto(valor, porcentagem)
        
        # função que valida se a saída real é igual a saída esperada 
        self.assertEqual(resultado, 80, 'FALHA: retorno do método não é compatível com a saída esperada!')

#chamada da main(função principal onde é iniciada a execução do teste)
if __name__ == '__main__':
    unittest.main()


