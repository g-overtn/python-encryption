def AtbashCipher(plaintext : str) -> str:
    """
    Performs an Atbash Cipher encryption/decryption algorithm on a given string, converts input to lowercase.

    Parameters:
        plaintext (str): the given string to be encrypted or decrypted.

    Returns:
        ciphertext (str): the encrypted/decrypted string.
    """

    ciphertext : str = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")

    for c in plaintext.lower():
        if c in alphabet: ciphertext += chr(219 - ord(c))
        else: ciphertext += c
    

    return ciphertext

print(AtbashCipher("The quick brown fox jumps over the lazy dog!"))
print(AtbashCipher("gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt!"))