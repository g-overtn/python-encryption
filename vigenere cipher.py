def VigenereCipher(text : str, key : str, direction : int) -> str:
    """
    Performs a Vigenere Cipher encryption/decryption algorithm on a given string, converts input to lowercase and removes all punctuation.

    Parameters:
        text (str): the given string to be encrypted or decrypted.
        key (str): the key used to encrypt or decrypt the message.
        direction (int): decides whether to encrypt or decrypt the message. 1: encrypt, -1: decrypt.

    Returns:
        output (str): the encrypted/decrypted string.
    """

    output : str = ""
    keystream : str = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    text = "".join(c for c in text.lower() if c in alphabet)

    #extend/shrink key to match plaintext length
    for i in range(len(text) // len(key)):
        keystream += key
    keystream += key[:len(text) % len(key)]

    for i in range(len(text)):
        val = (ord(text[i]) - 96) + ((ord(keystream[i]) - 96) * direction)
        if val < 1: val += 26
        elif val > 26: val -= 26

        output += chr(val + 96)

    return output

print(VigenereCipher("Attack at dawn!", "lemon", 1))
print(VigenereCipher("mygpqwfgsois", "lemon", -1))