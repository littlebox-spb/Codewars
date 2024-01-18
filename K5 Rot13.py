def rot13(message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    code = ""
    for c in message:
        start = alphabet.find(c)
        if start == -1:
            code += c
            continue
        if start < 26:
            newChar = start + 13 if start + 13 < 26 else abs(13 - (26 - start))
        else:
            newChar = start + 13 if start + 13 < 52 else abs(26 + 13 - (52 - start))
        code += alphabet[newChar]
    return code


assert rot13("test") == "grfg"
assert rot13("Test") == "Grfg"
assert rot13("aA bB zZ 1234 *!?%") == "nN oO mM 1234 *!?%"

print("OK")
