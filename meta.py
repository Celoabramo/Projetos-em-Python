meta = float(input("Meta:"))
vt = 0

while True:
    valor = float(input("Valor do pedido:"))
    vt += valor
    if vt < meta:
        print("valor do pedido:", valor,
            "\nvalor total:", vt,
              "\nMeta:", meta
              ,"\nMeta não atingida")
    elif vt >= meta:
        print("valor do pedido:", valor,
            "\nvalor total:",vt,
              "\nMeta:", meta
              ,"\nMeta atingida")

    terminar = input("terminar(s/n)")
    if terminar == "s":
        if vt < meta:
            print("valor total:", vt,
                  "\nMeta:", meta
                  , "\nMeta não atingida")
        elif vt > meta:
            print("valor total:", vt,
                  "\nMeta:", meta
                  , "\nMeta atingida")
        break
    else:
        continue