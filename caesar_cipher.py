def CaesarCipher(text : str, key : int, direction : int) -> str:
    """
    Performs a Caesar Cipher encipher/decipher algorithm on a given string, converts input to lowercase.

    Parameters:
        text (str): the given string to be enciphered or deciphered,
        key (int): the key used.
        direction (int): decides whether to encipher or decipher the message. 1: encipher, -1: decipher.

    Returns:
        output (str): the enciphered/deciphered string.
    """

    output : str = ""
    alphabet : set = set("abcdefghijklmnopqrstuvwxyz")
    
    for c in text.lower():
        if c in alphabet:
            val = (ord(c) - 96) + (key * direction)
            if val < 1: val += 26
            elif val > 26: val -= 26
            output += chr(val + 96)
        else:
            output += c

    return output

print(CaesarCipher("The quick brown fox jumps over the lazy dog.", 23, 1))
print(CaesarCipher("qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.", 23, -1))