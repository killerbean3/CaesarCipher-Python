#GitHub - @killerbean3 - CaesarCipher-Python
from string import punctuation
from itertools import cycle
print("""Instuctions for this encryption/decryption
Put your text in a .txt file named 'words'
Put your encryption key in a .txt file named 'ekey'""")
BASE = ord('a') - 1

def strToNums(s):
    """
    Convert a lowercase string to a list of integers in [1..26]
"""
    return [ord(ch) - BASE for ch in s]

def numsToStr(nums):
    """
    Convert a list of integers in [1..26] back to a lowercase string
"""
    return "".join(chr(n + BASE) for n in nums)

def shiftCypher(string, key_string, encry):
    nums = strToNums(string)
    key  = strToNums(key_string)
    if encry == "encrypt":
        encrypted = [((num + k - 1) % 26) + 1 for num,k in zip(nums, cycle(key))]
    elif encry == "decrypt":
        encrypted = [((num - k - 1) % 26) + 1 for num,k in zip(nums, cycle(key))]
    return numsToStr(encrypted)

def remove(string):
    return "".join(string.split())

def start():
    with open ("words.txt", "r") as myfile:
        text = myfile.readline()
        text3 = (remove(text.lower()))
    with open ("ekey.txt", "r") as myfile:
        key = myfile.readline()
        key3 = (remove(key.lower()))
    if any(c.isdigit() or c in punctuation for c in text3):
        exit("number or symbol detected in words.txt. Please remove number and restart.")
    if any(c.isdigit() or c in punctuation for c in key3):
        exit("number or symbol detected in ekey.txt. Please remove number and restart.")


    print("encrypt or decrypt?")
    choice = input(">").lower()

    if 'encrypt' in choice or 'decrypt' in choice:
        cypheren=shiftCypher(text3, key3, choice)
        with open ("words.txt", "w") as export:
            export.write(cypheren)
        print("check words.txt")
        print("Restarting code\n")
        start()
    else:
        print("encrypt or decrypt!")
        start()
start()
