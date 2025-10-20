def multiplyVectorByMatrix(key_matrix : list[list[int]], chunk_vector : list[int]) -> list[int]:
    """
    Mutliplies the given n-component vector by the given key matrix, then returns the result against modulus 26.

    Parameters:
        key_matrix (list[list[int]]): an invertible n x n matrix.
        chunk_vector (list[int]): an n-component vector.

    Returns:
        enciphered_vector (list[int]): the result n-component vector.
    """
    enciphered_vector : list[int] = []
    n : int = len(chunk_vector)
    for row in key_matrix:
        total : int = 0
        for i in range(n):
            total += (row[i] * chunk_vector[i])
        enciphered_vector.append(total % 26 + 1)
    
    return enciphered_vector

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
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    plaintext = "".join(c for c in plaintext.lower() if c in alphabet)

    #split text into chunks of size n, pad with 'x'
    n : int = len(key[0])
    chunks : list[str] = [plaintext[i:i+n] for i in range(0, len(plaintext), n)]
    last_chunk_len : int = len(chunks[-1])
    if last_chunk_len != n:
        chunks[-1] += 'x' * (n - last_chunk_len)
    
    #convert each chunk into an n-component vector, each component being the modulo 26 value of the character
    vectors : list[list[int]] = []
    for chunk in chunks:
        vector : list[int] = [ord(c) - 96 for c in chunk]
        vectors.append(vector)
    
    #perform a matrix multiplication on each vector with the key
    enciphered_vectors : list[list[int]] = [multiplyVectorByMatrix(key, vector) for vector in vectors]

    #re-convert each column vector into an encpihered string chunk, then add that to the returned ciphertext
    ciphertext : str = ""
    for vector in enciphered_vectors:
        new_chunk : str = "".join(chr(val + 96) for val in vector)
        ciphertext += new_chunk
    
    return ciphertext

def HillCipherDecrypt(ciphertext : str, key : list[list[int]]) -> str:
    """
    Performs a Hill Cipher decryption algorithm on a given ciphertext and an n x n matrix grid as a key.
    Converts the given string to lowercase and removes punctuation.

    Parameters:
        ciphertext (str): the given text to be decrypted. Assumes that the string is divisible by n.
        key (list[list[int]]): an invertible n x n matrix against modulus 26.

    Returns:
        plaintext (str): the encrypted text.
    """

    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    ciphertext = "".join(c for c in ciphertext.lower() if c in alphabet)

    #split text into chunks of size n
    #no need to pad as (if using right key size) ciphertext will be divisible by n
    n : int = len(key[0])
    chunks : list[str] = [ciphertext[i:i+n] for i in range(0, len(ciphertext), n)]

    #TODO - calculate the inverse matrix of the key
    return 0


key1 : list[list[int]] = [ 
    [3, 3],
    [2, 5]
]

key2 : list[list[int]] = [
    [17, 17, 5],
    [21, 18, 21],
    [2, 2, 9]
]

#using a 2x2 matrix as key
print(HillCipherEncrypt("Pay more money, okay?", key1))
#print(HillCipherDecrypt("zlklvqcxjwmfahax", key1))

#using a 3x3 matrix as key
print(HillCipherEncrypt("Pay more money, okay?", key2))
#print(HillCipherDecrypt("dynhcrupefapojyids", key2))

#i fear for anyone using a 4x4 matrix