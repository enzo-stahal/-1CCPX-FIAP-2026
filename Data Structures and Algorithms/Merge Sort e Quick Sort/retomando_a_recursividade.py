def contagem(n):
    if n == 0:
        return

    print(n)
    contagem(n - 2)

contagem(6)

def dividir(n):
    if n <= 1:
        return
    print(n)
    dividir(n // 2)


dividir(32)