temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

maior_risco = 0
sala_maior_risco = 0
numero_sala = 1

for sala in temperaturas:
    soma = 0
    contador = 0

    for valor in sala:
        soma += valor

        if valor >= 33:
            contador += 1

    media = soma / 4

    print("Sala", numero_sala)
    print("Média:", media)
    print("Registros críticos:", contador)
    print()

    if contador > maior_risco:
        maior_risco = contador
        sala_maior_risco = numero_sala

    numero_sala += 1

print("Sala com maior risco: Sala", sala_maior_risco)