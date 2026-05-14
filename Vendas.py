Vendas = [
    ["Vendedor1", []],
    ["Vendedor2", []],
    ["Vendedor3", []]
]

while True:
    while True:
        print("DIA 1"
              "\nQuem Vendeu?"
              "\n1-Vendedor 1"
              "\n2-Vendedor 2"
              "\n3-Vendedor 3"
              "\n4-Fechar o dia")

        opcao = int(input("Opcao:"))

        if opcao == 1:
            Vendas[0][1].append(["Dia1", float(input("VALOR VENDA:"))])
        elif opcao == 2:
            Vendas[1][1].append(["Dia1", float(input("VALOR VENDA:"))])
        elif opcao == 3:
            Vendas[2][1].append(["Dia1", float(input("VALOR VENDA:"))])
        else:
            break

    while True:
        print("======================================="
            "\nDIA 2"
              "\nQuem Vendeu?"
              "\n1-Vendedor 1"
              "\n2-Vendedor 2"
              "\n3-Vendedor 3"
              "\n4-Fechar o dia")

        opcao = int(input("Opcao:"))

        if opcao == 1:
            Vendas[0][1].append(["Dia2", float(input("VALOR VENDA:"))])
        elif opcao == 2:
            Vendas[1][1].append(["Dia2", float(input("VALOR VENDA:"))])
        elif opcao == 3:
            Vendas[2][1].append(["Dia2", float(input("VALOR VENDA:"))])
        else:
            break

    while True:
        print("========================================"
            "\nDIA 3"
              "\nQuem Vendeu?"
              "\n1-Vendedor 1"
              "\n2-Vendedor 2"
              "\n3-Vendedor 3"
              "\n4-Fechar o dia")

        opcao = int(input("Opcao:"))

        if opcao == 1:
            Vendas[0][1].append(["Dia3", float(input("VALOR VENDA:"))])
        elif opcao == 2:
            Vendas[1][1].append(["Dia3", float(input("VALOR VENDA:"))])
        elif opcao == 3:
            Vendas[2][1].append(["Dia3", float(input("VALOR VENDA:"))])
        else:
            break

    terminar = input("==========================================="
        "\nReiniciar?(s/n):")

    if terminar == "n":
        if len(Vendas[0][1])+len(Vendas[1][1])+len(Vendas[2][1]) <= 0:
            print("SEM VENDAS!!")
            break
        else:
            for j in range(len(Vendas)):
                print(f"{Vendas[j][0]} - {Vendas[j][1]}")

            break
    else:
        Vendas[0].pop()
        Vendas[1].pop()
        Vendas[2].pop()
