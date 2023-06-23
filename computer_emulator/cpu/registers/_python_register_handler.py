from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from types import ModuleType

from ._registers_interface import RegistersInterface, StaticRegisterEnum


class PythonRegisterHandler(RegistersInterface):

    def __init__(self, config: ModuleType) -> None:
        self.__register_count = config.REGISTER_COUNT
        self.__register_size = config.BIT_LENGTH // 8

        # Check that there are enough registers
        if self.__register_size < len(StaticRegisterEnum):
            raise ValueError(f"The register does not have enough indexes to store static registers")

        # Instantiate all registers with zero byte values
        self.__registers = [bytes(self.__register_size)] * self.__register_count

    def store_index(self, value: bytes, register_index: int) -> None:
        # Check that the value can be stored in the register
        if len(value) != self.__register_size:
            raise ValueError(f"The register cannot store values of size {len(value)} bytes")

        self.__registers[register_index] = value

    def read_index(self, register_index: int) -> bytes:
        # Check the the index is within the expected range
        if register_index < 0 or register_index >= self.__register_count:
            raise IndexError(f"The register cannot access a value as index position {register_index}")
        
        return self.__registers[register_index]
