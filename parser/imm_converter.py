'''
Helpers to convert base10 integers to an immediate of a
certain type and return their binary string.
'''

def twos_compliment(n, width):
    if n < 0:
        n = (1 << width) + n
    return f'{n:0{width}b}'


def imm_type_i(n):
    'signed 12 bit immediate'
    MAX = 0b011111111111
    MIN = -0b100000000000
    assert n >= MIN and n <= MAX, f"{n} doesn't fit signed 12bit"
    res = twos_compliment(n, 12)
    assert len(res) == 12
    return res

def imm_type_sb(n):
    pass

def imm_type_ui(n):
    pass

def imm_type_uj(n):
    pass