
def encrypt(m):
    message_e = ''

    for c in m:
        if c == ' ':
            message_e += ' '
        else:
            message_e += chr(ord(c) + 5)
    return message_e


def decrypt(m):
    message_c = ''
    for c in m:
        if c == ' ':
            message_c += ' '
        else:
            message_c += chr(ord(c) - 5)
    return message_c


while True:
    op = input('Encrypt/Decrypt (E/D) or Leave (L)').lower()
    if op == 'l':
        break
    else:
        message = input('Enter a message: ')
        if op == 'e':
            print(encrypt(message))
        elif op == 'd':
            print(decrypt(message))
        else:
            print('Please, enter a valid option.')
