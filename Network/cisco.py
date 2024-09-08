def decrypt_type7(password):
    # Cisco type 7 password decryption algorithm
    key = [int(x, 16) for x in "0123456789ABCDEF"]
    decrypted = []
    for i in range(0, len(password), 2):
        c = int(password[i:i+2], 16)
        decrypted.append(chr(c ^ key[i // 2 % 16]))
    return ''.join(decrypted)

encrypted_passwords = [
    "025017705B3907344E",
    "10181A325528130F010D24",
    "124F163C42340B112F3830",
    "144101205C3B29242A3B3C3927"
]

for password in encrypted_passwords:
    print(decrypt_type7(password))
