from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from types import ModuleType
    from typing import Union

from ._alu_interface import ALUInterface


class PythonALUHandler(ALUInterface):

    def __init__(self, config: ModuleType) -> None:
        self.__bit_endian = config.BIT_ENDIAN
        self.__bit_length = config.BIT_LENGTH
        self.__bit_signed = config.BIT_SIGNED

        # Calculate the maximum and minimum integer values (inclusive)
        # given the number of bits and whether they are signed
        self.__max_value = 2**self.__bit_length - 1
        self.__min_value = 0
        if self.__bit_signed:
            self.__max_value = 2**(self.__bit_length - 1) - 1
            self.__min_value = -2**(self.__bit_length - 1)
        
    def _int_to_bytes(self, x: int) -> bytes:
        return int.to_bytes(x, self.__bit_length, self.__bit_endian, signed=self.__bit_signed)

    def _bool_to_bytes(self, x: bool) -> bytes:
        return bool.to_bytes(x, self.__bit_length, self.__bit_endian, signed=self.__bit_signed)

    def _bytes_to_bool(self, x: bytes) -> bool:
        return bool.from_bytes(x, self.__bit_endian, signed=self.__bit_signed)

    def _bytes_to_int(self, x: bytes) -> int:
        return int.from_bytes(x, self.__bit_endian, signed=self.__bit_signed)

    def _execute_arithmetic(
        self, 
        x: bytes, 
        y: bytes, 
        operator: function
    ) -> Union[bytes, bytes, bool, bool, bool]:
        # Perform arithmetic operation
        int_x = self._bytes_to_int(x)
        int_y = self._bytes_to_int(y)
        int_result = operator(int_x, int_y)

        # Divisor depends on which max/min result is closer to
        divisor = self.__max_value
        if int_result < 0:
            divisor = self.__min_value

        # Calculate the output and carry values
        int_output = int_result % divisor
        int_carry = int_result // divisor

        # Handle negative output values
        if not self.__bit_signed and int_output < 0:
            raise ArithmeticError(f"The ALU does not support negative numbers: {int_output}")

        # Calculate output from operation
        bin_output = self._int_to_bytes(int_output)
        bin_carry = self._int_to_bytes(int_carry)
        bool_zero = bool(int_output == 0)
        bool_negative = bool(int_output < 0)
        bool_overflow = int_result >= self.__max_value or (self.__bit_signed and int_result <= self.__min_value)

        return bin_output, bin_carry, bool_zero, bool_negative, bool_overflow

    def _execute_logic(
        self, 
        x: bytes, 
        y: bytes, 
        operator: function
    ) -> bytes:
        # Perform logical operation
        bool_x = self._bytes_to_bool(x)
        bool_y = self._bytes_to_bool(y)
        bool_result = operator(bool_x, bool_y)

        # Calculate output from operation
        bin_output = self._bool_to_bytes(bool_result)
        return bin_output

    def add(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        operator = lambda x, y: x + y
        return self._execute_arithmetic(x, y, operator)
    
    def increment(self, x: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        operator = lambda x, y: x + y
        return self._execute_arithmetic(x, self._int_to_bytes(1), operator)

    def decrement(self, x: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        operator = lambda x, y: x + y
        return self._execute_arithmetic(x, self._int_to_bytes(-1), operator)

    def subtract(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        operator = lambda x, y: x - y
        return self._execute_arithmetic(x, y, operator)

    def multiply(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        operator = lambda x, y: x * y
        return self._execute_arithmetic(x, y, operator)

    def divide(self, x: bytes, y: bytes) -> Union[bytes, bytes, bool, bool, bool]:
        operator = lambda x, y: x / y
        return self._execute_arithmetic(x, y, operator)

    def and_(self, x: bytes, y: bytes) -> bytes:
        operator = lambda x, y: x and y
        return self._execute_logic(x, y, operator)
    
    def or_(self, x: bytes, y: bytes) -> bytes:
        operator = lambda x, y: x or y
        return self._execute_logic(x, y, operator)
    
    def not_(self, x: bytes) -> bytes:
        operator = lambda x, y: not x
        return self._execute_logic(x, self._bool_to_bytes(False), operator)

    def nand_(self, x: bytes, y: bytes) -> bytes:
        operator = lambda x, y: not(x and y)
        return self._execute_logic(x, y, operator)

    def nor_(self, x: bytes, y: bytes) -> bytes:
        operator = lambda x, y: not(x or y)
        return self._execute_logic(x, y, operator)

    def xor_(self, x: bytes, y: bytes) -> bytes:
        operator = lambda x, y: (x or y) and not(x and y)
        return self._execute_logic(x, y, operator)
