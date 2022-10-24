"Función que cuente cuantas veces se repite el patrón en una cadena de caracteres incluyendo si se superponen."
def cuenta_patron(cadena: str, patron:str):
    repeticiones= 0
    i=0
    
    while i<len(cadena) - len(patron) + 1:
        if cadena[i:i + len(patron)] == patron:
            repeticiones +=1
        i+=1
    return repeticiones

c = str(input('Ingrese una cadena: '))
p = str(input('Ingrese un patron que este en la cadena: '))

print(cuenta_patron(c, p), 'veces')







