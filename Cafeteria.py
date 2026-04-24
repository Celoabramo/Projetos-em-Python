j = 0
p = 0
pt = 0
nome = input("Digite seu nome: ")
print("Olá,",nome)
def menu():
    print("1-café"
          "\n2-capuccino" 
          "\n3-chocolate"
          "\n4-terminar pedido")

    return escolha(1,4)

def escolha(n, m):
    valor = int(input("Digite sua opcao: "))
    if n<= valor <= m:
        return valor
    else:
        return 0
def tamanho():
    print("1-Pequeno"
          "\n2-Médio"
          "\n3-Grande")
    return escolha(1,3)

def terminar():
    v = pt
    f = input("Você é aluno FIAP?(sim/não):")
    if f == "sim" and v >= 20:
        v = pt * 0.90
        print("OLÁ FIAPINHO,""Você pediu", j, "itens,",
              "o seu pedido teve um desconto de 10% e ficou em um total de", v, "R$, Pedido com brinde!")
    elif f == "sim" and v <= 20:
        v = pt * 0.90
        print("OLÁ FIAPINHO,""Você pediu", j, "itens,", "o seu pedido teve um desconto de 10% e ficou em um total de",
              v, "R$, Pedido sem brinde")
    else:
        if v >= 20:
            print(nome, "Você pediu", j, "itens,", "o seu pedido ficou em um total de", v, "R$, Pedido com brinde!")
        else:
            print(nome, "Você pediu", j, "itens,", "o seu pedido ficou em um total de ", v, "R$, Pedido sem brinde")

while True:
    o = menu()

    if o == 0:
        print("opcao invalida!!!")

    elif o == 4:
        terminar()
        break

    else :
        t = tamanho()
        if o == 1:
            if t==1:
                p = 4
                print("café pequeno")
            elif t==2:
                p = 5.5
                print("café médio")
            elif t==3:
                p = 7
                print("café grande ")
        elif o == 2:
            if t==1:
                p = 6
                print("capuccino pequeno")
            if t ==2:
                p=7.5
                print("capuccino médio")
            if t ==3:
                p = 9
                print("capuccino grande ")
        elif o == 3:
            if t==1:
                p = 5.5
                print("chocolate pequeno")
            elif t==2:
                p = 7
                print("chocolate médio")
            elif t==3:
                p = 8.5
                print("chocolate grande ")

        if p > 0 and j >= 0:
            pt += p
            j += 1
            print ("Valor atual do pedido: ", pt,"R$"
                   "\nQuantidade de itens: ", j)

