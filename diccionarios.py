
# Actualizar valores en diccionarios y listas

def lista(l1,l2,v):
    print("\n\n== Ejercicio #1 =========\n")
    x = [ [5,2,3], [10,8,9] ]
    x [l1][l2] = v
    print(x)



def dict1(clave, lastname, valor):
    print("\n\n== Ejercicio #2 =========\n")
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
    ]
    students[clave][lastname] = valor 
    print(students[clave][lastname])

def dict2(clave, pos, valor):
    sports_directory = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer' : ['Messi', 'Ronaldo', 'Rooney']
    }
    sports_directory[clave][pos] = valor
    print(sports_directory['soccer'][0])
    
def dict3(dic, pos, valor):
    z = [ {'x': 10, 'y': 20} ]
    z[dic][pos] = valor
    print(z)

# Invocando las funciones
lista(1,0,15)
dict1(0,"last_name","Bryant")
dict2('soccer',0,'Andres')
dict3(0,'y',30)



