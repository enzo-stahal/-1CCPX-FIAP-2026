def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[-1]

    menores = []
    iguais = []
    maiores = []

    for elemento in lista:
        if elemento < pivo:
            menores.append(elemento)
        elif elemento == pivo:
            iguais.append(elemento)
        else:
            maiores.append(elemento)

    return (
        quick_sort(menores)
        + iguais
        + quick_sort(maiores)
    )


numeros = [6, 2, 8, 3, 5]

print(quick_sort(numeros))