def list_position(word):
    """Return the anagram list position of the word"""
    return 1


assert list_position("A") == 1
assert list_position("ABAB") == 2
assert list_position("AAAB") == 1
assert list_position("BAAA") == 4
assert list_position("QUESTION") == 24572
assert list_position("BOOKKEEPER") == 10743
