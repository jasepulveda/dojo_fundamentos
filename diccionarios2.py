# Actualizar valores en diccionarios y listas

def iterateDictionary():
    students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]
    
    for i in students:
        #print(i.keys())
        print(i.get('first_name') + ' - ' + i.get('last_name'))
        #print(students[0]['first_name'],students[0]['last_name'])

def iterateDictionary2(par1):
    students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]
    print('\n\n')
    for i in students:
        #print(i.keys())
        print(i.get(par1))
        #print(students[0]['first_name'],students[0]['last_name'])

iterateDictionary() 
iterateDictionary2('first_name')
iterateDictionary2('last_name')
