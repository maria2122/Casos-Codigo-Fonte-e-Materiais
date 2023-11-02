from operacoes import Operacoes

valor = 100.00
porcentagem = 20
# Constroi o objeto da classe Operações
operacoes = Operacoes()
resultado = 0

# São 10 parcelas são fixas com 20% de desconto no valor fixo de 100.00
parcela = 10
while parcela > 0:
    resultado += operacoes.calcula_preco_com_desconto(valor, porcentagem)
    parcela-=1

print(resultado)