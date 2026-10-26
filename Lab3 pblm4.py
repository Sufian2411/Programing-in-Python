ch = input("Enter a character: ")

if len(ch) == 1 and ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Not vowel")