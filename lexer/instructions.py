# https://metalcode.eu/2019-12-06-rv32i.html

# R type
ADD = 'add'
SUB = 'sub'
AND = 'and'
OR = 'or'
XOR = 'xor'
SLT = 'slt'
SLTU = 'sltu'
SLL = 'sll'
SRL = 'srl'
SRA = 'sra'

# I type
ADDI = 'addi'
ANDI = 'andi'
ORI = 'ori'
XORI = 'xori'
SLTI = 'slti'
SLTIU = 'sltiu'
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

# S type
# Load
LB = 'lb'
LH = 'lh'
LW = 'lw'
LBU = 'lbu'
LHU = 'lhu'

# Store
SB = 'sb'
SH = 'sh'
SW = 'sw'
SBU = 'sbu'
SHU = 'shu'

# Memory ordering
# ...

INSTR_LOAD = (LB, LH, LW, LBU, LHU,)
INSTR_STORE = (SB, SH, SW, SBU, SHU,)

TYPE_R = (ADD, SUB, AND, OR, XOR, SLL, SRL, SRA, SLT, SLTU )
TYPE_I = (ADDI, ANDI, ORI, XORI, SLLI, SRLI, SRAI, SLTI, SLTIU )
TYPE_SB = (BEQ, BNE, BLT, BGE, BLTU, BGEU, )
TYPE_UI = (LUI, AUIPC, )
TYPE_UJ = (JAL, )
TYPE_S = INSTR_LOAD + INSTR_STORE

INSTR_ALL = set(TYPE_R + TYPE_I + TYPE_SB + TYPE_UI + TYPE_UJ + TYPE_S)


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
OP_LOAD = '0000011'
OP_STORE = '0100011'


def get_opcode(instr):
    if instr in TYPE_R:
        return OP_ARITH
    if instr in TYPE_I:
        return OP_AIRTHI
    if instr in TYPE_SB:
        return OP_BRANCH
    if instr in INSTR_LOAD:
        return OP_LOAD
    if instr in INSTR_STORE:
        return OP_STORE
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
    SLT: '010',
    SLTU: '011',
    XOR: '100',
    SRL: '101',
    SRA: '101',
    OR: '110',
    AND: '111',
}

FUNC3_ARITHI = {
    ADDI: '000',
    SLTI: '010',
    SLTIU: '011',
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

FUNC3_LOAD = {
    LB: '000',
    LH: '001',
    LW: '010',
    LBU: '100',
    LHU: '101',
}

FUNC3_STORE = {
    SB: '000',
    SH: '001',
    SW: '010',
    SBU: '100',
    SHU: '101',
}


def get_func3(instr):
    if instr in TYPE_R:
        return FUNC3_ARITH[instr]
    if instr in TYPE_I:
        return FUNC3_ARITHI[instr]
    if instr in TYPE_SB:
        return FUNC3_BRANCH[instr]
    if instr in INSTR_LOAD:
        return FUNC3_LOAD[instr]
    if instr in INSTR_STORE:
        return FUNC3_STORE[instr]
    raise Exception('Instruction not implemented')


# FUNC7
FUNC7_ARITH = {
    ADD: '0000000',
    SUB: '0100000',
    SLL: '0000000',
    SLT: '0000000',
    SLTU: '0000000',
    XOR: '0000000',
    SRL: '0000000',
    SRA: '0100000',
    OR: '0000000',
    AND: '0000000',
}


def get_func7(instr):
    assert instr in TYPE_R, 'Instruction not implemented'
    return FUNC7_ARITH[instr]
