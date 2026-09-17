while True:
    print("olá, Mundo!")

    resposta = input("Deseja exibir a mensagem novamente? (s/n): ")

    if resposta.lower() != "s":
        break

    print("Fim")