nomes = ["Ana", "Maria", "vini", "Mat"]

for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        print(nomes[j], nomes[i])
        print([i], [j])