logon=[["marcelo","najjar"]]

def validar(nom,sen):
    val = 0
    for i in logon:
        if nom == i[0] and sen == i[1]:
            val +=1
        else:
            continue
    return val 



while True:
        print("1-Entrar", "\n2-Cadastrar", "\n3-Sair")
        op = int(input("Opcção"))

        if op == 1:
            nome = str(input("digite o seu nome: "))
            senha = str(input("digite sua senha: "))
            if validar(nome,senha) >= 1 :
                print("Olá ", nome)
            elif validar(nome,senha) ==0:
                print("Usário e/ou senha incorreto!")



        elif op == 2:
            nome = str(input("digite o seu nome: "))
            senha = str(input("digite sua senha: "))
            logon.append([nome,senha])

        else:
            print("Obrigado:)")
            break

