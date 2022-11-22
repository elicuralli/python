
#edadEli= input('elibeth introduce tu edad: ')
#edadEli= int(edadEli)

#edadOri= input('oriana introduce tu edad: ')
#edadOri= int(edadOri)

'''if(edadEli>edadOri):
    print("elibeth es la mayor tiene " + str(edadEli)+" años"),
    print('oriana es la menor tiene '+str(edadOri)+ " años")

elif(edadOri>edadEli):
    print('oriana es la mayor tiene '+str(edadOri)+ " años"),
    print("elibeth es la menoor tiene " + str(edadEli)+" años"),

elif(edadEli==edadOri):
    print("elbeth y oriana tienen la misma edad")
'''

#ejercicio, con una lista y comprobar que el dato que ingreso el usuario esta en la lista

#dato= input('por favor ingrese una parte del cuerpo humano: ')
#lista=['cabeza','manos','pies', 'piernas','cerebro','brazos']

'''if lista.count(dato)>0: #aqui se pregunta si nuestra lista contiene alguno de esos elementos q ingreso el usuario 
 print('el dato ingresado ya esta registrado') # con el >0 interpretamos que tenemos mas de un solo elemento y se puede interpretar como q el dato existe 
 
else:
 print('el dato ingresado no esta registrado: ',dato)

'''

 #calculadora de suma

num1= input('ingrese un numero: ')

try:
    num1=int(num1)

except: 
    num1='dato erroneo'
if num1=='dato erroneo':
    print('solo se admiten datos numericos')
    exit()
num2= input('ingrese otro numero: ')

try: 
    num2= int(num2)
except:
    num2='dato erroneo'
 

if num2=='dato erroneo':
    print('solo se admiten datos numericos')
    exit()

operacion= input('ingrese la operacion(+,-,*,/): ')

if operacion=='+':
    print('su suma es: ',num1+num2)

elif operacion=='-':
     print('su resta es: ',num1-num2)

elif operacion=='*':
     print('su multiplicacion es: ',num1*num2)

elif operacion=='/':
     print('su division es: ',num1/num2)

else:
    print('el simbolo ingresado no es valido')

