word=str(input("¿Qué palabra desea que se verifique?"))
reversed_word=""

for letter in word:
    reversed_word = letter + reversed_word

print(reversed_word)

if reversed_word==word:
    print ("La palabra ingresada es un palindromo ")
else:
    print ("La palabra ingresada no es un palindromo ")