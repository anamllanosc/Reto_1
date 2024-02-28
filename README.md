# Reto_1
## Punto 1:
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

```
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
```
### Explicación:
- Se definió la función "basic_operations", que toma como parametros X, Y y Z, en donde X y Y corresponden a los numeros los cuales se van a operar, y Z a el signo que define la operacion que se realizara.
- +:suma, -:resta, *:multiplicacion y /:division.
- Con un "if" anidado a el "elif" correspondiente a la division, se asegura que no llegue a ocurrir una division por 0.
- Si a Z, se le asigna un caracter diferente de +,-,* o /, se dira que el operando no es valido.
## Punto 2:
Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original
```
def palindrome (word: str):
    reversed_word=""

    for letter in word:
        reversed_word = letter + reversed_word


    if reversed_word==word:
        print ("La palabra ingresada es un palindromo ")
    else:
        print ("La palabra ingresada no es un palindromo ")


word=str(input("¿Qué palabra desea que se verifique?"))
palindrome (word)
```
### Explicación:
- Se definio la funcion "palindrome" en donde se toma como parametro la variable "word", que corresponde a la palabra que el usuario ingresa por teclado. En esta funcion se desea verificar si la palabra escrita en sentido contrario sigue siendo ella misma, como por ejemplo : rallar.
- Se crea la cadena vacia "reversed_word", a la que se le ira sumando ella misma y la letra correspondiente:
- 
reversed_word = r + reversed_word
reversed_word= a + r + reversed_word
reversed_word= l + a + r + reversed_word
reversed_word= l + l + a + r + reversed_word
reversed_word= a + l + l + a + r + reversed_word
reversed_word= r + a + l + l + a + r + reversed_word

- si "reversed_word" es igual a "word", la palabra es un palindromo, en cualquier caso contrario, no lo es.

### Punto 3:
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
```
def prime_number(numbers_list):
    primes_list=[]
    for number in numbers_list:
        divisors=[]
        for i in range (1,number):
            if number%i==0:
                divisors.append(i)
        if len(divisors)==1:
            primes_list.append(number)
    return primes_list
   
if __name__ == "__main__":
    numbers_list=[]
    n=int(input("Ingrese la cantidad de elementos de la lista:"))
    for i in range (n):
        numbers_list.append(int(input("*")))
    print(f"Los numeros primos de la lista que acaba de ingresar son: {prime_number(numbers_list)}")
```
### Punto 4:
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
```
def max_sum (numbers_list):
    maxi_sum=0


    for i in range (len(numbers_list)-1):# rango de 0 a n-2
        actual_sum=numbers_list[i]+numbers_list[i+1]# el ultimo i sera n-2 e i+1 sera n-1


        if actual_sum > maxi_sum:
            maxi_sum=actual_sum


    return maxi_sum


if __name__ == "__main__":      
    n=int(input("Ingrese el numero de elementos que tendra la lista: "))
    numbers_list=[]
    for i in range (n):
        numbers_list.append(int(input("*")))


    print (f"La mayor suma de elementos consecutivos es: {max_sum(numbers_list)}")
```
### Punto 5:
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]
```
def same_characters(words_list):
    same_char_list=[]
    for i in range (len(words_list)):
        first_word=words_list[i]


        for j in range (i+1, len(words_list)):
            second_word=words_list[j]


            first_chars = sorted(list(first_word))
            second_chars = sorted(list(second_word))


            if first_chars == second_chars:
                same_char_list.append(first_word)
                same_char_list.append(second_word)
    return same_char_list


if __name__ == "__main__":
    words_list=[]
    n=int(input("Ingrese la cantidad de elementos de la lista:"))
    for i in range (n):
        words_list.append(str(input("*")))
    print(f"Los elementos con los mismos caracteres son: {same_characters(words_list)}")
```
