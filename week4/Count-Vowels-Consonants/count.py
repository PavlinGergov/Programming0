def count_vowels_consonants(word):
    vols = "aeiouyAEIOUY"
    cons = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    info = {
            "vowels": 0,
            "consonants": 0,
            }
    for char in word:
        if char in vols:
            info['vowels'] += 1
        elif char in cons:
            info['consonants'] += 1
    return info

print(count_vowels_consonants("aaaAcccD"))
