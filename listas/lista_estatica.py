class ListaEstatica:
    def __init__ (self, tamanho):
        self.tamanho = tamanho
        self.lista = []

    def inserir_inicio(self, nome, nota):
        if len(self.lista) == self.tamanho:
            print("lista cheia")
        else: 
            self.lista.insert(0, {'nome':nome, 'nota':nota})

    def inserir_final(self, nome, nota):
        if len(self.lista) == self.tamanho:
            print("lista cheia")
        else:
            self.lista.append({'nome':nome, 'nota':nota})

    def imprimir(self):
        if len(self.lista) > 0:
            print(self.lista)
        elif len(self.lista) == 0:
            print("lista vazia: []")

    def buscar(self, nome):
        for elemento in self.lista:
            if elemento['nome'] == nome:
                print(f"Elemento encontrado: Nome: {elemento['nome']}, Nota: {elemento['nota']}")
                return
        print("o estudante não pertence a lista")

    def retirar(self, nome):
        for i, elemento in enumerate(self.lista):
            if elemento['nome'] == nome:
                del self.lista[i]
    def esvaziar(self):
        self.lista.clear()

lista = ListaEstatica(4)

lista.inserir_inicio('João', 10)
lista.inserir_final('Maria', 8)
lista.inserir_inicio('Pedro', 7)
lista.imprimir()
lista.buscar('João')
lista.retirar('Pedro')
lista.imprimir()
lista.esvaziar()
lista.imprimir()
    