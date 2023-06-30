from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Union

from enum import Enum


class RISCInstructionEnum(Enum):
    """the instruction formats for RISC-V architecture"""

    REGISTER = 0        # register to register
    IMMEDIATE = 1       # immediate (and load)
    STORE = 2           # store in register
    BRANCH = 3          # branch to address
    UPPER = 4           # upper immediate (and load)
    JUMP = 5            # jump to address


class RISCInstruction:

    def __init__(self, data: bytes) -> None:
        self.__data = data

        type_, operation, args = self._decode_instruction()
        
        self.__type = type_
        self.__operation = operation
        self.__args = args

    
    def _decode_instruction(self) -> Union[RISCInstructionEnum, function, dict]:
        # Determine the instruction type
        ...
