class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None


class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, dado):
        novo = No(dado)

        if self.raiz is None:
            self.raiz = novo
            print("Valor inserido!")
            return

        atual = self.raiz

        while True:
            if dado < atual.dado:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    print("Valor inserido!")
                    return
                atual = atual.esquerda

            elif dado > atual.dado:
                if atual.direita is None:
                    atual.direita = novo
                    print("Valor inserido!")
                    return
                atual = atual.direita

            else:
                print("Valor duplicado! Não foi inserido.")
                return

    def buscar(self, dado):
        atual = self.raiz

        while atual is not None:
            if dado == atual.dado:
                return True

            if dado < atual.dado:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return False

    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.dado, end=" ")
            self.em_ordem(no.direita)

    def minimo(self, no=None):
        atual = self.raiz if no is None else no

        if atual is None:
            return None

        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual.dado

    def maximo(self, no=None):
        atual = self.raiz if no is None else no

        if atual is None:
            return None

        while atual.direita is not None:
            atual = atual.direita

        return atual.dado

    def remover(self, no, dado):
        if no is None:
            return None

        if dado < no.dado:
            no.esquerda = self.remover(no.esquerda, dado)

        elif dado > no.dado:
            no.direita = self.remover(no.direita, dado)

        else:
            if no.esquerda is None:
                return no.direita

            if no.direita is None:
                return no.esquerda

            sucessor = no.direita

            while sucessor.esquerda is not None:
                sucessor = sucessor.esquerda

            no.dado = sucessor.dado

            no.direita = self.remover(
                no.direita, sucessor.dado
            )

        return no

    def excluir(self, dado):
        if not self.buscar(dado):
            print("Valor não encontrado!")
            return

        self.raiz = self.remover(self.raiz, dado)
        print("Valor removido!")


def mostrar_menu():
    print("\n===== GERENCIADOR BST =====")
    print("1 - Inserir valor")
    print("2 - Buscar valor")
    print("3 - Mostrar em ordem")
    print("4 - Mostrar menor valor")
    print("5 - Mostrar maior valor")
    print("6 - Remover valor")
    print("7 - Encerrar")


def executar_testes(arvore):
    valores = [
        61, 43, 77,
        16, 55, 69, 85,
        11, 31, 49, 59,
        65, 73, 81, 89
    ]

    print("\nInserindo os valores obrigatórios:")

    for valor in valores:
        arvore.inserir(valor)

    print("\n1. Valores em ordem:")
    arvore.em_ordem(arvore.raiz)
    print()

    print("\n2. Buscar 73:")
    print(arvore.buscar(73))

    print("\n3. Buscar 100:")
    print(arvore.buscar(100))

    print("\n4. Menor e maior valor:")
    print("Mínimo:", arvore.minimo())
    print("Máximo:", arvore.maximo())

    print("\n5. Remover 31 (folha):")
    arvore.excluir(31)

    print("\n6. Remover 16 (um filho):")
    arvore.excluir(16)

    print("\n7. Remover 77 (dois filhos):")
    arvore.excluir(77)

    print("\n8. Valores em ordem após as remoções:")
    arvore.em_ordem(arvore.raiz)
    print()



# PROGRAMA PRINCIPAL

arvore = BST()

while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            valor = int(input("Digite o valor para inserir: "))
            arvore.inserir(valor)
        except ValueError:
            print("Digite um número inteiro válido!")

    elif opcao == "2":
        try:
            valor = int(input("Digite o valor para buscar: "))

            if arvore.buscar(valor):
                print("Valor encontrado!")
            else:
                print("Valor não encontrado!")

        except ValueError:
            print("Digite um número inteiro válido!")

    elif opcao == "3":
        if arvore.raiz is None:
            print("A árvore está vazia.")
        else:
            print("Valores em ordem:")
            arvore.em_ordem(arvore.raiz)
            print()

    elif opcao == "4":
        resultado = arvore.minimo()

        if resultado is None:
            print("A árvore está vazia.")
        else:
            print("Menor valor:", resultado)

    elif opcao == "5":
        resultado = arvore.maximo()

        if resultado is None:
            print("A árvore está vazia.")
        else:
            print("Maior valor:", resultado)

    elif opcao == "6":
        try:
            valor = int(input("Digite o valor para remover: "))
            arvore.excluir(valor)
        except ValueError:
            print("Digite um número inteiro válido!")

    elif opcao == "7":
        print("Programa encerrado!")
        break

    elif opcao == "8":
        executar_testes(arvore)

    else:
        print("Opção inválida!")


# RESPOSTAS DAS QUESTÕES

# (a) O percurso em ordem produz valores ordenados porque
# visita primeiro a subárvore esquerda, depois o nó e,
# por último, a subárvore direita. Na BST, os menores
# valores ficam à esquerda e os maiores à direita.

# (b) O mínimo não precisa ser uma folha porque pode ter
# um filho à direita. Ele só não pode ter filho à esquerda.

# (c) O pior formato é uma árvore degenerada, parecida com
# uma lista encadeada. Isso pode acontecer ao inserir valores
# já ordenados em uma BST comum.

# (d) O mínimo da subárvore direita é utilizado porque é o
# menor valor maior que o nó removido. Ele pode substituí-lo
# mantendo a propriedade de ordenação da BST.
