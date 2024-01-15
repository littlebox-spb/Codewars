# Перед вставкой сотри все, что ниже этого текста!!


def persistence(n):
    count = 0
    while True:
        if len(str(n)) == 1:
            return count
        dig = str(n)
        n = 1
        for i in dig:
            n *= int(i)
        count += 1


assert (
    persistence(39) == 3
)  # because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit
assert persistence(4) == 0
assert persistence(25) == 2
assert persistence(999) == 4

print("OK!")
