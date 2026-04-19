#EJ 5
def romanos(cadena: str) -> int:
    valores = {'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000}

    if cadena == '': #si no hay letras, devuelve 0
        return 0
    if len(cadena) == 1:
        return valores[cadena]
    # si el valor actual es menor al que sigue, se resta
    if valores[cadena[0]] < valores[cadena[1]]:
        return -valores[cadena[0]] + romanos(cadena[1:])
    else:
        # si es mayor o igual, se suma 
        return valores[cadena[0]] + romanos(cadena[1:])


print(romanos("VVI"))    
print(romanos("XIV"))   
print(romanos("C"))

#EJ 22
def usar_la_fuerza(mochila: list) -> tuple:
    if not mochila: #si no hay nada en la mochila, y sacamos 0 objetos en esta llamaada
       return False, 0 
    objeto = mochila[0] #saca el primer objeto
    
    if objeto == 'sable de luz':
       return True, 1 #se encontro y se cuenta el objeto
    
    encontrado, contador_resto = usar_la_fuerza(mochila[1:])
    if encontrado:            #si se encontro mas adelante, se suma 1 por el objeto q sacamos
     return True, 1 + contador_resto
    else: #si no está en el resto, retornamos que no se encontró
        return False, contador_resto

mochila_mace_windu = ["raciones", "comunicador", "sable de luz"]
hallado, total_sacados = usar_la_fuerza(mochila_mace_windu)
if hallado:
    print(f"Mace Windu recuperó su sable! Sacó {total_sacados} objetos en total")
else:
    print("La mochila no contenía un sable de luz")
