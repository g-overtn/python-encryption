def xorEncipher(plaintext : str, key : str) -> str:
    """
    Performs an xor enciphering algorithm on the provided string with a given key.
    Converts both string and key to lowercase and removes punctuation.

    Parameters:
        plaintext (str): the text to encipher.
        key (str): the key used.

    Returns:
        ciphertext (str): the enciphered text.
    """
    ciphertext : str = ""
    alphabet : list = list("abcdefghijklmnopqrstuvwxyz")
    plaintext = "".join(c for c in plaintext.lower() if c in set(alphabet))
    key = "".join(c for c in key.lower() if c in set(alphabet))

    #shrink/extend key to match plaintext length
    n : int = len(plaintext)
    keystream : str = ""
    for i in range(n // len(key)):
        keystream += key
    keystream += key[:n % len(key)]

    for i in range(n):
        print(f"{plaintext[i]} : {ord(plaintext[i]) - 97}, {keystream[i]} : {ord(keystream[i]) - 97}, {plaintext[i] ^ keystream[i] = }")

    return ciphertext

print(xorEncipher("We all love computer science!", "nuh uh!"))