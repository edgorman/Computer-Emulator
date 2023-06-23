from abc import ABC, abstractmethod
from enum import Enum


class AddressingModeEnum(Enum):
    IMPLIED = 0             # implied by type of instruction (e.g. accumulator)
    IMMEDIATE = 1           # described literally in the operand
    REGISTER = 2            # stored directly in the register
    REGISTER_INDIRECT = 3   # stored in a register address that this register address points to
    AUTO_INCREMENT = 4      # increments the register after the operand is read
    AUTO_DECREMENT = 5      # decrements the register after the operand is read
    MEMORY_DIRECT = 6       # stored directly in the memory address
    MEMORY_INDIRECT = 7     # stored in a memory address that this memory address points to


class CUInterface(ABC):

    @abstractmethod
    def run(self) -> None:
        """perform the next operation and execute the required actions"""
