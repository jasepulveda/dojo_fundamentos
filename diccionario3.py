# Actualizar valores en diccionarios y listas

from zlib import decompressobj


def printInfo(some_dict):
    dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
    }
    largo = len(list(dojo[some_dict]))
    print(str(largo) + ' ' + some_dict.upper())
    #print([*dojo])
    for i in range(largo):
        print(dojo[some_dict][i])
    print('\n')


printInfo('locations')
printInfo('instructors')