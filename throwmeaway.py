debating = True

while debating:
    Can = [0, 1]
    Mic = [0, 1]

    if Can[0]:
        Mic[0] = True
        Mic[1] = False

    elif Can[1]:
        Mic[0] = False
        Mic[1] = True

    else:
        Mic[0] = False
        Mic[1] = False
