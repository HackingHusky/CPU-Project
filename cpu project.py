# project on cpu sending instructions to intital memory bus 

class CPU:
    def __init__(self):
        self.instructions = []
    
    def send_instruction(self, instruction):
        self.instructions.append(instruction)
        print(f"CPU received instruction: {instruction}")

class MemoryBus:
    def __init__(self):
        self.memory = {}
    
    def set_value(self, address, value):
        self.memory[address] = value
        print(f"MemoryBus set value at address {address}: {value}")

# Initialize CPU and MemoryBus
cpu = CPU()
memory_bus = MemoryBus()

# Send instructions to CPU
cpu.send_instruction("LOAD A, 0x01")
cpu.send_instruction("STORE A, 0x02")
cpu.send_instruction("ADD A, B")
cpu.send_instruction("HALT")

# Set initial memory values
memory_bus.set_value(0x01, 42)
memory_bus.set_value(0x02, 84)

# Print the current state of CPU and MemoryBus
print("\nCPU Instructions:")
for instruction in cpu.instructions:
    print(instruction)

print("\nMemoryBus Values:")
for address, value in memory_bus.memory.items():
    print(f"Address {hex(address)}: {value}")
