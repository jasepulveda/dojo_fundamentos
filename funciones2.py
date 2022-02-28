# Tamaño grande
print("\n\n== Ejercicio #1 Tamaño grande =========\n")
def biggie_sizie(lista):
    con = 0
    for i in lista:
        if i >= 0:
            lista[con] = "big"
        con = con + 1
    print(lista)

biggie_sizie([-1,3,5,-5])

# Contar positivo
print("\n\n== Ejercicio #2 Contar positivo =========\n")
def count_positives(lista):
    con = 0
    lon = len(lista)
    for i in range(lon - 1):
        if lista[i] > 0:
            con = con + 1
    lista[lon - 1] = con
    print(lista)

count_positives([-1,1,1,1,1])
count_positives([1,6,-4,-2,-7,-2])

# Suma total 
print("\n\n== Ejercicio #3 Suma total  =========\n")
def sum_total(lista):
    sum = 0
    for i in range(len(lista)):
        sum = sum + lista[i]
    print(sum)

sum_total([1,2,3,4])
sum_total([6,3,-2])

# Suma total 2
print("\n\n== Ejercicio #4 Suma total  =========\n")
def average(lista):
    sum = 0
    for i in range(len(lista)):
        sum = sum + lista[i]
    avg = sum / len(lista)
    print(avg)

average([1,2,3,4])

# Longitud
print("\n\n== Ejercicio #5 Longitud  =========\n")
def length(lista):
    return len(lista)

print(length([37,2,1,-9]))
print(length([]))

# Mínimo
print("\n\n== Ejercicio #6 Mínimo  =========\n")
def minimum(lista):
    if len(lista) != 0:
        menor = lista[0]
        for k in lista:
            if k < menor: 
                menor = k
    else:
        menor = False
    print(menor)


minimum([37,2,1,-9])
minimum([])