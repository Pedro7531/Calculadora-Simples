def soma():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    print("Soma: ",x+y)

def subtracao():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    print("Subtracao: ",x-y)

def multiplicacao():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    print("Multiplicacao: ",x*y)

def divisao():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    if(y == 0):
        print("não é possível dividir por zero!")
    else:
        print("Divisao: ",x/y)

def divisao_inteira():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    if(y == 0):
        print("não é possível dividir por zero!")
    else:
        print("Divisao inteira: ",x//y)

def Modulo():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    print("Modulo(resto): ",x%y)

def exponenciacao():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    print("Exponenciação: ",x**y)

opcao=1

while opcao:
    print("")
    print("Selecione a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Divisão inteira")
    print("6. Modulo (resto)")
    print("7. Exponenciação")
    print("0. Sair")
    
    opcao = int(input("Informe o número da operação:"))

    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()
    if(opcao==5):
        divisao_inteira()
    if(opcao==6):
        Modulo() 
    if(opcao==7):
        exponenciacao()
    if(opcao==0):
        print("Obrigado por utilizar a calculadora!")           