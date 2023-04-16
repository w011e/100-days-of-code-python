from day_8_project_art import logo

def caesar(text, shift, direction):
    output = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            output += alphabet[new_position]
        else: 
            output += char 
    print(f"Here is the {direction}d result: {output}")

print(logo)

alphabet = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

restart = "yes"
while restart == "yes":
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n').lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26      
    caesar(text, shift, direction)
    restart = input('Do you want to restart the cipher program? Type "yes" if you want to go again. Otherwise, type "no".\n').lower()
if restart == "no":
    print("Thank you for using this programme :)")



#first ideas of code:

# def encrypt (plain_text, shift_amount):
#     cipher_text = ""
#     for char in plain_text:
#         position = alphabet.index(char)
#         new_position = position + shift_amount 
#         new_char = alphabet[new_position]
#         cipher_text += new_char
#     print(f"The encoded text is {cipher_text}")
# def decrypt (cipher_text, shift_amount):
#     plain_text = ""
#     for char in cipher_text:
#         position = alphabet.index(char)
#         new_position = position - shift_amount
#         new_char = alphabet[new_position]
#         plain_text += new_char
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("You've typed the wrong command for this programme. Please start again.")

# def caesar(text, shift, direction):
#     output = ""
#     if direction == "encode": 
#         for char in text:
#             position = alphabet.index(char)
#             new_position = position + shift
#             new_char = alphabet[new_position]
#             output += new_char
#         print(f"The encoded text is {output}")
#     elif direction == "decode":
#         for char in text:
#             position = alphabet.index(char)
#             new_position = position - shift
#             new_char = alphabet[new_position]
#             output += new_char
#         print(f"The decoded text is {output}")
# caesar(text, shift, direction)