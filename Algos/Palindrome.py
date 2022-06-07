"""Two functions for checking if a word is a palindrome"""


def palindrome1(seq):
    seq = seq.lower()
    if seq == seq[::-1]:
        return True
    else:
        return False


def palindrome2(seq):
    seq = seq.lower()
    for i in range(len(seq) // 2):
        if seq[i] == seq[-i - 1]:
            pass
        else:
            return False
    return True
