num1 = int(input("Digite o 1° Numero decimal: "))
num2 = int(input("Digite o 2° Numero decimal: "))

mais = int(input(f'Digite o resultado de {num1} + {num2}:'))
menos = int(input(f'Digite o resultado de {num1} - {num2}:'))
div = int(input(f'Digite o resultado de {num1} / {num2}:'))
vez = int(input(f'Digite o resultado de {num1} * {num2}:'))

remais= num1 + num2

remenos= num1 - num2

rediv= num1 / num2

revez= num1 * num2

if mais == remais:
    print("Soma correta")
else:
    print("Soma incorreta")

if menos == remenos:
    print("Subtração correta")
else:
    print("Subtração incorreta")    

if div == rediv:
    print("Divisao correta")
else:
    print("Divisao incorreta")  

if vez == revez:
    print("Multiplicação correta")
else:
    print("Multiplicação incorreta")  