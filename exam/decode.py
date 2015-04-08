def decode_word(encrypted_word, cipher):
    new_cipher = {cipher[key]: key for key in cipher}
    return "".join([new_cipher[ch] for ch in encrypted_word])


def main():
    print(decode_word("mjriew", {
        'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'}) == 'python')
    print(decode_word("rpf", {'m': 'p', 'o': 'r', 'g': 'f'}) == 'omg')
    print(decode_word("wfhsftzzuys", {
        'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'}) == 'programming')
    print(decode_word("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'}) == 'aaaaaaaaaaaaaaaaaaaaaaaaaaa')

if __name__ == '__main__':
    main()
