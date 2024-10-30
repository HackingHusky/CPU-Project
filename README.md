CPU and MemoryBus Simulation
This repository contains a simple simulation of a CPU and MemoryBus in Python. The simulation allows you to send instructions to the CPU and set values in the MemoryBus.

Classes
CPU
The CPU class is responsible for receiving and storing instructions.

Methods:

__init__(): Initializes the CPU with an empty list of instructions.

send_instruction(instruction): Adds an instruction to the CPU and prints a message indicating the received instruction.

MemoryBus
The MemoryBus class is responsible for storing values at specified addresses.

Methods:

__init__(): Initializes the MemoryBus with an empty dictionary to store values.

set_value(address, value): Sets the value at the specified address in the MemoryBus and prints a message indicating the set value.

Usage
Here's an example of how to use the CPU and MemoryBus classes:

python

Copy
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
Output
The output of the example usage will be:


Copy
CPU received instruction: LOAD A, 0x01
CPU received instruction: STORE A, 0x02
CPU received instruction: ADD A, B
CPU received instruction: HALT
MemoryBus set value at address 1: 42
MemoryBus set value at address 2: 84

CPU Instructions:
LOAD A, 0x01
STORE A, 0x02
ADD A, B
HALT

MemoryBus Values:
Address 0x1: 42
Address 0x2: 84
License
