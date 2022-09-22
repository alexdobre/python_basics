# Given two words, decide if the two are anagrams of each other
# Two words are anagrams if they contain the exact same letters only in different orders


def are_anagrams(str1: str, str2: str) -> bool:
    raise Exception('Implement me!')
    return ''


def test():
    assert are_anagrams('Dog', 'God')
    assert are_anagrams('aRc', 'caR')
    assert are_anagrams('state', 'taste')
    assert not are_anagrams('state', 'tastes')
    assert not are_anagrams('x', 'y')
    print('All tests passed!')


test()
