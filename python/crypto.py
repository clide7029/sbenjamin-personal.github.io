def encode(message):
    e = list(message)
    index = 0
    for c in message:
        if(c == 'a'):
            e[index] = 'z'
        elif(c == 'b'):
            e[index] = 'y'
        elif(c == 'c'):
            e[index] = 'x'
        elif(c == 'd'):
            e[index] = 'w'
        elif(c == 'e'):
            e[index] = 'v'
        elif(c == 'f'):
            e[index] = 'u'
        elif(c == 'g'):
            e[index] = 't'
        elif(c == 'h'):
            e[index] = 's'
        elif(c == 'i'):
            e[index] = 'r'
        elif(c == 'j'):
            e[index] = 'q'
        elif(c == 'k'):
            e[index] = 'p'
        elif(c == 'l'):
            e[index] = 'o'
        elif(c == 'm'):
            e[index] = 'n'
        elif(c == 'n'):
            e[index] = 'm'
        elif(c == 'o'):
            e[index] = 'l'
        elif(c == 'p'):
            e[index] = 'k'
        elif(c == 'q'):
            e[index] = 'j'
        elif(c == 'r'):
            e[index] = 'i'
        elif(c == 's'):
            e[index] = 'h'
        elif(c == 't'):
            e[index] = 'g'
        elif(c == 'u'):
            e[index] = 'f'
        elif(c == 'v'):
            e[index] = 'e'
        elif(c == 'w'):
            e[index] = 'd'
        elif(c == 'x'):
            e[index] = 'c'
        elif(c == 'y'):
            e[index] = 'b'
        elif(c == 'z'):
            e[index] = 'a'
        index += 1
    secret_message = ""
    return secret_message.join(e)

def decode(encoded_message):
    d = list(encoded_message)
    index = 0
    for c in encoded_message:
        if(c == 'z'):
            d[index] = 'a'
        elif(c == 'y'):
            d[index] = 'b'
        elif(c == 'x'):
            d[index] = 'c'
        elif(c == 'w'):
            d[index] = 'd'
        elif(c == 'v'):
            d[index] = 'e'
        elif(c == 'u'):
            d[index] = 'f'
        elif(c == 't'):
            d[index] = 'g'
        elif(c == 's'):
            d[index] = 'h'
        elif(c == 'r'):
            d[index] = 'i'
        elif(c == 'q'):
            d[index] = 'j'
        elif(c == 'p'):
            d[index] = 'k'
        elif(c == 'o'):
            d[index] = 'l'
        elif(c == 'n'):
            d[index] = 'm'
        elif(c == 'm'):
            d[index] = 'n'
        elif(c == 'l'):
            d[index] = 'o'
        elif(c == 'k'):
            d[index] = 'p'
        elif(c == 'j'):
            d[index] = 'q'
        elif(c == 'i'):
            d[index] = 'r'
        elif(c == 'h'):
            d[index] = 's'
        elif(c == 'g'):
            d[index] = 't'
        elif(c == 'f'):
            d[index] = 'u'
        elif(c == 'e'):
            d[index] = 'v'
        elif(c == 'd'):
            d[index] = 'w'
        elif(c == 'c'):
            d[index] = 'x'
        elif(c == 'b'):
            d[index] = 'y'
        elif(c == 'a'):
            d[index] = 'z'
        index += 1
    secret_message = ""
    return secret_message.join(d)


secrets = encode(input("tell me your secrets: "))
print(secrets)
message = decode(secrets)
print(message)