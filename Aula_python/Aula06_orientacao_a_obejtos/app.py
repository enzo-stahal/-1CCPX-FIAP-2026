from aluno import Aluno
from diciplina import Diciplina

# Criar / instanciar 1 aluno
aluno1 = Aluno("João", "123456", "Cinência da Computação")

# Criar / instanciar 2 diciplinas
dsa = Diciplina("Data Strucutres", "Álvaro")
model_lin = Diciplina("Modelagem Linear", "Rodolfo")

# Matricula o aluno nas diciplinas
aluno1.matricular(dsa)
aluno1.matricular(model_lin)
# print(aluno1.diciplinas[0].professor)
# print(aluno1.diciplinas[1].professor)

# Adicionar notas do aluno referente as diciplinas
aluno1.adicionar_nota(dsa, 10)
aluno1.adicionar_nota(dsa, 8)
aluno1.adicionar_nota(model_lin, 5)
aluno1.adicionar_nota(model_lin, 3)
# print(aluno1.notas_por_diciplina)

print(aluno1.calcular_media_d(dsa))