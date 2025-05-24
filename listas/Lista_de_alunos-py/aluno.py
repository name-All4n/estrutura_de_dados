class aluno:
    def __init__(self, matricula, nota):
        self.matricula = matricula #Atributo para armazenar a matrícula
        self.nota = nota #Atributo para armazenar a nota
        self.proximo = None #Atributo para armazenar o próximo aluno na lista
