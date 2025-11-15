

def HillCipherEncrypt(plaintext : str, matrix : list[list[int]]) -> str:
    """
    Performs a hill cipher enciphering algorithm on a given string and n x n invertible matrix against modulo 26, converts to lowercase and removes punctuation. 
    Assumes it is invertible and modulo 26.
    If the length of the string is not divisible by n, pads with x.

    Parameters:
        plaintext (str): the plaintext to be enciphered.
        matrix (list[list[int]]): the matrix used.

    Returns:
        ciphertext (str): the enciphered result.
    """
    ciphertext : str = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    n : int = len(matrix)

    #converting our string into chunks and padding
    plaintext = "".join(c for c in plaintext.lower() if c in alphabet)
    chunks : list[list[str]] = [plaintext[i:i+n] for i in range(0, len(plaintext), n)]
    chunks[-1] += 'x' * (n - len(chunks[-1]))

    #convering chunks into vectors
    vectors : list[list[int]] = []
    for chunk in chunks:
        vectors.append([ord(s) - 97 for s in chunk])
    print(vectors)

    #multiplying each vector by the matrix


    return ciphertext

#2x2 matrix key
key2 : list[list[int]] = [
    [6, 24],
    [13, 16]
]

#3x3 matrix key
key3 : list[list[int]] = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

print(HillCipherEncrypt("The name of the game is survival!", key3))