texto = "CASA"

for letra in texto:
    codigo_01 = ord(letra)

    print(
        letra,
        "->",
        codigo_01,
        "->",
        "{:08b}".format(codigo_01)
    )