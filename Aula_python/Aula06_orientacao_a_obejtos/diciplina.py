class Diciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_infos(self):
        print(f"Diciplina: {self.nome} | Professor: {self.professor}")





# Temporario
model_mat = Diciplina("Modelagem matematica", "igor")


