# Given a sentence, capitalize the first letter and add a dot at the end


def add_punctuation(sentence: str) -> str:
    r = sentence.capitalize() + '.'
    return r


def test():
    assert 'A word.' == add_punctuation('a word')
    assert 'Some other sentence.' == add_punctuation('some other sentence')
    assert '.' == add_punctuation('')
    assert 'B.' == add_punctuation('b')
    print('All tests passed!')


test()
