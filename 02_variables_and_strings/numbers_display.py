# Given a floating point number as a string, change its display from the US format to the RO format
# For example '1,000.5' should be `1.000,5`


def us_to_ro_number(nr_as_string: str) -> str:
    raise Exception('Implement me!')
    return ''


def test():
    assert '10' == us_to_ro_number('10')
    assert '10,5' == us_to_ro_number('10.5')
    assert '1.000,5' == us_to_ro_number('1,000.5')
    assert '1.000.000' == us_to_ro_number('1,000,000')
    print('All tests passed!')


test()
