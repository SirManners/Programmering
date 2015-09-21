__author__ = 'ab53995'

while True:

    plain_text = input("What do you want to encrypt?")

    if plain_text == "q":
        break

    encrypted_text = ""
    for c in plain_text:
        x = ord(c)
        x = x + 5
        c2 = chr(x)
        encrypted_text = encrypted_text + c2

    print(encrypted_text)



    encrypted_text = input("What text do you want to decrypt?")

    if plain_text == "q":
        break


    plain_text = ""
    for c in encrypted_text:
        x = ord(c)
        x = x - 5
        c2 = chr(x)
        plain_text = plain_text + c2

    print(plain_text)
