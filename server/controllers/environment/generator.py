
class Generator:
    def __init__(self):

        self.data = [".data\n"]
        self.text = [".text\n"]
        self.code = ["_start:\n"]
        self.footer = ["\tli a7, 10\n\tecall"]
        self.base = 0
        self.offset = -100

    def get_full_code(self):
        full_code = ""
        for data in self.data:
            full_code += data
        for text in self.text:
            full_code += text
        for code in self.code:
            full_code += code
        for footer in self.footer:
            full_code += footer
        return full_code

    def add_li(self, register, value):
        li = f"\tli {register}, {value}\n"
        self.code.append(li)
    def add_sw(self, register, offset, base):
        sw = f"\tsw {register}, {offset}({base})\n"
        self.code.append(sw)
    def add_lw(self, register, offset, base):
        lw = f"\tlw {register}, {offset}({base})\n"
        self.code.append(lw)
    def add_ecall(self):
        self.code.append("\tecall\n")
    def add_print(self , base):
        self.add_li("t0", base)
        self.add_lw("a0", self.offset, "t0")
        self.add_li("a7", 1)
        self.add_ecall()
    def get_base(self):
        return str(self.base)

