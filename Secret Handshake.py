def commands(binary_str):
    l = ['jump', 'close your eyes', 'double blink', 'wink']
    handshake = []
    for i in range(4, 0, -1):
        if binary_str[i] == '1':
            handshake.append(l[i-1])
    if binary_str[0] == '1':
        handshake.reverse()
    return handshake