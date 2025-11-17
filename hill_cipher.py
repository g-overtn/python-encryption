import numpy as np

def HillEncipher(plaintext : str, m : np.matrix) -> str:
    """
    Performs a hill cipher enciphering algorithm on a given string and n x n invertible matrix against modulo 26, converts to lowercase and removes punctuation. 
    Assumes the matrix is invertible.
    If the length of the string is not divisible by n, pads with x.

    Parameters:
        plaintext (str): the plaintext to be enciphered.
        matrix (np.matrix): the key matrix used.

    Returns:
        ciphertext (str): the enciphered result.
    """
    ciphertext : str = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    m = m % 26
    n : int = len(m)

    #converting our string into chunks and padding
    plaintext = "".join(c for c in plaintext.lower() if c in alphabet)
    chunks : list[list[str]] = [plaintext[i:i+n] for i in range(0, len(plaintext), n)]
    chunks[-1] += 'x' * (n - len(chunks[-1]))

    #convering chunks into vectors
    vectors : list[list[int]] = []
    for chunk in chunks:
        vectors.append([ord(s) - 97 for s in chunk])

    #multiplying each vector by the matrix and applying modulo 26
    vectors = [m.dot(v) % 26 for v in vectors]

    #converting vectors back into characters
    for v in vectors:
        new_chunk : str = "".join([chr(x + 97) for x in np.nditer(v)])
        ciphertext += new_chunk

    return ciphertext

def HillDecipher(ciphertext : str, m : np.matrix) -> str:
    """
    Performs a hill cipher decryption algorithm on a given string and n x n invertible matrix against modulo 26, converts to lowercase and removes punctuation.
    Assumes the matrix is invertible.
    Assumes the string is divisible by n, else your matrix key is wrong.

    Parameters:
        ciphertext (str): the string to be deciphered.
        matrix (np.matrix): the key matrix used.

    Returns:
        ciphertext (str): the deciphered result.
    """
    plaintext : str = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    m = m % 26
    n : int = len(m)

    #converting our string into chunks
    ciphertext = "".join(c for c in ciphertext.lower() if c in alphabet)
    chunks : list[list[str]] = [ciphertext[i:i+n] for i in range(0, len(ciphertext), n)]

    #converting chunks into vectors
    vectors : list[list[int]] = []
    for chunk in chunks:
        vectors.append([ord(s) - 97 for s in chunk])
    
    #calculating inverse matrix against modulo 26
    mI = np.linalg.inv(m)
    print(mI)
    print(mI.round())

    return plaintext


#2x2 matrix key
key2 : np.matrix = np.matrix([[3, 3], 
                              [2, 5]])

#3x3 matrix key
key3 : np.matrix = np.matrix([[6, 24, 1], 
                              [13, 16, 10], 
                              [20, 17, 15]])

#print(HillCipherEncrypt("The name of the game is survival!", key3))
print(HillEncipher("act", key3))
print(HillDecipher("poh", key3))