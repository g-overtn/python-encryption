def RailFenceEncrypt(plaintext : str, rails: int) -> str:
    """
    Performs a Rail Fence Cipher algorithm on a given string, converts input to lowercase and removes punctuation.

    Parameters:
        plaintext (str): the given string to be encrypted.
        rails (int): the number of imaginary rails to be used.

    Returns:
        ciphertext (str): the enciphered string.
    """

    ciphertext : str = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    fence : list = [[] * 1 for i in range(rails)]
    direction : int = 1
    rail : int = 0
    for c in plaintext.lower():
        if c in alphabet:
            fence[rail].append(c)
            rail += direction
            if rail == 0 or rail == rails - 1:
                direction *= -1

    for i in range(rails):
        ciphertext += "".join(c for c in fence[i])
        ciphertext += " "

    return ciphertext.rstrip()

def RailFenceDecrypt(ciphertext : str, rails: int) -> str:
    """
    Performs a Rail Fence Decipher algorithm on a given string, converts input to lowercase and removes punctuation.

    Parameters:
        cipher (str): the given string to be decrypted.
        rails (int): the number of imaginary rails to be used.

    Returns:
        plaintext (str): the deciphered string.
    """
    plaintext : str = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    fence : list = ciphertext.split(" ")
    direction : int = 1
    rail : int = 0
    for c in ciphertext.lower():
        if c in alphabet:
            plaintext += fence[rail][0]
            fence[rail] = fence[rail][1:] #remove first character from the rail
            rail += direction
            if rail == 0 or rail == rails - 1:
                    direction *= -1

    return plaintext

print(RailFenceEncrypt("We are discovered! Run at once!", 4))
print(RailFenceDecrypt("wira edseente aecvduoc rorn", 4))
