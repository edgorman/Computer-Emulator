from abc import ABC, abstractmethod
from enum import Enum


class StaticRegisterEnum(Enum):
    PROGRAM_COUNTER = 0
    ACCUMULATOR = 1


class RegistersInterface(ABC):

    @abstractmethod
    def store_index(self, value: bytes, register_index: int) -> None:
        """store a value at register index"""

    @abstractmethod
    def read_index(self, register_index: int) -> bytes:
        """read a value from register index"""
