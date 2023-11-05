from operacoes import Operacoes

valor = 100.00
porcentagem = 20
# Constroi o objeto da classe Operações
operacoes = Operacoes()
resultado = 0

# São 10 parcelas fixas com 20% de desconto fixo e valor variável de 100.00
parcela = 10
try :
    while parcela > 0:
        resultado += operacoes.calcula_preco_com_desconto(valor, porcentagem)
        parcela-=1
    print(resultado)
except Exception as e: 
    print(e)
