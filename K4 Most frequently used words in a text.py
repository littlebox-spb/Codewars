def top_3_words(text):
    sec={}
    text=text.lower()
    for z in ('#',',','.',':',';','/','\\'," ' ","  '''  ",'!','-', '_','?'):
        text=text.replace(z,' ')
    for s in text.split():
        sec[s]=sec.setdefault(s, 0)+1    
    result = sorted(sec.items(), key=lambda item: item[1], reverse=True)
    return([result[i][0] for i in range(3 if len(result)>=3 else len(result))])

'''
Чужое решение
from collections import Counter
import re


def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]
'''

assert top_3_words("a a a  b  c c  d d d d  e e e e e") == ["e", "d", "a"]
assert top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e") == ["e", "ddd", "aa"]
assert top_3_words("  //wont won't won't ") == ["won't", "wont"]
assert top_3_words("  , e   .. ") == ["e"]
assert top_3_words("  ...  ") == []
assert top_3_words("  '  ") == []
assert top_3_words("  '''  ") == []
assert top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income.""") == ["a", "of", "on"]

print("OK!")