from Item import Item # Importa a classe Item

class Lista:
    def __init__(self):
        self.inicio = None
        self.ultimo = None

    def adicionar_inicio(self, valor):
        # 1-Instanciar elemento novo
        novo = Item(valor) #
        # 2-Atualizar ponteiro do proximo ao NOVO
        novo.proximo = self.inicio #
        # 3-Atualizar ponteiro do ANTERIOR ao inicio
        if self.inicio is not None:
            self.inicio.anterior = novo
        # 4-Atualizar ponteiro do proximo ao ANTERIOR do novo
        self.inicio = novo #
        if self.ultimo is None: #
            self.ultimo = novo #

    def adicionar_fim(self, valor):
        # 1-Instanciar elemento novo
        novo = Item(valor) #
        # 2-LOCALIZO O ULTIMO
        # nao e mais necessario, devido à otimização
        # já conhecemos o fim
        """
        Item ultimo = inicio;
        while(ultimo != null  &&  ultimo.proximo != null) {
            ultimo = ultimo.proximo;
        }
        """
        # 3-Atualizar ponteiro do proximo do ULTIMO para ser o novo
        if self.ultimo is not None: #
            self.ultimo.proximo = novo #
            novo.anterior = self.ultimo
        else: # lista vazia, nao tem ultimo
            self.inicio = novo #
        self.ultimo = novo # Atualiza o último para o novo elemento

    def mostrar_lista(self):
        atual = self.inicio #
        if atual is None: #
            print("LISTA VAZIA!") #

        while atual is not None: #
            print(atual.valor) #
            atual = atual.proximo #

    def mostrar_lista_reversa(self):
        atual = self.ultimo
        if atual is None:
            print("LISTA VAZIA!")
        while atual is not None:
            print(atual.valor)
            atual = atual.anterior

    def remover(self, valor):
        # 1-LOCALIZAR ALVO
        alvo = self.inicio #
        while alvo is not None and alvo.valor != valor: #
            alvo = alvo.proximo #
        # 2-REMOVER
        if alvo is not None: #
            # 3-se for o primeiro
            if alvo.anterior.proximo == alvo.proximo: #
                alvo.anterior.proximo = alvo.proximo #
            else: #
                self.inicio == alvo.proximo #
            # 4-se for o ultimo
            if alvo.proximo is not None:
                alvo.proximo.anterior = alvo.anterior
            else: 
                self.ultimo = alvo.anterior
