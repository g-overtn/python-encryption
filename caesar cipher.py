def CaesarCipher(plaintext : str, key : int, direction : int) -> str:
    """
    Performs a Caesar Cipher encryption/decryption algorithm on a given string, converts input to lowercase.

    Parameters:
        plaintext (str): the given string to be encrypted or decrypted.
        key (int): the key used to encrypt or decrypt the message.
        direction (int): decides whether to encrypt or decrypt the message. 1: encrypt, -1: decrypt.

    Returns:
        ciphertext (str): the encrypted/decrypted string.
    """

    ciphertext : str = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    
    for c in plaintext.lower():
        if c in alphabet:
            val = (ord(c) - 96) + (key * direction)
            if val < 1: val += 26
            elif val > 26: val -= 26
            ciphertext += chr(val + 96)
        else:
            output += c

    return ciphertext

print(CaesarCipher("The quick brown fox jumps over the lazy dog.", 23, 1))
print(CaesarCipher("qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.", 23, -1))