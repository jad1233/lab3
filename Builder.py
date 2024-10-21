class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f'Computer [CPU: {self.cpu}, GPU: {self.gpu}, RAM: {self.ram}, Storage: {self.storage}]'

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer

# Usage
builder = ComputerBuilder()
computer = (builder.set_cpu("Intel i7")
                  .set_gpu("NVIDIA RTX 3080")
                  .set_ram("32GB")
                  .set_storage("1TB SSD")
                  .build())
print(computer)
