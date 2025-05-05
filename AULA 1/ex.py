nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media= (nota1 + nota2) / 2

if media  >= 6.0:
    print(f"Sua media foi {media:.1f}). Resultado: APROVADO!")
    
elif media  >= 4.0:
    print(f"Sua media foi {media:.1f}). Resultado: Reprovado!")

else:
    print(f"Sua media foi {media:.1f}). Resultado: Recuperaçao!")