from diciplina import Diciplina

class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.diciplinas = []
        self.notas_por_diciplina = {}

    def matricular(self, diciplina: Diciplina):
        self.diciplinas.append(diciplina)
        self.notas_por_diciplina.setdefault(diciplina.nome, [])

    def adicionar_nota(self, diciplina: Diciplina, nota: float):
        self.notas_por_diciplina[diciplina.nome].append(nota)

    def calcular_media_d(self, d: Diciplina) -> float:
        notas = self.notas_por_diciplina.get(d.nome, [])
        return sum(notas) / len(notas)
