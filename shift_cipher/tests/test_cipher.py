from ShiftCipher import ShiftCipher
import pytest

# util for testing that mimics shifting
def shift_char(c, shift):
    if not c.isalpha():
        return c
    if c.islower():
        a,z = 'a','z'
    else: a,z = 'A','Z'

    v = ord(c) + shift%26
    if v <= ord(z):
        return chr(v)
    else:
        ov = (v - ord(z)) % 26
        return chr(ord(a) + (ov-1))

# @pytest.mark.skip
def test_wrap_util ():
    assert 'z' == shift_char('y', 1)
    assert 'a' == shift_char('z', 1)
    assert 'a' == shift_char('y', 2)
    assert 'b' == shift_char('y', 3)
    assert 'z' == shift_char('a', 25)
    assert 'a' == shift_char('a', 26)
    assert 'Z' == shift_char('Y', 1)
    assert 'A' == shift_char('Z', 1)
    assert 'a' == shift_char('a', 52)
    assert 'b' == shift_char('a', 26 * 4 + 1)
    assert ' ' == shift_char(' ', 212)
    assert '*' == shift_char('*', 3)
    assert '.' == shift_char('.', 5)
    assert 'z' == shift_char('d', 22)
    assert 'z' == shift_char('d', 48)





# @pytest.mark.skip
def test_lower ():
    c = ShiftCipher(1)
    r = c.encode('abc')
    assert 'bcd' == r


    r = c.encode('abc xyz')
    assert 'bcd yza' == r

    e = ''.join(map(lambda c: shift_char(c, 1), 'abc xyz'))
    assert e == r

    c = ShiftCipher(10)
    r = c.encode('abc xyz')
    e = ''.join(map(lambda c: shift_char(c, 10), 'abc xyz'))
    assert e == r

# @pytest.mark.skip
def test_upper ():
    c = ShiftCipher(1)
    r = c.encode('ABC XYZ')
    assert 'BCD YZA' == r

    c = ShiftCipher(2)
    r = c.encode('ABC XYZ')
    assert 'CDE ZAB' == r

    c = ShiftCipher(5)
    r = c.encode('ABC XYZ!#  Q38')
    e = ''.join(map(lambda c: shift_char(c, 5), 'ABC XYZ!#  Q38'))
    assert e == r

# @pytest.mark.skip
def test_mixed ():
    c = ShiftCipher(19)
    r = c.encode('This is a test!')
    e = ''.join(map(lambda c: shift_char(c, 19), 'This is a test!'))
    assert e == r

    c = ShiftCipher(48)
    r = c.encode('The cost of the nuclear codes will be 5 Million Rubles.  Putin can afford this, no problem.')
    e = ''.join(map(lambda c: shift_char(c, 48), 'The cost of the nuclear codes will be 5 Million Rubles.  Putin can afford this, no problem.'))
    assert e == r

def test_decode_simple ():
    c = ShiftCipher(1)
    msg = 'abc'
    assert msg == c.decode(c.encode(msg))
    msg = 'xx zz'
    assert msg == c.decode(c.encode(msg))
    c = ShiftCipher(34)
    msg = 'A 12 KKIZ QRS'
    assert msg == c.decode(c.encode(msg))

def test_decode_mixed ():
    c = ShiftCipher(14)
    msg = 'The quick red fox jumped over the lazy brown dog.'
    assert msg == c.decode(c.encode(msg))
    c = ShiftCipher(39)
    msg = "It's alright ma.  I'm only bleeding. Ho Ho Ho!"
    assert msg == c.decode(c.encode(msg))


