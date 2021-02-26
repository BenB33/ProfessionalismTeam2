def xorEncryption(password):
    key = 'B'
    length = len(password);
    for i in range(length):
        password = (password[:i] +
                    chr(ord(password[i] ^ ord(key)) +
                        password[i+1]);
    return password;



