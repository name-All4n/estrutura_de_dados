import time
import random
import matplotlib.pyplot as plt

#Implementação do Merge Sort
def merge_sort(vetor):
    if len(vetor) > 1:
        meio = len(vetor) // 2
        esquerda = vetor[:meio]
        direita = vetor[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1
    return vetor

#Casos de Teste
testes = {
    "Vetor Ordenado": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Vetor Quase Ordenado": [1, 2, 3, 4, 5, 6, 7, 9, 8, 10],
    "Vetor Inverso": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    "Vetor Vazio": [],
    "Vetor com Repetições": [5, 3, 5, 3, 5, 3, 5, 3, 5, 3],
    "Vetor Aleatório 1000": [random.randint(0, 1000) for _ in range(1000)],
    "Vetor Aleatório 10000": [random.randint(0, 10000) for _ in range(10000)],
    "Vetor Aleatório 100000": [random.randint(0, 100000) for _ in range(100000)]
}

#Main
tempos = []
nomes_testes = []

for nome, vetor in testes.items():
    inicio = time.time()
    resultado = merge_sort(vetor.copy())
    tempo = time.time() - inicio

    tempos.append(tempo)
    nomes_testes.append(nome)
    
    print(f"\n=== {nome} ===")
    print(f"Original: {vetor[:10]}...")  # Mostra apenas os 10 primeiros para vetores grandes
    print(f"Ordenado: {resultado[:10]}...")  # Mesmo para o resultado
    print(f"Tempo: {tempo:.4f} segundos")

#Criação do Gráfico 
plt.figure(figsize=(12, 7))
plt.bar(nomes_testes, tempos, color='lightgreen')
plt.title("Desempenho do Merge Sort")
plt.xlabel("Caso de Teste")
plt.ylabel("Tempo (segundos)")
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()

for i, v in enumerate(tempos):
    plt.text(i, v + 0.001, f"{v:.4f}s", ha='center')

plt.show()