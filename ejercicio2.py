cantidad_segundos=int(input("Ingrese una cantidad de segundos"))
print(f"Horas: {int(cantidad_segundos/3600) } ")
cantidad_segundos %= 3600
print (f"Minutos: {int(cantidad_segundos/60)}")
cantidad_segundos%=60
print(f"Segundos: {cantidad_segundos}")
