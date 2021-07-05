import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for sign in  plaintext:
        key = ord(sign)
        if sign.isupper():
            start = ord("A")
        elif sign.isslower():
            start = ord('a')
        else:
            ciphertext+=chr(key)
            continue
        difference =key-start
        key=(difference +shift)%26+start
        ciphertext +=chr(key)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for sign in ciphertext:
        key = ord(sign)
        if ord('A')<= key<= ord('Z'):
            difference =key - ord('A')
            key = (diff-shift)%26+ord('a')
        elif ord('a') <= key <= ord('z'):
            difference = key - ord('a')
            key = (difference - shift)% 26 + ord('a')
        plaintext += chr(key)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
