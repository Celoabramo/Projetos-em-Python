j = 0
p = 0
pt = 0

def menu():
    print("1-café"
          "\n2-capuccino" 
          "\n3-chocolate"
          "\n4-Água"
          "\n5-Suco de laranja"
          "\n6-Pão de queijo"
          "\n7-terminar pedido")

    return escolha(1,7)

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
    f = input("Aluno FIAP?(s/n):")
    d = int(input("Desconto:"))
    if f == "s":
        v = pt * (0.90- d /100)
        print("total:",v,"R$"
                "\nQuantidade de itens: ", j,
                "\ndesconto de",d+10,"%" )

    else:
        v = pt *(d/ 100)
        print("total:", v, "R$"
            "\nQuantidade de itens: ", j,
              "\ndesconto de", d , "%")


while True:
    o = menu()

    if o == 0:
        print("opcao invalida!!!")

    elif o == 7:
        terminar()
        break


    else:
        if o == 1:
            t = tamanho()
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
            t = tamanho()
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
            t = tamanho()
            if t==1:
                p = 5.5
                print("chocolate pequeno")
            elif t==2:
                p = 7
                print("chocolate médio")
            elif t==3:
                p = 8.5
                print("chocolate grande ")
        elif o == 4:
            p = 5
            print("Água")
        elif o == 5:
            p = 9
            print("Suco de laranja")
        elif o == 6:
            p= 7
            print("Pão de queijo")



        if p > 0 and j >= 0:
            pt += p
            j += 1
            print ("Valor atual do pedido: ", pt,"R$"
                   "\nQuantidade de itens: ", j)
