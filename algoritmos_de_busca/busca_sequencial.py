#função
def busca_seq(numero, vetor):
    tamanho_vetor = len(vetor)
    comparacoes = 0

    for i in range(tamanho_vetor):
        comparacoes += 1
        if vetor[i] == numero:
            print(f"Tamanho do vetor recebido: {tamanho_vetor}")
            print(f"índice do vetor onde o número foi localizado: {i}")
            print(f"quantidade de comparações realizadas para se chegar ao resultado: {comparacoes}")
    if numero not in vetor:
        print(f"Tamanho do vetor recebido: {tamanho_vetor}")
        print(f"Número não localizado")
        print(f"quantidade de comparações realizadas para se chegar ao resultado: {comparacoes}")

#main
vetor1 = [14, 21, 5, 45, 12, 3, 86, 98, 46, 53, 24, 2, 1, 15, 90, 47]
vetor2 = [1, 2, 3, 5, 12, 14, 15, 21, 24, 45, 46, 47, 53, 86, 90, 98]

print("\nBusca por 14 em vetor1:")
busca_seq(14, vetor1)
print("\nBusca por 14 em vetor2:")
busca_seq(14, vetor2)

print("\nBusca por 46 em vetor1:")
busca_seq(46, vetor1)
print("\nBusca por 46 em vetor2:")
busca_seq(46, vetor2)

print("\nBusca por 90 em vetor1:")
busca_seq(90, vetor1)
print("\nBusca por 90 em vetor2:")
busca_seq(90, vetor2)

print("\nBusca por 50 em vetor1:")
busca_seq(50, vetor1)
print("\nBusca por 50 em vetor2:")
busca_seq(50, vetor2)

'''
Resultados:
Busca por 14:
Vetor 1 : Localizado no índice 0 com 1 comparação.
Vetor 2 : Localizado no índice 5 com 6 comparações.

Busca por 46:
Vetor 1 : Localizado no índice 8 com 9 comparações.
Vetor 2 : Localizado no índice 10 com 11 comparações.

Busca por 90:
Vetor 1 : Localizado no índice 14 com 15 comparações.
Vetor 2 : Localizado no índice 14 com 15 comparações.

Busca por 50:
Vetor 1 : Não localizado com 16 comparações.
Vetor 2 : Não localizado com 16 comparações.
'''


'''
Análise da Eficiência:

Melhor caso :
Ocorre quando o número procurado está na primeira posição do vetor.
Exemplo: A busca por 14 no vetor1 resultou em apenas 1 comparação.

Caso médio :
Ocorre quando o número procurado está em uma posição intermediária do vetor.
Exemplo: A busca por 46 no vetor1 resultou em 9 comparações.

Pior caso :
Ocorre quando o número procurado está na última posição do vetor ou não está presente.
Exemplo: A busca por 50 no vetor1 e vetor2 resultou em 16 comparações.
'''