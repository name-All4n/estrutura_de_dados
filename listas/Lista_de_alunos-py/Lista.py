from aluno import aluno # Importa a classe Item

class Lista:
    def __init__(self):
        self.inicio = None #Inicializa o início da lista como None
        self.ultimo = None #Inicializa o último da lista como None

    def adicionar_inicio(self, matricula, nota):
        #1-INSTANCIAR O NOVO ALUNO
        novo = aluno(matricula, nota) 
        #2-ATUALIZAR O PONTEIRO DO NOVO ALUNO
        novo.proximo = self.inicio 
        #3-ATUALIZAR O INÍCIO DA LISTA
        self.inicio = novo 
        if self.ultimo is None: 
            self.ultimo = novo 

    def adicionar_fim(self, matricula, nota):
        #1-INSTANCIAR O NOVO ALUNO
        novo = aluno(matricula, nota) 
        #2-ATUALIZAR O PONTEIRO DO ÚLTIMO ALUNO
        if self.ultimo is not None: 
            self.ultimo.proximo = novo 
        else: #lista vazia, nao tem ultimo
            self.inicio = novo 
            self.ultimo = novo 
        self.ultimo = novo #Atualiza o último aluno para o novo

    def mostrar_lista(self):
        atual = self.inicio 
        #1-VERIFICAR SE A LISTA ESTÁ VAZIA
        if atual is None: 
            print("LISTA VAZIA!") 
        #2-EXIBIR A LISTA
        while atual is not None: 
            print(f'matrícula: {atual.matricula}, nota: {atual.nota}') 
            atual = atual.proximo 

    def remover_inicio(self):
        #1-VERIFICAR SE A LISTA ESTÁ VAZIA
        if self.inicio is None:
            print("LISTA VAZIA!")
            return
        #2-ATUALIZAR O INÍCIO DA LISTA
        self.inicio = self.inicio.proximo
        #3-VERIFICAR SE A LISTA FICOU VAZIA
        if self.inicio is None:
            self.ultimo = None

    def remover_fim(self):
        #1-VERIFICAR SE A LISTA ESTÁ VAZIA
        if self.inicio is None:
            print("LISTA VAZIA!")
            return
        #2-VERIFICAR SE A LISTA TEM APENAS UM ALUNO
        if self.inicio == self.ultimo: 
            self.inicio = None
            self.ultimo = None
            return
        #3-ATUALIZAR O ÚLTIMO ALUNO
        atual = self.inicio
        while atual.proximo != self.ultimo: #Percorre a lista até o penúltimo aluno
            atual = atual.proximo
        atual.proximo = None #Atualiza o ponteiro do penúltimo aluno para None
        self.ultimo = atual

    def mostrar_nota(self, matricula):
        atual = self.inicio
        while atual is not None: #Percorre a lista
            if atual.matricula == matricula:
                print(f'A nota da matrícula: {atual.matricula} é {atual.nota}')
                return
            atual = atual.proximo #Se não encontrar a matrícula
        print("Matrícula não encontrada.")
