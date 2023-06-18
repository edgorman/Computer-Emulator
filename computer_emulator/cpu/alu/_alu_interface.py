from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Union

from abc import ABC, abstractmethod


class ALUInterface(ABC):
    
    @abstractmethod
    def add(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        """perform an addition operation, returning the result, carry, zero flag, negative flat, overflow flag"""

    @abstractmethod
    def subtract(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        """perform a subtraction operation, returning the result, carry, zero flag, negative flat, overflow flag"""

    @abstractmethod
    def multiply(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        """perform an multiplication operation, returning the result, carry, zero flag, negative flat, overflow flag"""

    @abstractmethod
    def divide(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        """perform a division operation, returning the result, carry, zero flag, negative flat, overflow flag"""
