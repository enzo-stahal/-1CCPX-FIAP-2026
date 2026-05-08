lista = []

while len(lista) < 5:
    numero = int(input("Digite um número: "))
    lista.append(numero)

    print(f"Lista Atual {lista}")

maior = max(lista)

print("O mairo número da lista é ", maior)