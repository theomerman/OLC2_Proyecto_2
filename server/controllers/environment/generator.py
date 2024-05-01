
class Generator:
    def __init__(self):

        self.data = [".data\nnext_line: .string \"\\n\"\n"]
        self.text = [".text\n"]
        self.code = ["_start:\n"]
        self.footer = ["\tli a7, 10\n\tecall\n"]
        self.target = "code"
        self.labels = []
        self.base = 0
        self.offset = -1000#-100
        self.string_counter = 0
        self.float_counter = 0
        self.label_counter = 0
        self.label_queue = []

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
        for label in self.labels:
            full_code += label
        return full_code

    def add_data(self, ctx, stringid=""):
        self.data.append(f"str{self.string_counter}: .string \"{ctx}\"\n")
        self.string_counter =+ 1


    def add_label(self, label):
        self.code.append(f"{label}:\n")
    def add_fsw(self, register, base):
        fsw = f"\tfsw {register}, {self.offset}({base})\n"
        self.code.append(fsw)
    def add_flw(self, register, label, temporal):
        flw = f"\tflw {register}, {label},{temporal}\n"
        self.code.append(flw)
    # def add_flw(self, register, base):
    #     flw = f"\tflw {register}, {self.offset}({base})"
    def add_la(self, register, base):
        la = f"\tla {register}, {base}\n"
        arr = self.code if self.target == "code" else self.labels
        arr.append(la)
        # self.code.append(la)
    def add_li(self, register, value):
        li = f"\tli {register}, {value}\n"
        arr = self.code if self.target == "code" else self.labels
        arr.append(li)
        # self.code.append(li)
    def add_sw(self, register, offset, base):
        sw = f"\tsw {register}, {offset}({base})\n"
        arr = self.code if self.target == "code" else self.labels
        arr.append(sw)
        # self.code.append(sw)
    def add_lw(self, register, offset, base):
        lw = f"\tlw {register}, {offset}({base})\n"
        arr = self.code if self.target == "code" else self.labels
        arr.append(lw)
        # self.code.append(lw)
    def add_ecall(self):
        arr = self.code if self.target == "code" else self.labels
        arr.append("\tecall\n")
        # self.code.append("\tecall\n")
    # def add_print(self , base):
    #     self.add_li("t0", base)
    #     self.add_lw("a0", self.offset, "t0")
    #     self.add_li("a7", 1)
    #     self.add_ecall()
    def add_print(self , base):
        arr = self.code if self.target == "code" else self.labels
        arr.append(f"\tli t0, {base}\n")
        arr.append(f"\tlw a0, {self.offset}(t0)\n")
        arr.append(f"\tli a7, 1\n")
        arr.append(f"\tecall\n")
    # def add_print_string(self, base):
    #     self.add_la("a0", base)
    #     self.add_li("a7", 4)
    #     self.add_ecall()
    def add_print_string(self, base): # nuevo
        arr = self.code if self.target == "code" else self.labels
        arr.append(f"\tla a0, {base}\n")
        arr.append(f"\tli a7, 4\n")
        arr.append(f"\tecall\n")
    def add_print_float(self, base):
        try:
            base = int(base)
            self.add_li("t1", base)
            # self.add_flw("fa0", self.offset, "t1")
            self.code.append(f"\tflw fa0, {self.offset}(t1)\n")
        except:
            self.add_flw("fa0", base, "t3")

        self.add_li("a7", 2)
        self.add_ecall()
    def get_base(self):
        return str(self.base)

