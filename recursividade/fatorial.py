# matematicamente: n! = n × (n − 1)! e 0! = 1

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print(fatorial(4))

