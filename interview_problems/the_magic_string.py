# Given a string, determine if it is valid. If so, return YES, otherwise return NO.
#
# Rule 1 - We consider a string to be valid if all characters of the string appear the same number of times.
# Rule 2 - It is also valid if we can remove just one character at one location in the string,
#          and the remaining characters will occur the same number of times.
#
# For example:
#     * "abcd" is valid because each letter occurs only once.
#     * "aabb" is valid because each letter occurs twice.
#     * "abcc" is valid because we can remove a "c" and the resulting string has all letters occurring only once.
#     * "abbcc" is valid because we can remove the "a" and the resulting string has all letters occurring twice.
#
# We consider a non empty input string made up only of lower case characters.


def is_valid(string: str) -> str:
    raise Exception('Implement me!')
    return 'YES'


def test():
    assert 'YES' == is_valid('a')
    assert 'NO' == is_valid('abbbbc')
    assert 'YES' == is_valid('aaaa')
    assert 'YES' == is_valid('aaaabbb')
    assert 'NO' == is_valid('aaaabbbcccc')
    assert 'YES' == is_valid('abbcc')
    assert 'YES' == is_valid('abc')
    assert 'YES' == is_valid('abcc')
    assert 'NO' == is_valid('aabbcd')
    assert 'NO' == is_valid('aabbccddeefghi')
    assert 'YES' == is_valid('abcdefghhgfedecba')
    print('All tests passed!')


test()