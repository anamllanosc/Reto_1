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
    print(f"Ingrese las {n} palabras a comparar")
    for i in range (n):
        words_list.append(str(input("*")))
    print(f"Los elementos con los mismos caracteres son: {same_characters(words_list)}")