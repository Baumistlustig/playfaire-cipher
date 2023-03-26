def encrypt(cleartext, key):
    # Convert Key & cleartext into lowercase
    key = key.lower()
    cleartext.lower()

    # Remove double characters
    key = "".join(dict.fromkeys(key))

    # Shorten the alphabet
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    for n in key:
        alphabet = alphabet.replace(n, "")

    # Create the encrypt-matrix
    matrix = []

    for i in range(5):
        row = []

        for j in range(5):
            # Create a row
            if len(key) > 5 * i + j:
                row.insert(j, key[5 * i + j])
            else:
                row.insert(j, alphabet[(5 * i + j) - len(key)])

        matrix.insert(i, row)

    print(matrix)

    # Create character pairs
    pairs = []
    for i in range(0, len(cleartext) + 1, 2):
        if len(cleartext) > (i + 1):
            if cleartext[i] != cleartext[i + 1]:
                pairs.insert(i, cleartext[i] + cleartext[i + 1])
            else:
                cleartext = cleartext[:i + 1] + "x" + cleartext[i + 1:]
                pairs.insert(i, cleartext[i] + "x")
        else:
            pairs.insert(i, cleartext[i] + "x")
    print(pairs)


if __name__ == "__main__":
    clearText = open("Python/cleartext.txt", "r").read()

    password = input("Pass in the encryption key (<25): ")
    while len(password) > 25:
        password = input("Pass in the encryption key (<25): ")

    encrypt(clearText, password)
