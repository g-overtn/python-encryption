import DES_data as dd

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
        """
        
        #generate permutated key, split into two
        new_key : str = "".join([key[num-1] for num in dd.pc_1])
        key_left : str = new_key[:28]
        key_right : str = new_key[28:]

        #for each iteration, we generate key[i] by left-shifting its bits according to the table
        subkeys_dict : dict[str, str] = {}
        for n in dd.l_shifts:
            key_left = key_left[n:] + key_left[0:n]
            key_right = key_right[n:] + key_right[0:n]
            subkeys_dict[key_left] = key_right
        
        #for each pair of keys, concatenate them and apply a second permutation to generate final 16 keys
        subkeys_list : list[str] = []
        for k in subkeys_dict:
            new_subkey : str = k + subkeys_dict[k]
            new_subkey = "".join([new_subkey[num-1] for num in dd.pc_2])
            subkeys_list.append(new_subkey)
    
        return subkeys_list

    subkeys : list[str] = generateKeys(key)

    #perform initial permutation on the plaintext, according to ip table, and split in two
    plaintext = "".join([plaintext[num-1] for num in dd.ip_table])
    plaintext_left : str = plaintext[:32]
    plaintext_right : str = plaintext[32:]

    def feistel(L : str, R : str, K : str) -> int:
        """
        Nested function that performs 'Ln-1 XOR f(Rn-1, Kn)' within each round of encryption.
        """
    
        #start of f(Rn-1, Kn) function
        #first need to expand R to 48 bits
        R = "".join([R[num-1] for num in dd.bs_table])

        #K XOR R
        xor_res : str = "".join([str(int(K[i]) ^ int(R[i])) for i in range(48)])

        #split into 8 groups of 6 bits
        groups : list[str] = [xor_res[i:i+6] for i in range(0, 48, 6)]

        #get coordinate value from each s_box for each group of bits, concatenate
        res : str = ""
        for i in range(8):
            b : str = groups[i]
            row : int = int(b[0] + b[-1], 2)
            column : int = int(b[1:-2], 2)
            s_box : list[list[int]] = dd.s_boxes[i]
            res += format(s_box[row][column], '04b') #gets the value at the coordinates and converts into 4 bits of binary, concatenates
        
        #f-permutate result
        res = "".join([res[num-1] for num in dd.fp_table])

        #Ln-1 XOR res
        final_xor_res : str = "".join([str(int(L[i]) ^ int(res[i])) for i in range(32)])

        return final_xor_res

    #perform 16 rounds of feistel cipher, then concatenate
    for i in range(16):
        temp : str = plaintext_left #temp = Ln-1
        plaintext_left = plaintext_right #Ln = Rn-1
        plaintext_right = feistel(temp, plaintext_right, subkeys[i]) #Rn = Ln-1 XOR f(Rn-1, Kn)
    
    ciphertext : str = plaintext_right + plaintext_left

    #perform final permutation according to ip inverse
    ciphertext = "".join([ciphertext[num-1] for num in dd.ip_inverse_table])

    return ciphertext


plaintext : str = '0110100001101001001000000111010001101000011001010111001001100101'
key : str = '0111011101100001011110100111101001100001011100000010000100100001'
print(DESencrypt(plaintext, key))
