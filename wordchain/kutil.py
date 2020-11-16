def ruleofthumb(c):
    if '가' <= c <= '힝':
        ph = get_phoneme(c)
        if ph[0] == 0x1102:
            if ph[1] == 0x1167 or ph[1] == 0x116D or ph[1] == 0x1172 or ph[1] == 0x1175:
                ph[0] = 0x110B
        elif ph[0] == 0x1105:
            if ph[1] == 0x1163 or ph[1] == 0x1167 or ph[1] == 0x1168 \
                    or ph[1] == 0x116D or ph[1] == 0x1172 or ph[1] == 0x1175:
                ph[0] = 0x110B
            elif ph[1] == 0x1161 or ph[1] == 0x1162 or ph[1] == 0x1169 \
                    or ph[1] == 0x116C or ph[1] == 0x116E or ph[1] == 0x1173:
                ph[0] = 0x1102
        c = get_syllable(ph)
    return c


def get_phoneme(kor):
    c = ord(kor) - 0xAC00
    cf = ((c - (c % 28)) // 28) // 21 + 0x1100
    cm = ((c - (c % 28)) // 28) % 21 + 0x1161
    cl = (c % 28) + 0x11a7
    return [cf, cm, cl]


def get_syllable(phs):
    return chr(0xAC00 + (phs[0] - 0x1100) * 28 * 21 + (phs[1] - 0x1161) * 28 + phs[2] - 0x11a7)



