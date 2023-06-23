from abc import ABC, abstractmethod


class MemoryInterface(ABC):

    @abstractmethod
    def store_address(self, value: bytes, address: bytes) -> bytes:
        """store a value at memory address"""

    @abstractmethod
    def read_address(self, address: bytes) -> bytes:
        """read a value from memory address"""
