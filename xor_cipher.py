def xorCipher(plaintext : str, key : str) -> str:
    """
    Performs an xor ciphering algorithm on the provided string with a given key.

    Parameters:
        plaintext (str): the text to encipher/decipher.
        key (str): the key used.

    Returns:
        ciphertext (str): the enciphered/deciphered text.
    """
    ciphertext : str = ""

    #shrink/extend key to match plaintext length
    n : int = len(plaintext)
    keystream : str = ""
    for i in range(n // len(key)):
        keystream += key
    keystream += key[:n % len(key)]

    #xor each character together, mod 26 then add to ciphertext
    for i in range(n):
        ciphertext += chr((ord(plaintext[i]) - 97 ^ ord(keystream[i]) - 97) + 97)

    return ciphertext


k : str = "comp sci"
a : str = xorCipher("abcdefghijklmnopqrstuvwxyz", k); print(a)
b : str = xorCipher(a, k); print(b)