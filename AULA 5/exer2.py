
maior = None
menor = None
soma = 0


for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))
    
    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

media = soma / 10

print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média dos números: {media}")
