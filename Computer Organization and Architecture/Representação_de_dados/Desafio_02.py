mensagem = input("Digite uma mensagem: ")

for caractere in mensagem:
    codigo = ord(caractere)
    binario = format(codigo, "08b")

    print(caractere, "->", codigo, "->", binario)

quantidade_caracteres = len(mensagem)
quantidade_bytes = quantidade_caracteres
quantidade_bits = quantidade_bytes * 8

print("\nQuantidade de caracteres:", quantidade_caracteres)
print("Quantidade de bytes:", quantidade_bytes)
print("Quantidade de bits:", quantidade_bits)