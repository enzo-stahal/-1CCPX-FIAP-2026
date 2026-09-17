def resolver(problema):
    if caso_base:
        return resultado
    problema_menor = reduzir(problema)
    return resolver(problema_menor)

# DESCIDA:
# 3 → 2 → 1 → 0
# CASO-BASE
# RETORNO:
# 0 → 1 → 2 → 3
