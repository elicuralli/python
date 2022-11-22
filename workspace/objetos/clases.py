"""class Usuario:
    nombre="felipe"
    apellido="feliz"

usuario= Usuario() #esto es una instancia llamamos como si fuera una funcion

#print(usuario.nombre,usuario.apellido) #de esta forma se imprimen las propiedas de la clase
"""


class User:
 def __init__(self,nombre,apellido):
      self.nombre = nombre 
      self.apellido = apellido 

 def saludo(self): #se hace una referencia asi mismo
     print('hola, mi nombre es ', self.nombre,self.apellido)
 

usuario= User('felipe','feliz')
usuario2= User('maria','fernanda')

#usuario.saludo()
#usuario.nombre ='elibeth' #aqui se cambia el nombre de la instancia
#usuario.saludo() #se vuelve a imprimir con los nuevos cambios
#usuario2.saludo()
#del usuario.nombre (aqui se borra la propiedad de nombre mas no el objeto)
#del usuario (aqui si se borra el objeto usuario)
 
#self hace referencia a la instancia de la clase

'''herencia'''


class Admin(User):
    def superSaludo(self):
        print('hola me llamo',self.nombre, "soy el admin")


admin= Admin("elibeth","triste")
admin.saludo()
admin.superSaludo()