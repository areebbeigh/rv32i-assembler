from lexer import instructions


class CodeGenerator:

    def register_bin(self, r):
        r = int(r[1:])
        return f'{r:05b}'

    def type_r(self, node):
        'func7 rs2 rs1 func3 rd opcode'
        instr = node['instr']
        opcode = instructions.get_opcode(instr)
        rd = self.register_bin(node['rd'])
        func3 = instructions.get_func3(instr)
        rs1 = self.register_bin(node['rs1'])
        rs2 = self.register_bin(node['rs2'])
        func7 = instructions.get_func7(instr)
        return f'{func7}{rs2}{rs1}{func3}{rd}{opcode}'

    def type_i(self, node):
        'imm[11:0] rs1 func3 rd opcode'
        instr = node['instr']
        opcode = instructions.get_opcode(instr)
        rd = self.register_bin(node['rd'])
        func3 = instructions.get_func3(instr)
        rs1 = self.register_bin(node['rs1'])
        imm = node['imm']
        assert len(imm) == 12
        return f'{imm}{rs1}{func3}{rd}{opcode}'

    def type_sb(self, node):
        'imm[12] imm[10:5] rs2 rs1 func3 imm[4:1] imm[11] opcode'
        instr = node['instr']
        opcode = instructions.get_opcode(instr)
        imm = node['imm']
        imm_11 = imm[-12]
        imm_4_1 = imm[-4:]
        imm_10_5 = imm[-10:-4]
        imm_12 = imm[-12]
        func3 = instructions.get_func3(instr)
        rs1 = self.register_bin(node['rs1'])
        rs2 = self.register_bin(node['rs2'])
        return f'{imm_12}{imm_10_5}{rs2}{rs1}{func3}{imm_4_1}{imm_11}{opcode}'

    def instr_lui(self, node):
        'imm[31:12] rd opcode'
        instr = node['instr']
        opcode = instructions.get_opcode(instr)
        rd = self.register_bin(node['rd'])
        imm = node['imm']
        return f'{imm}{rd}{opcode}'

    def instr_auipc(self, node):
        'imm[31:12] rd opcode'
        instr = node['instr']
        opcode = instructions.get(instr)
        rd = self.register_bin(node['rd'])
        imm = node['imm']
        return f'{imm}{rd}{opcode}'

    def instr_jal(self, node):
        'imm[20] imm[10:1] imm[11] imm[19:12] rd opcode'
        instr = node['instr']
        opcode = instructions.get_opcode(instr)
        rd = self.register_bin(node['rd'])
        imm = node['imm']
        imm_19_12 = node[-19:-11]
        imm_11 = node[-11]
        imm_10_1 = node[-10:]
        imm_20 = node[-20]
        return f'{imm_20}{imm_10_1}{imm_11}{imm_19_12}{rd}{opcode}'

    def write_binstr(self, node, stream):
        'Translate node and write to stream'
        res = None
        # print(node)
        if node['type'] == 'r':
            res = self.type_r(node)
        if node['type'] == 'i':
            res = self.type_i(node)
        if node['type'] == 'sb':
            res = self.type_sb(node)
        if node['instr'] == 'lui':
            res = self.instr_lui(node)
        if node['instr'] == 'auipc':
            self.instr_auipc(node)
        if node['instr'] == 'jal':
            self.instr_jal(node)

        if res is None:
            raise NotImplementedError('Instruction not supported yet')
        stream.write(res)
        # print(node, res)
