def exemplo(n):
    if n == 0:
        return
    print("Entrando:", n)
    exemplo(n - 1)
    print("Saindo:", n)
exemplo(3)
