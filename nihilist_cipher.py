def constructPolybius(key : str) -> list[str]:
    """
    Constructs a polybius square using a mixed alphabet produced from the given string.

    Parameters: 
        key (str): the given string.
    
    Returns:
        ps (list[str]): the mixed-alphabet polybius square.
    """
    key = list(key)
    alphabet : list = list("abcdefghiklmnopqrstuvwxyz") #no 'j' as i and j share a square
    new : list[str] = list(dict.fromkeys(key + alphabet)) #combines and removes duplicates whilst preserving order
    if "j" in set(new): new.remove("j") #may be j's in the key, so want to remove them

    #adding rows
    ps : list[str] = []
    for i in range(0, 25, 5):
        ps.append(new[i:i+5])

    return ps

def NihilistEncipher(plaintext : str, key1 : str, key2: str) -> str:
    """
    Performs a Nihilist enciphering algorithm on the given string, using two given keys. Converts to lowercase and removes punctuation.

    Parameters:
        plaintext (str): the string to encipher.
        key1 (str): the key used in constructing a polybius square.
        key2 (str): the key that is added to the enciphered string.

    Returns:
        ciphertext (str): the enciphered string. 
    """
    ciphertext : str = ""
    alphabet : list = list("abcdefghijklmnopqrstuvwxyz")
    plaintext = "".join(c for c in plaintext.lower() if c in set(alphabet))

    ps : list[str] = constructPolybius(key1.lower())

    #replace j's with i's in plaintext
    plaintext = plaintext.replace('j', 'i')

    def convertNums(text : str) -> list[int]:
        """
        Nested function that converts a given text into a list of coordinates on a polybius square.

        Parameters:
            text (str): the given string to convert.
            
        Returns:
            nums (list[int]): a list of polybius square coordinates.
        """
        nums : list[int] = []
        for char in text:
            for i in range(5):
                if char in ps[i]:
                    nums.append(int(str(i+1) + str(ps[i].index(char) + 1)))
        
        return nums

    #convert plaintext into nums
    nums : list[int] = convertNums(plaintext)

    #shrink/extend key2 and convert into nums
    n = len(plaintext)
    keystream : str = ""
    for i in range(n // len(key2)):
        keystream += key2
    keystream += key2[:n % len(key2)]
    
    key_nums : list[int] = convertNums(keystream)

    #add up and concatenate to ciphertext
    for i in range(n):
        ciphertext += " " + str(nums[i] + key_nums[i])

    return ciphertext.rstrip()

print(NihilistEncipher("Dynamite Winter Palace!", "zebras", "russian"))