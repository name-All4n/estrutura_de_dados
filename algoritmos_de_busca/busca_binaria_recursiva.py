#função
def busca_bin_recursiva(numero, vetor, inicio=0, fim=None, comparacoes=0):
    if fim == None:
        fim = len(vetor) - 1

    if inicio > fim:
        print("NÃO ENCONTRADO")
        print(f"Quantidade de comparações realizadas: {comparacoes}")
        return
    
    meio = (inicio + fim) // 2
    comparacoes += 1

    if vetor[meio] == numero:
        print("ENCONTRADO")
        print(f"Quantidade de comparações realizadas: {comparacoes}")
    elif vetor[meio] > numero:
        busca_bin_recursiva(numero, vetor, inicio, meio-1, comparacoes)
    else:
        busca_bin_recursiva(numero, vetor, meio+1, fim, comparacoes)

#main
vetor1 = [14,21,5,45,12,3,86,98,46,53,24,2,1,15,90,47]
vetor2 = [1, 2, 3, 5, 12, 14, 15, 21, 24, 45, 46, 47, 53, 86, 90, 98]           

print("\nBusca por 14 em vetor1:")
busca_bin_recursiva(14, vetor1)
print("\nBusca por 14 em vetor2:")
busca_bin_recursiva(14, vetor2)

print("\nBusca por 46 em vetor1:")
busca_bin_recursiva(46, vetor1)
print("\nBusca por 46 em vetor2:")
busca_bin_recursiva(46, vetor2)

print("\nBusca por 90 em vetor1:")
busca_bin_recursiva(90, vetor1)
print("\nBusca por 90 em vetor2:")
busca_bin_recursiva(90, vetor2)

print("\nBusca por 50 em vetor1:")
busca_bin_recursiva(50, vetor1)
print("\nBusca por 50 em vetor2:")
busca_bin_recursiva(50, vetor2)

'''
os valores para o vetor2 foram encontrados em problemas, entretanto  para vetores desordenados, como vetor1, os resultados serão incorretos, pois a busca binária pressupõe que o vetor esteja ordenado.
'''