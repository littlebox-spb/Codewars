def duplicate_count(text):
    count=set()
    text = text.lower()
    for i in text:
        if text.count(i)>1:
            count.add(i)
    return len(count)

assert duplicate_count("abcde") == 0
assert duplicate_count("") == 0
assert duplicate_count("abcdeaa") == 1
assert duplicate_count("abcdeaB") == 2
assert duplicate_count("Indivisibilities") == 2

print("OK!")