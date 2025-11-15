def VigenereCipher(text : str, key : str, direction : int) -> str:
    """
    Performs a Vigenere Cipher encipher/decipher algorithm on a given string, converts input to lowercase and removes all punctuation.

    Parameters:
        text (str): the given string to be enciphered or deciphered.
        key (str): the key used.
        direction (int): decides whether to encipher or decipher the message. 1: encipher, -1: decipher.

    Returns:
        output (str): the enciphered/deciphered string.
    """

    output : str = ""
    keystream : str = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    text = "".join(c for c in text.lower() if c in alphabet)

    #extend/shrink key to match plaintext length
    for i in range(len(text) // len(key)):
        keystream += key
    keystream += key[:len(text) % len(key)]

    for i in range(len(text)):
        val = (ord(text[i]) - 96) + ((ord(keystream[i]) - 96) * direction)
        if val < 1: val += 26
        elif val > 26: val -= 26

        output += chr(val + 96)

    return output

print(VigenereCipher("Attack at dawn!", "lemon", 1))
print(VigenereCipher("mygpqwfgsois", "lemon", -1))