'''
Helpers to convert base10 integers to an immediate of a
certain type and return their binary string.
'''


def twos_compliment(n, width):
    if n < 0:
        n = (1 << width) + n
    # returns `width` no. of bits
    return f'{n:0{width}b}'


# TODO: Refactor these into single method.
def imm_12(n):
    'signed 12 bit immediate'
    MAX = 0b011111111111
    MIN = -0b100000000000
    assert n >= MIN and n <= MAX, f"{n} doesn't fit signed 12bit"
    res = twos_compliment(n, 12)
    assert len(res) == 12
    return res


def imm_13_effective(n):
    'signed even 12 bit immediate'
    # Last bit is ignored and always zero.
    MAX = 0b0111111111110
    MIN = -0b1000000000000
    assert n >= MIN and n <= MAX, f"{n} doesn't fit signed 13bit"
    res = twos_compliment(n, 13)
    assert len(res) == 13
    assert res[-1] == '0', f'{n} is not a multiple a multiple of 2.'
    return res[:-1]


def imm_20(n):
    'signed 20 bit immediate'
    MAX = 0b01111111111111111111
    MIN = -0b10000000000000000000
    assert n >= MIN and n <= MAX, f"{n} doesn't fit signed 20bit"
    res = twos_compliment(n, 20)
    assert len(res) == 20
    return res


def imm_21_effective(n):
    'signed even 20 bit immediate'
    MAX = 0b011111111111111111110
    MIN = -0b100000000000000000000
    assert n >= MIN and n <= MAX, f"{n} doesn't fit signed 20bit"
    res = twos_compliment(n, 21)
    assert len(res) == 21
    assert res[-1] == '0', f'{n} is not a multiple a multiple of 2.'
    return res
