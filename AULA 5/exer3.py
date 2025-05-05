temp=int(input("Digite a temp: "))

if temp < 37.2:
    print("Temperatura normal.")
elif 37.2 <= temp < 38.0:
    print("Estado febril.")
elif 38.0 <= temp < 39.0:
    print("Febre.")
else:
    print("Febre alta.")
        