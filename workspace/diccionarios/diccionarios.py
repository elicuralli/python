# listas se definen con [ ]
#tuplas se definen con ( )
# diccionarios se definen con { }

diccionario= {
    "nombre":"dona",
    "raza":"poodle",
    "edad": 8
}
#print(diccionario)
#print(diccionario["raza"]) #eso se coloca para acceder a un valor especifico del diccionario 
#print(diccionario.get("nombre")) #este parametro realiza la misma funcion q el anterior es para obtener valores especificos

""" para cambiar los valores del diccionario"""

diccionario["nombre"]=  "luna" #lo que se encuentra a la derecha es el nuevo valor que se va a asignar 
# para eso se coloca [ ] y dentro la propiedad que se quiere cambiar 
diccionario["edad"]= 4
#print(diccionario)

#tambien podemos ver la cantidad de elementos q contiene
#print(len(diccionario)) # indica 3 pq son los elementos existentes

diccionario["ladra"]="si"

'''print(diccionario)'''
#diccionario.pop("ladra")# esto es para eliminar un valor especifico 
#diccionario.popitem() aqui elimina el ultimo valor del diccionario
# del diccionario["ladra"] de esta forma tambien se puede eliminar datos 

copia_diccionario=diccionario.copy()#para copiar se usa el .copy() o dict(diccionario)
del diccionario["ladra"]
#diccionario.clear() #para eliminar todos los datos que se tienen en un diccionario se usa .clear()
'''print(diccionario,copia_diccionario)'''



perros={
    "dona":{
     "nombre":"dona",
     "edad":8

    },
    "luna":{
        "nombre":"luna",
        'edad': 4
    },
    "mancha":{
        'nombre':'mancha',
        'edad':8

    }
}

#print(perros)
#print(perros['dona'])

''' crear diccionario con constructor dict'''

gatos= dict(nombre="coco",edad=3)
print(gatos)
