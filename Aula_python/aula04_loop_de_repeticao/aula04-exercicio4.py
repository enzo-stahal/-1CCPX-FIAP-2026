from traceback import print_tb

lista = []

while len(lista) < 5:
    numero = int(input("Digite um número: "))
    lista.append(numero)

    print(f"Lista Atual {lista}")

soma = sum(lista)

print("Soma dos números", soma)



