from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from types import ModuleType

from ._registers_interface import RegistersInterface


class PythonRegisterHandler(RegistersInterface):

    def __init__(self, config: ModuleType) -> None:
        self.__register_count = config.REGISTER_COUNT
        self.__register_size = config.BIT_LENGTH // 8

        # Instantiate all registers with zero byte values
        self.__registers = [bytes(self.__register_size)] * self.__register_count

    def store_value(self, value: bytes, register_index: int) -> None:
        # Check that the value can be stored in the register
        if len(value) != self.__register_size:
            raise ValueError(f"The register cannot store values of size {len(value)} bytes")

        self.__registers[register_index] = value

    def read_value(self, register_index: int) -> bytes:
        # Check the the index is within the expected range
        if register_index < 0 or register_index >= self.__register_count:
            raise IndexError(f"The register cannot access a value as index position {register_index}")
        
        return self.__registers[register_index]
