alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def main(plan_text,shift_amount):
    cipher_text=""
    for char in plan_text:
        position = alphabet.index(char)
        if direction=="encode":
            new_position=position+ shift_amount
        elif direction=="decode":
            new_position=position- shift_amount
        new_letter=alphabet[new_position]
        cipher_text += new_letter
    print(f"The {direction} text is {cipher_text}")

main(plan_text=text,shift_amount=shift)

