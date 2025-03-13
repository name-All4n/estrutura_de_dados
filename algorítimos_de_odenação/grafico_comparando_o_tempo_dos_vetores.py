import matplotlib.pyplot as plt

#Dados de tempo de execução
tempos = {
    'Vetor Aleatório 1000': [0.0706, 0.0000, 0.0128],
    'Vetor Aleatório 10000': [4.8851, 0.0371, 0.0246],
    'Vetor Aleatório 100000': [512.8139, 0.2349, 0.3172]
}

algoritmos = ['Bubble Sort', 'Quick Sort', 'Merge Sort']

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.25
index = range(len(tempos))

for i, alg in enumerate(algoritmos):
    values = [t[i] for t in tempos.values()]
    bars = ax.bar([x + i * bar_width for x in index], values, bar_width, label=alg)
    
    # Adicionar valores no topo das barras
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., 1.05*height,
                f'{value:.4f}s', ha='center', va='bottom')

# Configurações adicionais
ax.set_yscale('log')  # Define a escala logarítmica no eixo Y
ax.set_xlabel('Caso de Teste')
ax.set_ylabel('Tempo (segundos) - Escala Logarítmica')
ax.set_title('Comparação de Desempenho entre Algoritmos de Ordenação')
ax.set_xticks([x + bar_width for x in index])
ax.set_xticklabels(tempos.keys())
ax.legend()

plt.tight_layout()
plt.show()