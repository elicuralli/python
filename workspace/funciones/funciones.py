def funcion():
    print('mi primera funcion')

#funcion()

def imprimeDato(argumentoUno):
    print('mi argumento es: ', argumentoUno)
#imprimeDato('parametro 1')


'''cuando se hace referencia a un valor es un argumento
pero, cuando se llama la funcion y se le da un valor es un parametro'''

def imprimeDato(nombre,apellido):
    print('su nombre completo es: ', nombre,apellido)
#imprimeDato('elibeth','curalli') 

#para poder recibiri mas de un argumento en la funcion se usa *

def imprimeDato(*nombre):
    print('su nombre completo es: ', nombre)
#imprimeDato('elibeth','curalli','leonela','jaimes')
#lo imprime como una tupla

#para imprimir un valor especifico de la tupla :

def imprimeDato(*nombre):
    print('su nombre completo es: ', nombre[0]) # me arroja el nombre que esta en esa posicion
#imprimeDato('elibeth','curalli','leonela','jaimes')


'''funciones con valor por defecto'''

def funcion2(argumento='elibeth'):
    print(argumento)
# como ya hay un valor por defecto en caso de que yo no asigne otro colocara ese
#funcion2()
#funcion2('maria')

def funcionlista(lista):
    for el in lista: #for elemento in lista 
        print(el)

#funcionlista(['chanchito','feliz'])

#RECURSIONN

def recursion(i):
    if (i<1):
        return i
    print(i)
    recursion(i-1)

    recursion(6)