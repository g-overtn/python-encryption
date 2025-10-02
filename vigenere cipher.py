def VigenereCipher(plaintext : str, key : str, direction : int) -> str:
    """
    Performs a Vigenere Cipher encryption/decryption algorithm on a given string, converts input to lowercase and removes all punctuation.

    Parameters:
        plaintext (str): the given string to be encrypted or decrypted.
        key (str): the key used to encrypt or decrypt the message.
        direction (int): decides whether to encrypt or decrypt the message. 1: encrypt, -1: decrypt.

    Returns:
        ciphertext (str): the encrypted/decrypted string.
    """

    ciphertext = ""
    keystream = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    plaintext = "".join(c for c in plaintext.lower() if c in alphabet)

    #extend/shrink key to match plaintext length
    for i in range(len(plaintext) // len(key)):
        keystream += key
    keystream += key[:len(plaintext) % len(key)]

    for i in range(len(plaintext)):
        val = (ord(plaintext[i]) - 96) + ((ord(keystream[i]) - 96) * direction)
        if val < 1: val += 26
        elif val > 26: val -= 26

        ciphertext += chr(val + 96)

    return ciphertext

print(VigenereCipher("Attack at dawn!", "lemon", 1))
print(VigenereCipher("mygpqwfgsois", "lemon", -1))