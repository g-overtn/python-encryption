# python-encryption
Some small encryption algorithms created using python. Here, i'll list each encryption algorithm with a short description.

Caesar Cipher
    - One of the simplest encryption algorithms, where each letter in the text is replaced by a letter some fixed number of positions down the alphabet, the shift paramenter used as the key.

Vigenere Cipher
    - Each letter of the original text is encoded with a different Caesar cipher, whos increment is determined by the corresponding letter of the key.
    - For example, plaintext: "abc", key: "def"
        - The first letter, a, is shifted 4 positions in the alphabet, as the first letter of the key, d, is the 4th letter of the alphabet.
        - b is shifted 5 positions, c is shifted 6 positions.
        - Thus, the encrypted string is now: "egi"