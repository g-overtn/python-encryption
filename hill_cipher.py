def multiplyMatrices():
    pass

def HillCipherEncrypt(plaintext : str, key : list[list[int]]) -> str:
    """
    Performs a Hill Cipher encryption algorithm on a given plaintext and an n x n matrix grid as a key.
    Converts the given string to lowercase and removes punctuation.

    Parameters:
        plaintext (str): the given text to be encrypted. If the amount of characters is not divisible by n, it is padded with 'x'.
        key (list[list[int]]): an invertible n x n matrix against modulus 26.

    Returns:
        ciphertext (str): the encrypted text.
    """
    ciphertext : str = ""
    return ciphertext

def HillCipherDecrypt():
    pass


key : list[list[int]] = [
    [17, 17, 5],
    [21, 18, 21],
    [2, 2, 19]
]

print(HillCipherEncrypt("Pay more money!", key))