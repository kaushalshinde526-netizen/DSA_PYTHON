def encode(strs):
    encoded = ""

    for s in strs:
        encoded += str(len(s)) + "#" + s

    return encoded


def decode(encoded):
    decoded = []
    i = 0

    while i < len(encoded):
        j = i

        while encoded[j] != "#":
            j += 1

        length = int(encoded[i:j])

        word = encoded[j + 1:j + 1 + length]
        decoded.append(word)

        i = j + 1 + length

    return decoded


n = int(input("Enter number of strings: "))

strs = []

for i in range(n):
    s = input(f"Enter string {i+1}: ")
    strs.append(s)

encoded_string = encode(strs)

print("\nEncoded String:")
print(encoded_string)

decoded_strings = decode(encoded_string)

print("\nDecoded Strings:")
print(decoded_strings)