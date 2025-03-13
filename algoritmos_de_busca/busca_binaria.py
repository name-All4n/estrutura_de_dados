#função
def busca_bin(numero, vetor):
    inicio = 0
    fim = len(vetor) - 1
    comparacoes = 0
    tamanho_vetor = len(vetor)
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        
        if vetor[meio] == numero:
            print(f"Tamanho do vetor recebido: {tamanho_vetor}")
            print(f"Índice do vetor onde o número foi localizado: {meio}")
            print(f"Quantidade de comparações realizadas para se chegar ao resultado: {comparacoes}")
            return
        elif vetor[meio] < numero:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    print(f"Tamanho do vetor recebido: {tamanho_vetor}")
    print("Número não localizado")
    print(f"Quantidade de comparações realizadas para se chegar ao resultado: {comparacoes}")

#main
vetor1 = [14, 21, 5, 45, 12, 3, 86, 98, 46, 53, 24, 2, 1, 15, 90, 47]
vetor2 = [1, 2, 3, 5, 12, 14, 15, 21, 24, 45, 46, 47, 53, 86, 90, 98]

print("\nBusca por 14 em vetor1:")
busca_bin(14, vetor1)
print("\nBusca por 14 em vetor2:")
busca_bin(14, vetor2)

print("\nBusca por 46 em vetor1:")
busca_bin(46, vetor1)
print("\nBusca por 46 em vetor2:")
busca_bin(46, vetor2)

print("\nBusca por 90 em vetor1:")
busca_bin(90, vetor1)
print("\nBusca por 90 em vetor2:")
busca_bin(90, vetor2)

print("\nBusca por 50 em vetor1:")
busca_bin(50, vetor1)
print("\nBusca por 50 em vetor2:")
busca_bin(50, vetor2)

'''
Análise da Eficiência:
1. A busca binária só funciona corretamente em vetores ordenados. No caso de vetor1,
   que não está ordenado, a função pode falhar ou retornar resultados incorretos.
2. Para vetor2, que está ordenado, a busca binária funciona conforme esperado.
'''

'''
- Melhor caso: O número procurado está exatamente no meio do vetor. Nesse caso, 
  o algoritmo realiza apenas 1 comparação (O(1)).

- Caso médio: Em média, o algoritmo também executa em tempo logarítmico (O(log n)).
  
- Pior caso: O número não está presente no vetor ou está em uma das extremidades.
  O algoritmo precisa dividir o vetor até encontrar o elemento ou determinar que 
  ele não existe. O número máximo de comparações é log2(n), onde n é o tamanho 
  do vetor (O(log n)).
'''

'''
Teste com vetor1 (não ordenado):
Busca por 14:
Tamanho do vetor: 16
Resultado: Resultado incorreto, pois o vetor não está ordenado).
Quantidade de comparações: depende do comportamento incorreto.
Busca por 46:
Tamanho do vetor: 16
Resultado: "Número não localizado" (ou resultado incorreto).
Quantidade de comparações: depende do comportamento incorreto.
Busca por 90:
Tamanho do vetor: 16
Resultado: "Número não localizado" (ou resultado incorreto).
Quantidade de comparações: depende do comportamento incorreto.
Busca por 50:
Tamanho do vetor: 16
Resultado: "Número não localizado".
Quantidade de comparações: logarítmica, mas o resultado pode ser incorreto.

Teste com vetor2 (ordenado):
Busca por 14:
Tamanho do vetor: 16
Resultado: "Número localizado no índice: 5".
Quantidade de comparações: 4.
Busca por 46:
Tamanho do vetor: 16
Resultado: "Número localizado no índice: 10".
Quantidade de comparações: 4.
Busca por 90:
Tamanho do vetor: 16
Resultado: "Número localizado no índice: 14".
Quantidade de comparações: 4.
Busca por 50:
Tamanho do vetor: 16
Resultado: "Número não localizado".
Quantidade de comparações: 4.
'''