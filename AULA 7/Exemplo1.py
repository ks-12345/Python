nota= 0
qnt_notas_info=0
while True:
    nota = float(input("Informe a nota(-1 para finalizar): "))
    if(nota==-1):
        break
    notas= nota + nota
    qnt_notas_info= qnt_notas_info +1
    if qnt_notas_info > 0:
     media = notas/qnt_notas_info
    print(f"Quntidade de notas informadas: {qnt_notas_info}")
    print(f"Media: {media: .2f}")
else:
 print("Nenhuma nota Informada")