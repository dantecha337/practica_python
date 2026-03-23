lista=[]
while True:
    palabra=input("Ingresa una palabra o . para finalizar")
    if palabra == ".":
        break
    if len(palabra) > 3:
        lista.append(palabra)
print(" ".join(lista))
