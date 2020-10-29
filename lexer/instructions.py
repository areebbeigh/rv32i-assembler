# https://metalcode.eu/2019-12-06-rv32i.html

# R type
ADD = 'add'
SUB = 'sub'
AND = 'and'
OR = 'or'
XOR = 'xor'
# SLT = 'slt'
# SLTU = 'sltu'
SLL = 'sll'
SRL = 'srl'
SRA = 'sra'

# I type
ADDI = 'addi'
ANDI = 'andi'
ORI = 'ori'
XORI = 'xori'
# SLTI = 'slti'
SLLI = 'slli'
SRLI = 'srli'
SRAI = 'srai'

# SB type
BEQ = 'beq'
BNE = 'bne'
BLT = 'blt'
BGE = 'bge'
BLTU = 'bltu'
BGEU = 'bgeu'

# UI type
LUI = 'lui'
AUIPC = 'auipc'

# UJ type
JAL = 'jal'

# IJ type
# JALR = 'jalr'

# Load and store
# ...
# Memory ordering
# ...

TYPE_R = (ADD, SUB, AND, OR, XOR, SLL, SRL, SRA, )
TYPE_I = (ADDI, ANDI, ORI, XORI, SLLI, SRLI, SRAI, )
TYPE_SB = (BEQ, BNE, BLT, BGE, BLTU, BGEU, )
TYPE_UI = (LUI, AUIPC, )
TYPE_UJ = (JAL, )

INSTR_ALL = set(TYPE_R + TYPE_I + TYPE_SB + TYPE_UI + TYPE_UJ)


def is_instr(instr):
    return instr in INSTR_ALL


# Binary opcodes
OP_ARITH = '0110011'
OP_AIRTHI = '0010011'
OP_BRANCH = '1100011'
OP_LUI = '0110111'
OP_AUIPC = '0010111'
OP_JAL = '1101111'
# OP_JALR = '1100111'
# OP_LOAD = 0000011
# OP_STORE = 0100011


def get_opcode(instr):
    if instr in TYPE_R:
        return OP_ARITH
    if instr in TYPE_I:
        return OP_AIRTHI
    if instr in TYPE_SB:
        return OP_BRANCH
    if instr == LUI:
        return OP_LUI
    if instr == AUIPC:
        return OP_AUIPC
    if instr == JAL:
        return OP_JAL
    raise Exception('Instruction not implemented')


# FUNC3
FUNC3_ARITH = {
    ADD: '000',
    SUB: '000',
    SLL: '001',
    # SLT: '010',
    # SLTU: '011',
    XOR: '100',
    SRL: '101',
    SRA: '101',
    OR: '110',
    AND: '111',
}

FUNC3_ARITHI = {
    ADDI: '000',
    # SLTI: '010',
    # SLTU: '011',
    XORI: '100',
    ORI: '110',
    ANDI: '111',
    SLLI: '001',
    SRLI: '101',
    SRAI: '101',
}

FUNC3_BRANCH = {
    BEQ: '000',
    BNE: '001',
    BLT: '100',
    BGE: '101',
    BLTU: '110',
    BGEU: '111',
}

# FUNC3_LOAD = {...}
# FUNC3_STORE = {...}


def get_func3(instr):
    if instr in TYPE_R:
        return FUNC3_ARITH[instr]
    if instr in TYPE_I:
        return FUNC3_ARITHI[instr]
    if instr in TYPE_SB:
        return FUNC3_BRANCH[instr]
    raise Exception('Instruction not implemented')


# FUNC7
FUNC7_ARITH = {
    ADD: '0000000',
    SUB: '0100000',
    SLL: '0000000',
    # SLT: '0000000',
    # SLTU: '0000000',
    XOR: '0000000',
    SRL: '0000000',
    SRA: '0100000',
    OR: '0000000',
    AND: '0000000',
}
