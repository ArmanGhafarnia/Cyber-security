cipher_text = "TYQTIMNHGICXABQSKDEKOHVPBVROIQTYQMIQFCQCKUNXFHVHISDAEFCFXOIEOWFHVEUEEEKANKTEUUSKMNKEHFDERXOEQFZSUIQSKAOUSAQUNXAUKMTKTEYARZLOEFHVSEEFLVNRVQZVDUWRLVPTYQIITAZDAJFHVKCFZTVYPCMTVPTYQMPETVDIVEOWFHVGNZHEIEEKTEJFICXNVESFRTYQMFYEEFEEHECAPVPTYQMFRFVDIESSFXATQADUDJFTYQCYMOJAFCUFV"
cipher_text = cipher_text.lower()


def Most_used(text, n):
    text = ''.join(char for char in text if char.isalpha()).lower()

    word_counts = {}

    for i in range(len(text) - n + 1):
        word = text[i:i + n]

        word_counts[word] = word_counts.get(word, 0) + 1

    if not word_counts:
        return None

    word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

    return word_counts


for i in range(3, 15):
    n = i
    result = Most_used(cipher_text, n)
    print("Most used word : ", result)


def find_indexes(text, word):
    indexes = []
    start_index = 0
    while True:
        index = text.find(word, start_index)
        if index == -1:
            break
        indexes.append(index)
        start_index = index + 1
    return indexes


word = "tyq"

word_indexes = find_indexes(cipher_text, word)
print("indexes :".format(word), word_indexes)

print([word_indexes[i] - word_indexes[i - 1] for i in range(1, len(word_indexes))])

key = ''
for i in range(3):
    key += chr(ord('tyq'[i]) - ord('the'[i]) + ord('a'))

print(key)

shifts = [ord(i) - ord('a') for i in key]

plain_text = ''

for i in range(0, len(cipher_text), 3):
    three_letter = cipher_text[i:i + 3]
    for j in range(3):
        try:
            plain_text += chr((ord(three_letter[j]) - ord('a') - shifts[j]) % 26 + ord('a'))
        except:
            pass

print(plain_text)


def decrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()

    ciphertext = ''
    key_index = 0

    for char in plaintext:

        if char.isalpha():

            shift = ord(key[key_index % len(key)]) - ord('A')

            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))

            ciphertext += encrypted_char

            key_index += 1
        else:

            ciphertext += char

    return ciphertext


plaintext = "ThetranquillakestretchedbeforethemreflectingthevibrantcolorsofthesunsetOnthedistantshorealonefigurestoodgazingoutatthehorizonThegentlebreezeruffledtheirhairastheycontemplatedthemysteriesoftheuniverseThestillnessofthemomentenvelopedthemofferingsolaceamidstthechaosoflife"
key = "arm"

encrypted_text = decrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
