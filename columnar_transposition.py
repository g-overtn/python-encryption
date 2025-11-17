def ColumnarEncrypt(plaintext : str, key : str) -> str:
    """
    Performs a columnar transposition ciphering algorithm on the provided string using the provided keyword, converts input to lowercase and removes punctuation.
    If there are any null spaces, replaces with x.

    Parameters:
        plaintext (str): the string to encipher.
        key (str): the keyword used.
    

    Returns:
        ciphertext (str): the enciphered string.
    """
    ciphertext : str = ""
    alphabet : list = list("abcdefghijklmnopqrstuvwxyz")
    plaintext = "".join(c for c in plaintext.lower() if c in set(alphabet))
    n : int = len(key)
    key = list(key)

    #getting column permutation
    cur : int = 1
    for i in range(len(alphabet)):
        for j in range(len(key)):
            if alphabet[i] == key[j]:
                key[j] = cur
                cur += 1
    
    #writing string to rows and replacing nulls with x
    rows : list[str] = [plaintext[i:i+n] for i in range(0, len(plaintext), n)]
    rows[-1] += 'x' * (n - len(rows[-1]))

    #writing each column to the ciphertext
    for i in range(1, n + 1):
        c : str = ""
        for row in rows:
            c += row[key.index(i)]
        ciphertext += c

    return ciphertext

def ColumnarDecrypt(ciphertext : str, key : str) -> str:
    """
    Performs a columnar transposition deciphering algorithm on the provided string with the provided keyword, converts input to lowercase and removes punctuation.
    
    Parameters:
        ciphertext (str): the string to decipher
        key (str): the key used.

    Returns:
        plaintext (str): the deciphered string
    """
    plaintext : str = ""
    alphabet : list = list("abcdefghijklmnopqrstuvwxyz")
    ciphertext = "".join(c for c in ciphertext.lower() if c in set(alphabet))
    n : int = len(key)
    key = list(key)

    #getting column permutation
    cur : int = 1
    for i in range(len(alphabet)):
        for j in range(len(key)):
            if alphabet[i] == key[j]:
                key[j] = cur
                cur += 1
    
    #finding row count
    row_count : int = len(ciphertext) // n

    #seperating into columns and ordering them
    columns : list[str] = [ciphertext[i:i+row_count] for i in range(0, len(ciphertext), row_count)]
    ordered_columns : list[str] = [[] * i for i in range(n)]
    for i in range(len(columns)):
        ordered_columns[key.index(i + 1)] = columns[i]

    #writing each row to the plaintext
    for i in range(row_count):
        for c in ordered_columns:
            plaintext += c[i]

    return plaintext

print(ColumnarEncrypt("We are discovered. Flee at once!", "zebras"))
print(ColumnarDecrypt("evlnxacdtxeseaxrofoxdeecxwiree", "zebras"))