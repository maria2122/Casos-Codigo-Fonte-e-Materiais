# impotação da biblioteca 'unittest' que possibilita o teste de unidade
import unittest
# impotação da classe a ser testada
from operacoes import Operacoes

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


