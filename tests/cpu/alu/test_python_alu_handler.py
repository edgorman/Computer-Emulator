from types import ModuleType

import pytest

from computer_emulator.cpu.alu._alu_interface import ALUInterface


@pytest.mark.parametrize(
    "int_operand1, int_operand2, int_expected_output, int_expected_carry, bool_expected_zero, bool_expected_negative, bool_expected_overflow", 
    [
        (0, 0, 0, 0, True, False, False),
        (0, 1, 1, 0, False, False, False),
        (1, 1, 2, 0, False, False, False),
        (32766, 1, 0, 1, True, False, True),
        (32766, 32766, 32765, 1, False, False, True),
        (-1, -1, -2, 0, False, True, False),
        (-32767, -1, 0, 1, True, False, True),
        (-32767, -32767, -32766, 1, False, True, True)
    ]
)
def test_signed_addition(
    signed_python_alu_handler: ALUInterface,
    signed_alu_config: ModuleType,
    int_operand1: int,
    int_operand2: int,
    int_expected_output: int,
    int_expected_carry: int,
    bool_expected_zero: bool,
    bool_expected_negative: bool,
    bool_expected_overflow: bool
):
    bin_operand1 = int_operand1.to_bytes(signed_alu_config.BIT_LENGTH, signed_alu_config.BIT_ENDIAN, signed=signed_alu_config.BIT_SIGNED)
    bin_operand2 = int_operand2.to_bytes(signed_alu_config.BIT_LENGTH, signed_alu_config.BIT_ENDIAN, signed=signed_alu_config.BIT_SIGNED)
    bin_expected_output = int_expected_output.to_bytes(signed_alu_config.BIT_LENGTH, signed_alu_config.BIT_ENDIAN, signed=signed_alu_config.BIT_SIGNED)
    bin_expected_carry = int_expected_carry.to_bytes(signed_alu_config.BIT_LENGTH, signed_alu_config.BIT_ENDIAN, signed=signed_alu_config.BIT_SIGNED)

    bin_output, bin_carry, bool_zero, bool_negative, bool_overflow = signed_python_alu_handler.add(
        bin_operand1, bin_operand2
    )
    assert bin_output == bin_expected_output
    assert bin_carry == bin_expected_carry
    assert bool_zero == bool_expected_zero
    assert bool_negative == bool_expected_negative
    assert bool_overflow == bool_expected_overflow


@pytest.mark.parametrize(
    "int_operand1, int_operand2, int_expected_output, int_expected_carry, bool_expected_zero, bool_expected_negative, bool_expected_overflow", 
    [
        (0, 0, 0, 0, True, False, False),
        (0, 1, 1, 0, False, False, False),
        (1, 1, 2, 0, False, False, False),
        (65534, 1, 0, 1, True, False, True),
        (65534, 65534, 65533, 1, False, False, True),
    ]
)
def test_unsigned_addition(
    unsigned_python_alu_handler: ALUInterface,
    unsigned_alu_config: ModuleType,
    int_operand1: int,
    int_operand2: int,
    int_expected_output: int,
    int_expected_carry: int,
    bool_expected_zero: bool,
    bool_expected_negative: bool,
    bool_expected_overflow: bool
):
    bin_operand1 = int_operand1.to_bytes(unsigned_alu_config.BIT_LENGTH, unsigned_alu_config.BIT_ENDIAN, signed=unsigned_alu_config.BIT_SIGNED)
    bin_operand2 = int_operand2.to_bytes(unsigned_alu_config.BIT_LENGTH, unsigned_alu_config.BIT_ENDIAN, signed=unsigned_alu_config.BIT_SIGNED)
    bin_expected_output = int_expected_output.to_bytes(unsigned_alu_config.BIT_LENGTH, unsigned_alu_config.BIT_ENDIAN, signed=unsigned_alu_config.BIT_SIGNED)
    bin_expected_carry = int_expected_carry.to_bytes(unsigned_alu_config.BIT_LENGTH, unsigned_alu_config.BIT_ENDIAN, signed=unsigned_alu_config.BIT_SIGNED)

    bin_output, bin_carry, bool_zero, bool_negative, bool_overflow = unsigned_python_alu_handler.add(
        bin_operand1, bin_operand2
    )
    assert bin_output == bin_expected_output
    assert bin_carry == bin_expected_carry
    assert bool_zero == bool_expected_zero
    assert bool_negative == bool_expected_negative
    assert bool_overflow == bool_expected_overflow
