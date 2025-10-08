# python-encryption
Some small encryption algorithms / ciphers created using python. Here, i'll list each encryption algorithm with a short description.

Caesar Cipher
    - One of the simplest encryption algorithms, where each letter in the text is replaced by a letter some fixed number of positions down the alphabet, the shift paramenter used as the key. 
    For example, plaintext: "abc", key: 5. 
    Each letter will be shifted 5 positions right, so "a" becomes "f", "b" becomes "g", "c" becomes "h". 
    Thus, the encrypted string is now: "fgh".

Vigenere Cipher
    - Each letter of the original text is encoded with a different Caesar cipher, whos increment is determined by the corresponding letter of the key. 
    For example, plaintext: "abc", key: "def". 
    The first letter, a, is shifted 4 positions in the alphabet, as the first letter of the key, d, is the 4th letter of the alphabet. 
    Likewise, b is shifted 5 positions, c is shifted 6 positions. 
    Thus, the encrypted string is now: "egi".

Atbash Cipher
    - Another simple cipher algorithm, which reverses the alphabet so that the first letter maps onto the last letter. 
    For example, plaintext: "abc" would be mapped onto "zyx".

Diffie-Hellman Key Exchange
    - A mathematical method of generating a symmetric crytpographic key over a public channel. 
    Each party first agree on two public parameters, p (which is a prime modulus) and g (which is a primitive rood modulo p), and each choose their secret key values. 
    The first party sends the second party: A = g^(private_key) mod p. The second party sends the first party: B = g^(private_key) mod p.
    Then, each party computes s = recieved_value^(private_key) mod p. If everything is correct, both parties have the same shared secret.

Rail Fence Cipher
    - A ciphering method where plaintext is written downwards diagonally on 'rails' of an imaginary fence. Once the bottom rail has been reached, it zigzags up to the top. 
    For example, plaintext: "hello world" with a 3 'rail' fence: hol elwrd lo