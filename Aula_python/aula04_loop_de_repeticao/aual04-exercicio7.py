n = int(input("Digite um número positivo: "))

while n <= 0:
    print("valor inválido!")
    n = int(input("Digite um número positivo: "))

soma = 0
for i in range(1, n + 1):
    soma += i

print("A soma dos números até", n, "é", soma)