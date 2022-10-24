"Función que calcule el valor factorial de un número entero positivo."
def factorial(n):
    print('Valor Inicial= ', n)
    if n>1:
        n= n*factorial(n-1)

    return n

n= int(input('Ingrese un numero: '))

f= factorial(n)  
print(f'Su factorial de {n} es: {f} ') 

