def AtbashCipher(text : str) -> str:
    """
    Performs an Atbash Cipher encryption/decryption algorithm on a given string, converts input to lowercase.

    Parameters:
        text (str): the given string to be encrypted or decrypted.

    Returns:
        output (str): the encrypted/decrypted string.
    """

    output : str = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")

    for c in text.lower():
        if c in alphabet: output += chr(219 - ord(c))
        else: output += c
    

    return output

print(AtbashCipher("The quick brown fox jumps over the lazy dog!"))
print(AtbashCipher("gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt!"))