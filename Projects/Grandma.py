while True:
    word = input("what do you think grandma likes?")

    if "a" in word or "e" in word or "i" in word or "u" in word or "o" not in word:
        print (f"Grandma doesn't like {word}!")
    else:
        print (f"Grandma likes {word}")

        print ("")