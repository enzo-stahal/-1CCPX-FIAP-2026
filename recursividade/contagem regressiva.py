def contagem1(n):
 while n > 0:
    print(n)
    n -= 1

print(contagem1(5))

def contagem2(n):
    print(n)
    contagem2(n - 1)

#print(contagem2(3))


def contagem3(n):
    if n == 0:
        return
    print(n)
    contagem3(n - 1)

print(contagem3(5))

