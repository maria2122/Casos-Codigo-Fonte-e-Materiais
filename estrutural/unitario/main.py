from operacoes import Operacoes

valor = 100
porcentagem = 20
operacoes = Operacoes()
resultado = operacoes.calcula_preco_com_desconto(valor, porcentagem)
i = 10
while i > 0:
    i-=1
    resultado += operacoes.calcula_preco_com_desconto(valor, porcentagem)

print(resultado)