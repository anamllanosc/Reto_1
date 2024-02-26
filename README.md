# Reto_1
###Punto 1 : 
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

def basic_operations (x:int, y:int, z:str):


    if z == "+":
        return (x+y)
    elif z== "-":
        return (x-y)
    elif z== "*":
        return (x*y)
    elif z== "/":
        if y!=0:
            return (x/y)
        else:
            print ("NO SE PUEDE DIVIDIR ENTRE 0")
    else: print ("EL OPERANDO NO ES VALIDO")
   
       
x=int(input("Ingrese el primer operando:"))
y=int(input("Ingrese el segundo operando:"))
z=str(input("¿Qué operación desea realizar?(+),(-),(*),(/):"))  


print (basic_operations('x', 'y', 'z'))
