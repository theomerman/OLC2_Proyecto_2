
from icecream import ic


class Generator:
    def __init__(self):

        self.data = [".data\nnext_line: .string \"\\n\"\n"]
        self.data.append("true: .string \"true\"\n")
        self.data.append("false: .string \"false\"\n")
        self.data.append(f"null: .string \"null\"\n")
        self.data.append(f"bracketL: .string \"[\"\n")
        self.data.append(f"bracketR: .string \"]\"\n")
        self.data.append(f"comma: .string \",\"\n")
        self.data.append(f"space: .string \" \"\n")
        self.text = [".text\n"]
        self.code = []
        self.footer = ["\tli a7, 10\n\tecall\n"]
        self.target = "code" #useless
        self.labels = []
        self.base = 0
        self.offset = -1000#-100
        self.string_counter = 0
        self.float_counter = 0
        self.label_counter = 0
        self.word_counter = 0
        self.label_queue = []

        self.label_queue.insert(0, ["_start:\n"])
        self.break_stack = []

    def get_full_code(self):
        full_code = ""
        for data in self.data:
            full_code += data
        for text in self.text:
            full_code += text

        for code in self.code:
            full_code += code

        for label in self.label_queue:
            for l in label:
                full_code += l

        for footer in self.footer:
            full_code += footer

        for label in self.labels:
            full_code += label
        return full_code

    def add_label_to_code(self):
        try:
            self.code = self.code + self.label_queue[0]
            self.label_queue[0].pop(0)
        except IndexError as e:
            ic(e)

    def add_data(self, ctx, stringid=""):
        self.data.append(f"str{self.string_counter}: .string \"{ctx}\"\n")
        self.string_counter =+ 1


    def add_label(self, label):
        self.code.append(f"{label}:\n")
    def add_fsw(self, register, base):
        fsw = f"\tfsw {register}, {self.offset}({base})\n"
        self.label_queue[0].append(fsw)
    def add_flw(self, register, label, temporal):
        flw = f"\tflw {register}, {label},{temporal}\n"
        self.label_queue[0].append(flw)
    def add_flw(self, register, base):
        flw = f"\tflw {register}, {self.offset}({base})"
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
            # self.add_li("t1", base)
            self.label_queue[0].append(f"\tli t1, {base}\n")
            # self.add_flw("fa0", self.offset, "t1")
            self.label_queue[0].append(f"\tflw fa0, {self.offset}(t1)\n")
        except:
            # self.add_flw("fa0", base, "t3")
            self.label_queue[0].append(f"\tflw fa0, {base}, t3\n")

        # self.add_li("a7", 2)
        # self.add_ecall()
        self.label_queue[0].append(f"\tli a7, 2\n")
        self.label_queue[0].append(f"\tecall\n")
    def get_base(self):
        return str(self.base)
    def get_offset(self):
        return str(self.offset)
    def get_label_counter(self):
        return str(self.label_counter)


