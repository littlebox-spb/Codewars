def spin_words(sentence):
    sentenceclear = ""
    for i in range(len(sentence)):
        if sentence[i].isalpha() or sentence[i] == " ":
            sentenceclear += sentence[i]
    words = sentenceclear.split()
    result = ""
    for word in words:
        print(word)
        if len(word) < 5:
            result += word + " "
        else:
            result += word[::-1] + " "
    return result.strip()


TestSting = "this Kata Strings name Just letter words"
#             'this Kata sgnirtS name Just rettel words'
# should equal 'this Kata sgnirtS name Just rettel sdrow"
print(spin_words(TestSting))

# Чужое решение
"""
def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)
"""
