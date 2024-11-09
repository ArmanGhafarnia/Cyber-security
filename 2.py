family = "i am arman ghafarnia"
print(family)
print('\n')
num = ''.join(format(ord(char), '08b') for char in family)
num = num[:32]
num = num.zfill(32)
key = "01100010011001010110100001100101"


def right_shift(input, n):
    return input[:n] + input[n:]


def key_gen(key):
    first = key[:8]
    second = key[8:16]
    third = key[16:24]
    fourth = key[24:32]

    subs = []

    for i in range(1, 4):
        first = right_shift(first, 1 * i)
        second = right_shift(second, 2 * i)
        third = right_shift(third, 2 * i)
        fourth = right_shift(fourth, 1 * i)

        subs.append(first + second + third + fourth)

    return subs


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m

        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t

    if x1 < 0:
        x1 += m0
    return x1


def f(key, R):
    new_R = R + R
    xnor_result = ''.join([str(int(not (int(new_R[i]) ^ int(key[i])))) for i in range(32)])

    output = ''
    for i in range(0, 32, 8):
        my_box_input = xnor_result[i:i + 8]
        l, r = int(my_box_input[:4], 2), int(my_box_input[4:], 2)

        l, r = mod_inverse(l, 17), mod_inverse(r, 17)

        out = (l * r) % 17

        if out == 16:
            out = 9

        out = bin(out)[2:]
        out = out.zfill(4)
        output += out

    return output


def feistel(l, r, key):
    new_l = r

    out = f(key, r)
    new_r = int(l, 2) ^ int(out, 2)

    new_r = bin(new_r)[2:]
    new_r = new_r.zfill(16)

    return new_l, new_r


def my_des(input, keys):
    l, r = input[:16], input[16:]

    for i in range(3):
        l, r = feistel(l, r, keys[i])

    return r + l


def binary_to_string(binary_str):
    byte_chunks = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]

    characters = [chr(int(byte, 2)) for byte in byte_chunks]

    return ''.join(characters)




key_all = key_gen(key)

family = ''.join(format(ord(char), '08b') for char in family)

blocks = []
for i in range(0, len(family), 32):
    blocks.append(family[i:i + 32])

while len(blocks[-1]) < 32:
    blocks[-1] += '0'

cipher_text = ''
for block in blocks:
    cipher_text += my_des(block, key_all)


key_all = key_gen(key)
key_all = key_all[::-1]
blocks = []
for i in range(0, len(cipher_text), 32):
    blocks.append(cipher_text[i:i + 32])

while len(blocks[-1]) < 32:
    blocks[-1] += '0'

plain = ''
for block in blocks:
    plain += my_des(block, key_all)


print(binary_to_string(cipher_text))
print('\n')
result = binary_to_string(plain)
print(result)
