
val= float(input("Digite o valor da prestaçao: "))
tax = float(input("Digite a taxa: "))
tem = float(input("Digite o tempo(em meses): "))

pres = val + (val *(tax/100)* tem)

print(f"O valor da Prestaçao em atrazo è: {pres}")