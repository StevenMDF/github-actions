def capitalize_string(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.capitalize()


def test_capitalize_string():
    assert capitalize_string('test') == 'Test'


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
