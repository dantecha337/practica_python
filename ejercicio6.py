n=int(input("Ingrese un numero "))
multiplos=[]
otros=[]
for i in range(1, n+1):
    if i%5 == 0:
        multiplos.append(i)
        continue
    otros.append(i)
print (f"multiplos de 5: {multiplos}")
print(f"otros: {otros}")