num1 = float(input("numero 1: "))
print("OPERAÇÕES(+,-,*,/,ac)")

while True:
    op = input("Operação: ")
    while op=="ac":
        num1=0
        num1 = float(input("numero 1: "))
        op = input("Operação: ")


    num2 = float(input("Numero 2: "))

    if op=="+":
        num1+=num2
        print("resultado: ",num1)
    elif op=="-":
        num1-=num2
        print("resultado: ",num1)
    elif op=="*":
        num1*=num2
        print("resultado: ",num1)
    elif op=="/":
        num1/=num2
        print("resultado: ",num1)
    
        
