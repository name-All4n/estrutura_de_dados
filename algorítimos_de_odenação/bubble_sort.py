import time
import random
import matplotlib.pyplot as plt 

#Implemnetação do Bubble Sort
def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        trocado = False
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                trocado = True
        if not trocado:
            break
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
    resultado = bubble_sort(vetor.copy())
    tempo = time.time() - inicio

    tempos.append(tempo)
    nomes_testes.append(nome)
    
    print(f"\n=== {nome} ===")
    print(f"Original: {vetor[:10]}...")  # Mostra apenas os 10 primeiros para vetores grandes
    print(f"Ordenado: {resultado[:10]}...")  # Mesmo para o resultado
    print(f"Tempo: {tempo:.4f} segundos")

#Criação do gráfico
plt.figure(figsize=(12, 7))
plt.bar(nomes_testes, tempos, color='skyblue')
plt.title("Desempenho do Bubble Sort")
plt.xlabel("Caso de Teste")
plt.ylabel("Tempo (segundos)")
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()

for i, v in enumerate(tempos):
    plt.text(i, v + 0.001, f"{v:.4f}s", ha='center')

plt.show()