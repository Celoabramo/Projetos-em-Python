agenda = []

def menu():
    print("1-Adicionar novo contato" \
    "\n2-Editar contato" \
    "\n3-Pesquisar contato" \
    "\n4-Lista de contatos" \
    "\n5-Apagar um contato" \
    "\n6-Sair")
    return validar("Escolha uma opção: ", 1, 6)

def validar(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input())
            if inicio <= valor <= fim:
                return (valor)
            else:
                return(0)
        except ValueError :
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def listar_dados(nome, celular, email): 
        print("Nome: %s " \
        "\nCelular: %s" \
        "\ne-mail: %s" % (nome, celular, email ))
        print ("----------------------------------------")


def listar():
    print(" CONTATOS DA AGENDA ")
    for e in agenda :
        listar_dados(e[0], e[1], e[2])
    print("FIM DA AGENDA")

          

def novo():
    global agenda
    nome = p_nome()
    celular = input("Celular...:")
    email = input("e-mail...:")
    agenda.append([nome, celular, email])
    print("\n----------------------------------" \
    "\nRegistro Adicionado com sucesso!" \
    "\n----------------------------------")

def pesquisar():
    p = pesquisa(p_nome())
    if p != None:
        print("Registro encontrado!")
        nome = agenda [p][0]
        celular = agenda [p][1]
        email = agenda [p][2]
        listar_dados(nome, celular, email)
    else:
        print("\nNão encontrado!!!")

def apagar():
    global agenda 
    nome = p_nome()
    p = pesquisa(nome)
    if p != None:
        del agenda [p]
        print("\n----------------------------------" \
    "\nRegistro Apagado com sucesso!" \
    "\n----------------------------------")
    else:
        print("Nome não encontrado")

def p_nome():
    return(input("Nome...:"))

def pesquisa(nome):
    name = nome.lower()
    for d, e in enumerate(agenda):
        if e[0].lower() == name:
            return d 
    return None

def editar():
    p = pesquisa(p_nome())
    if p != None:
        nome = agenda[p][0]
        print("Nome...:", nome)
        celular = input("Celular...:")
        email = input("e-mail...:")
        agenda[p] = [nome, celular, email]
        print("\n----------------------------------"
              "Contato Editado com Sucesso!" \
              "\n----------------------------------")

while True: 
    opcao = menu()
    if opcao == 0:
        print("Opcao invalida!")
    elif opcao == 6:
        print(
            "-------------------------------" "\nOBRIGADO POR USAR MINHA AGENDA!!!"
            "\n-------------------------------")
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        apagar()

