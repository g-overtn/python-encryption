def DESencrypt(plaintext : str, key : str) -> str:
    """
    Performs a Data Encryption Standard encryption algorithm on the provided 64-bit input and 64-bit key.

    Paramaters:
        plaintext (str): the input to encode.
        key (str): the key used.
    
    Returns:
        ciphertext (str): the encoded string.
    
    Raises:
        TypeError: if either parameters is not a string.
        ValueError: if either parameter does not have a length of 64, or is not a binary string.
    """
    #check the types and lengths of parameters
    if (type(plaintext) != str or type(key) != str): raise TypeError("Both parameters must be strings.")
    if (len(plaintext) != 64 or len(key) != 64): raise ValueError("Both parameters must be of length 64.")

    def generateKeys(key : str) -> list[str]:
        """
        Nested function that uses the 64-bit key to generate 16 sub-keys.
        Permutates the key, according to the PC-1 table, to generate a new 56-bit key.
        Splits that key into 16 pairs of new keys.
        Concatenates each pair of keys and permutates them, according to the PC-2 table, to generate 16 new 48-bit keys.
        """

        #pc-1 table
        pc_1 : list[int] = [57, 49, 41, 33, 25, 17, 9,
                            1, 58, 50, 42, 34, 26, 18,
                            10, 2, 59, 51, 43, 35, 27,
                            19, 11, 3, 60, 52, 44, 36,
                            63, 55, 47, 39, 31, 23, 15,
                            7, 62, 54, 46, 38, 30, 22,
                            14, 6, 61, 53, 45, 37, 29,
                            21, 13, 5, 28, 20, 21, 4]
        
        #pc-2 table
        pc_2 : list[int] = [14, 17, 11, 24, 1, 5,
                            3, 28, 15, 6, 21, 10,
                            23, 19, 12, 4, 26, 8,
                            16, 7, 27, 20, 13, 2,
                            41, 52, 31, 37, 47, 55,
                            30, 40, 51, 45, 33, 48,
                            44, 49, 39, 56, 34, 53,
                            46, 42, 50, 36, 29, 32]
        
        #left-shift table
        l_shifts : list[int] = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        
        #generate permutated key, split into two
        new_key : str = "".join([key[num-1] for num in pc_1])
        key_left : str = new_key[:28]
        key_right : str = new_key[28:]

        #for each iteration, we generate key[i] by left-shifting its bits according to the table
        subkeys_dict : dict[str, str] = {}
        for n in l_shifts:
            key_left = key_left[n:] + key_left[0:n]
            key_right = key_right[n:] + key_right[0:n]
            subkeys_dict[key_left] = key_right
        
        #for each pair of keys, concatenate them and apply a second permutation to generate final 16 keys
        subkeys_list : list[str] = []
        for k in subkeys_dict:
            new_subkey : str = k + subkeys_dict[k]
            new_subkey = "".join([new_subkey[num-1] for num in pc_2])
            subkeys_list.append(new_subkey)
    
        return subkeys_list

    subkeys : list[str] = generateKeys(key)
    
    #IP table
    ip_table : list[int] = [58, 50, 42, 34, 26, 18, 10, 2,
                            60, 52, 44, 36, 28, 20, 12, 4,
                            62, 54, 46, 38, 30, 22, 14, 6,
                            64, 56, 48, 40, 32, 24, 16, 8,
                            57, 59, 41, 33, 25, 16, 9, 1,
                            59, 51, 43, 35, 27, 19, 11, 3,
                            61, 53, 45, 37, 29, 21, 13, 5,
                            63, 55, 47, 39, 31, 23, 15, 7]

    #perform initial permutation on the plaintext, split in two
    plaintext = "".join(plaintext[num-1] for num in ip_table)
    plaintext_left : str = plaintext[:32]
    plaintext_right : str = plaintext[32:]

    def feistel(L : str, R : str, K : str) -> int:
        """
        Nested function that performs 'Ln-1 XOR f(Rn-1, Kn)' within each round of encryption.
        """
        
        #bit-selection table


        #first need to expand

    #perform 16 rounds of feistel cipher
    for i in range(16):
        temp : str = plaintext_left
        plaintext_left = plaintext_right #Ln = Rn-1
        plaintext_right = feistel #Rn = Ln-1 XOR f(Rn-1, Kn)


plaintext : str = '0110100001101001001000000111010001101000011001010111001001100101'
key : str = '0111011101100001011110100111101001100001011100000010000100100001'
print(DESencrypt(plaintext, key))