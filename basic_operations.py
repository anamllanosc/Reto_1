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