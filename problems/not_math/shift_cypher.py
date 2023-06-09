def shift_cipher(message, shift):
    enc_message = ""
    for index in message:
        xyz = ord(index)
        enc_message += chr(xyz + shift)
    return enc_message


print(shift_cipher("abc", 1))
print(shift_cipher("Raining-Frogs", -10))
