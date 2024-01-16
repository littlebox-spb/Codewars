def is_test_interesting(number, awesome_phrases):
    if number<100:
        return False
    if not int(str(number)[1::]):
        return True
    if len(awesome_phrases) and (number in awesome_phrases):
        return True
    if str(number)==str(number)[-1::-1]:
        return True
    if str(number)==str(number)[0]*len(str(number)):
        return True
    s=int(str(number)[0])
    flag=True
    for i in range(1,len(str(number))):
        if int(str(number)[i])+1==s and flag:
            s=int(str(number)[i])
        elif int(str(number)[i])-1==s or (int(str(number)[i])==0 and s==9):
            s=int(str(number)[i])
            flag=False
        else:
            return False
    else:
        return True
        
        
        
def is_interesting(number, awesome_phrases):
    if is_test_interesting(number, awesome_phrases):
        return 2
    elif is_test_interesting(number+1, awesome_phrases) or is_test_interesting(number+2, awesome_phrases):
        return 1
    return 0
        

'''
+Любая цифра, за которой следуют все нули: 100,90000
+Каждая цифра представляет собой одно и то же число:1111
Цифры идут последовательно, начиная с † :1234
Цифры идут последовательно, уменьшаясь ‡ :4321
+Цифры представляют собой палиндром: 1221или73837
+Цифры соответствуют одному из значений awesome_phrasesмассива
† Для возрастающих последовательностей 0 должно идти после 9, а не перед 1, как в 7890.
‡ Для уменьшающих последовательностей значение 0 должно идти после 1, а не перед 9, как в 3210.


Чужое решение

def is_good(n, awesome):
    return n in awesome or str(n) in "1234567890 9876543210" or str(n) == str(n)[::-1] or int(str(n)[1:]) == 0

def is_interesting(n, awesome):
    if n > 99 and is_good(n, awesome):
        return 2
    if n > 97 and (is_good(n + 1, awesome) or is_good(n + 2, awesome)):
        return 1
    return 0
'''




assert is_interesting(90000,[1337, 256]) == 2
assert is_interesting(3,[1337, 256]) == 0
assert is_interesting(1336,[1337, 256]) == 1
assert is_interesting(1337,[1337, 256]) == 2
assert is_interesting(11208,[1337, 256]) == 0
assert is_interesting(11209,[1337, 256]) == 1
assert is_interesting(11211,[1337, 256]) == 2
assert is_interesting(1111,[1337, 256]) == 2
assert is_interesting(6789,[1337, 256]) == 2
assert is_interesting(7890,[1337, 256]) == 2
assert is_interesting(3210,[1337, 256]) == 2
assert is_interesting(4321,[1337, 256]) == 2
assert is_interesting(98,[1337, 256]) == 1
assert is_interesting(1232,[1337, 256]) == 1


print("OK")
