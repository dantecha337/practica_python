n=int(input("Ingrese un numero "))
for i in range(1, n+1):
    if i%5 == 0:
        continue
    print(i)