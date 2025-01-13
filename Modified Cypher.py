alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']





def cipher(t,s,d):
    cipher_text=""
    if direction == "decode":
        s *= -1
    for i in t:
        if i in alphabet:
            position=alphabet.index(i)
            new_positon = position + s
            new_letter = alphabet[new_positon]
            cipher_text += new_letter
        else:
            cipher_text+=i
    print(f"The {d}d text is '{cipher_text}'.")



should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cipher(text,shift,direction)
    restart=input("If you want to continue again type 'Yes' and if you dont want to type 'No'. ").lower()
    if restart=="no":
        should_continue=False
        print("Cipher ENDS")
