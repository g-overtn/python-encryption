## python-encryption
### This repository contains some encryption algorithms / ciphers created using python. Here, i'll list each encryption algorithm with a short description.

* [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
    - One of the simplest cipher algorithms, where each letter in the text is replaced by a letter some fixed number of positions down the alphabet, the shift paramenter used as the key. 
    - For example, plaintext: "abc", key: 5. 
    - Each letter will be shifted 5 positions right, so "a" becomes "f", "b" becomes "g", "c" becomes "h". 
    - Thus, the enciphered string is now: "fgh".

* [Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
    - Each letter of the original text is encoded with a different Caesar cipher, whos increment is determined by the corresponding letter of the key. 
    - For example, plaintext: "abc", key: "def". 
    - The first letter, a, is shifted 4 positions in the alphabet, as the first letter of the key, d, is the 4th letter of the alphabet. 
    - Likewise, b is shifted 5 positions, c is shifted 6 positions. 
    - Thus, the enciphered string is now: "egi".

* [Atbash Cipher](https://en.wikipedia.org/wiki/Atbash)
    - Another simple cipher algorithm, which reverses the alphabet so that the first letter maps onto the last letter. 
    - For example, plaintext: "abc" would be mapped onto "zyx".

* [Diffie-Hellman Key Exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
    - A mathematical method of generating a symmetric crytpographic key over a public channel. 
    - Each party first agree on two public parameters, p (which is a prime modulus) and g (which is a primitive rood modulo p), and each choose their secret key values. 
    - The first party sends the second party: A = g^(private_key) mod p. The second party sends the first party: B = g^(private_key) mod p.
    - Then, each party computes s = recieved_value^(private_key) mod p. If everything is correct, both parties have the same shared secret.

* [Rail Fence Cipher](https://en.wikipedia.org/wiki/Rail_fence_cipher)
    - Plaintext is written downwards diagonally on 'rails' of an imaginary fence. Once the bottom rail has been reached, it zigzags up to the top. 
    - For example, plaintext: "hello world" with a 3 'rail' fence: hol elwrd lo

* [Columnar Transposition Cipher](https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition)
    - Plaintext is written out in rows of a fixed length, then read out again column by column, the columns chosen in a scrambled order.
    - The width of the rows and permutation of the columns are chosen by a keyword
    - E.g. consider the keyword: ZEBRAS and plaintext: we are discovered. flee at once
        - 6 letters long, so each row as a width of 6.
        - Column permutation determined by order of letters, so '6 3 2 4 1 5'
        - Writing this to the grid:
            - 6 3 2 4 1 5
            - W E A R E D
            - I S C O V E 
            - R E D F L E 
            - E A T O N C 
            - E _ _ _ _ _ 
        - The ciphertext once read: EVLN_ ACDT_ ESEA_ ROFO_ DEEC_ WIREE 
        - There are 5 nulls, these can be filled with any letter

* [Hill Cipher](https://en.wikipedia.org/wiki/Hill_cipher)
    - Each letter is represented by a modulo 26. Each block of n letters is multiplied by an n x n matrix against modulo 26.
    - The matrix should be chosen randomly from the set of invertible n x n matrices.
    - E.g. consider 'ACT', which translates to 0 2 19, with the 3x3 invertible matrix:
        - 6  24 1
        - 13 16 10
        - 20 17 15
    - mutliplying the matrix by the vector:
        - 6  24 1      0     67      15
        - 13 16 10  x  2  =  222  =  14 (mod 26)
        - 20 17 15     9     319     7
    - converting 15 14 7 into ciphertext: POH

* [Nihilist Cipher](https://en.wikipedia.org/wiki/Nihilist_cipher)
    - A [polybius square](https://en.wikipedia.org/wiki/Polybius_square) is created using a mixed alphabet generated with the key.
    - This is then used to convert both plaintext and a key into a series of 2-digit number, of which are added together.
    - Either a single key can be used, or two seperate ones.
    - Consider the polybius square key: 'zebras', plaintext: 'computers' and second key: 'hello'
    - The generated polybius square:
        -	Z	E	B	R	A
        -	S	C	D	F	G
        -	H	I/J	K	L	M
        -	N	O	P	Q	T
        -	U	V	W	X	Y 
    - Which converts the plaintext into: 22 42 35 43 51 45 12 14 21
    - The key is extended and converted into: 31 12 34 34 42 31 12 34 34
    - Added the two to make the ciphertext: 53 54 69 77 93 86 33 48 55

* [XOR cipher](https://en.wikipedia.org/wiki/XOR_cipher)
    - Operates according to the [XOR](https://en.wikipedia.org/wiki/Exclusive_or) operation.
    - A bitwise XOR operation is applied to each character in a given string using a given key. 
    - Take plaintext: "hello", and key: "hi".
    - Extending the key: "hihih", then performing XOR on each character: ammdj