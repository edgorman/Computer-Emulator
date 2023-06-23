from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Union

from abc import ABC, abstractmethod


class ALUInterface(ABC):

    @abstractmethod
    def get_operation(self, x: bytes) -> function:
        """get the operation function from the opcode reference"""
    
    @abstractmethod
    def add(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        """perform an addition operation, returning the result, carry, zero flag, negative flag, overflow flag"""

    @abstractmethod
    def increment(self, x: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        """perform an increment operation, returning the result, carry, zero flag, negative flag, overflow flag"""

    @abstractmethod
    def decrement(self, x: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        """perform a decrement operation, returning the result, carry, zero flag, negative flag, overflow flag"""

    @abstractmethod
    def subtract(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        """perform a subtraction operation, returning the result, carry, zero flag, negative flag, overflow flag"""

    @abstractmethod
    def multiply(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        """perform an multiplication operation, returning the result, carry, zero flag, negative flag, overflow flag"""

    @abstractmethod
    def divide(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        """perform a division operation, returning the result, carry, zero flag, negative flag, overflow flag"""

    @abstractmethod
    def and_(self, x: bytes, y: bytes) -> bytes:
        """perform an and operation, returning the result"""
    
    @abstractmethod
    def or_(self, x: bytes, y: bytes) -> bytes:
        """perform an or operation, returning the result"""
    
    @abstractmethod
    def not_(self, x: bytes) -> bytes:
        """perform a not operation, returning the result"""

    @abstractmethod
    def nand_(self, x: bytes, y: bytes) -> bytes:
        """perform a nand operation, returning the result"""

    @abstractmethod
    def nor_(self, x: bytes, y: bytes) -> bytes:
        """perform a nor operation, returning the result"""

    @abstractmethod
    def xor_(self, x: bytes, y: bytes) -> bytes:
        """perform a xor operation, returning the result"""
