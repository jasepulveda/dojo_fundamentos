#Cuenta regresiva 
print("\n\n== Ejercicio #1 Cuenta Regresiva =========\n")
def cta_regresiva(n):
    lista = []
    for i in range(n,-1, -1):
        lista.append(i)
    print(lista)

cta_regresiva(5)

# Print y return
print("\n\n== Ejercicio #2 Print y Return =========\n")
def print_and_return(lista):
    print(lista[0])
    return lista[1]


print_and_return([1,2])

# Primero más longitud
print("\n\n== Ejercicio #3 Primero más longitud (no imprime nada) =========\n")
def first_plus_length(lista):
    sum = lista[0] + len(lista)
    return sum

first_plus_length([1,2,3,4,5])

# Esta longitud, ese valor
print("\n\n== Ejercicio #4 Esta longitud, ese valor =========\n")
def length_and_value(a,b):
    lista = []
    for k in range(a):
        lista.append(b)

    print(lista)

length_and_value(4,7)
length_and_value(6,2)
