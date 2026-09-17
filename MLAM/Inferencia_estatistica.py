from math import sqrt
from scipy.stats import norm

# Encontre o Zc:
print("Zc = ", ((55-53)-(0)) / sqrt( (7.5/5)+ (5/5)))


# Encontrar o Za/2
print("Za/2 = ", norm.ppf(0.05/2))
