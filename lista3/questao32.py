import sys

def pedido(n, qtd_caixas_4, qtd_caixas_6, qtd_caixas_9, qtd_caixas_20):
    if n == 0:
        print('PEDIDO ATENDIDO COM SUCESSO')
        print('QUANTIDADE DE CAIXAS DE 4 UNIDADES: %d' % qtd_caixas_4)
        print('QUANTIDADE DE CAIXAS DE 6 UNIDADES: %d' % qtd_caixas_6)
        print('QUANTIDADE DE CAIXAS DE 9 UNIDADES: %d' % qtd_caixas_9)
        print('QUANTIDADE DE CAIXAS DE 20 UNIDADES: %d' % qtd_caixas_20)
        sys.exit()
    elif n > 0:
        if (n - 20) >= 0:
            pedido(n - 20, qtd_caixas_4 , qtd_caixas_6, qtd_caixas_9, qtd_caixas_20 + 1)
        if (n - 9) >= 0:
            pedido(n - 9, qtd_caixas_4, qtd_caixas_6, qtd_caixas_9 + 1, qtd_caixas_20)
        if (n - 6) >= 0:
            pedido(n - 6, qtd_caixas_4, qtd_caixas_6 + 1, qtd_caixas_9, qtd_caixas_20)
        if (n - 4) >= 0:
            pedido(n - 4, qtd_caixas_4 + 1, qtd_caixas_6, qtd_caixas_9, qtd_caixas_20)      

n = int(input('Informe o numero de nuggets do pedido:'))
if not pedido(n, 0, 0, 0, 0):
    print('Pedido não pode ser atendido')