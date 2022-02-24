
# Imprimiendo del 0 al 150
from curses.ascii import isdigit


print("\n\n== Ejercicio 1 =========")
for i in range(151):
    print(i)


# Imprimiendo del 0 al 150, con múltiplo de 5
print("\n\n== Ejercicio 2 =========")
for j in range(5,1001):
    if j % 5 == 0:
        print(j)


# Imprime los enteros de 1 a 100. Si el entero es divisible por 5, 
# imprime “Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
print("\n\n== Ejercicio 3 =========")
for k in range(1,10001):
    if  k % 5 == 0:
        print("Coding")
    elif  k % 5 == 5:
        print("Coding")
    elif k % 10 == 0:
        print("Coding Dojo")
    else:
        print(k)

# Agrega los enteros impares del 0 al 500,000, e imprime la suma final.
print("\n\n== Ejercicio 4 =========")
t = 0
for n in range(0,500001):
    k = (2 * n) - 1
    if k < 0:
        continue
    else:
        t = t + k
print("Suma total impares: ", t )

# Imprime números positivos comenzando desde el 2018, en cuanta regresiva de 4 en 4.
print("\n\n== Ejercicio 5 =========")
for n in range(2018,0, -4):
    print(n)

# Establece tres variables: lowNum, highNum, mult. Comenzando en lowNum 
# hasta highNum, imprime solo los enteros que sean múltiplos de mult. 
# Por ejemplo, si lowNum=2, highNum=9, y mult=3, el bucle debería 
# imprimir 3, 6, 9 (en líneas sucesivas).
print("\n\n== Opcional =========")
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,highNum + 1):
    if i % mult == 0:
        print(i)


