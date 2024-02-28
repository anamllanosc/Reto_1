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