class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.ultimo = None

    def adicionar_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.inicio
        self.inicio = novo
        if self.ultimo is None:
            self.ultimo = novo

    def adicionar_fim(self, valor):
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
            self.ultimo = novo
        else:
            self.ultimo.proximo = novo
            self.ultimo = novo

    def mostrar(self):
        atual = self.inicio
        if atual is None:
            print("Lista vazia!")
            return
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

    def remover(self, valor):
        atual = self.inicio
        anterior = None

        while atual and atual.valor != valor:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            print(f"Valor {valor} não encontrado.")
            return

        if anterior is None:
            self.inicio = atual.proximo
            if self.inicio is None:
                self.ultimo = None
        else:
            anterior.proximo = atual.proximo
            if anterior.proximo is None:
                self.ultimo = anterior

    def buscar(self, valor):
        atual = self.inicio
        while atual:
            if atual.valor == valor:
                print(f"Valor {valor} encontrado na lista.")
                return True
            atual = atual.proximo
        print(f"Valor {valor} não encontrado na lista.")
        return False
