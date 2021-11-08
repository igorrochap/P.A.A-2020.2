def movimentar_hanoi(discos, torre_origem, torre_destino, torre_auxiliar_1, torre_auxiliar_2):
    movimentos = 1
    if discos == 0:
        return 0
    if discos == 1:
        print('Disco', discos ,'sai da torre', torre_origem, 'para a torre', torre_destino)
        return movimentos

    movimentos = 1 + (movimentos + movimentar_hanoi(discos-2, torre_origem, torre_auxiliar_1, torre_auxiliar_2, torre_destino))
    
    print('Disco', discos-1 ,'sai da torre', torre_origem, 'para a torre', torre_auxiliar_2)
    print('Disco', discos ,'sai da torre', torre_origem, 'para a torre', torre_destino)
    print('Disco', discos-1,'sai da torre', torre_auxiliar_2, 'para a torre', torre_destino)

    movimentos = 1 + (movimentos + movimentar_hanoi(discos - 2, torre_auxiliar_1, torre_destino, torre_origem, torre_auxiliar_2))

    return movimentos

movimentos = movimentar_hanoi(4, 'A', 'D', 'B', 'C')
print('Foram executados %d movimentos de disco' % movimentos)
#o algoritmo informará quais movimentos foram feitos e dirá que foram feitos 9 movimentos de disco