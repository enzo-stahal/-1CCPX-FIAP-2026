def soma(n):
    if n == 0:
        return 0
    return n + soma(n - 1)


# soma(4) = 4 + soma(3)
#  = 4 + 3 + soma(2)
#  = 4 + 3 + 2 + soma(1)
#  = 4 + 3 + 2 + 1 + soma(0)
# soma(0) = 0
# Retorno:
# soma(1) = 1
# soma(2) = 3
# soma(3) = 6
# soma(4) = 10

print(soma(4))