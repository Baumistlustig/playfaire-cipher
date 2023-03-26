def encrypt(cleartext, key):
    # Convert Key into lowercase
    key = key.lower()
    # Remove double characters
    key = "".join(dict.fromkeys(key))

    # Shorten the alphabet
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    for n in key:
        alphabet = alphabet.replace(n, "")

    matrix = []

    for i in range(5):
        row = []

        for j in range(5):
            if len(key) > 5 * i + j:
                row.insert(j, key[5 * i + j])
            else:
                row.insert(j, alphabet[(5 * i + j) - len(key)])

        matrix.insert(i, row)

    print(matrix)


if __name__ == "__main__":
    clearText = open("Python/cleartext.txt", "r").read()

    password = input("Pass in the encryption key (<25): ")
    while len(password) > 25:
        password = input("Pass in the encryption key (<25): ")

    encrypt(clearText, password)
