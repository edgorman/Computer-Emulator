from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from types import ModuleType

import pytest

from computer_emulator.cpu.registers._registers_interface import RegistersInterface


def test_single_store_and_read(
    python_register_handler: RegistersInterface,
    register_config: ModuleType
):
    value = int(1).to_bytes(register_config.BIT_LENGTH // 8, "big")

    # Store and read the value in the register
    python_register_handler.store_value(value, 0)
    expected = python_register_handler.read_value(0)
    assert value == expected

def test_multiple_store_and_read(
    python_register_handler: RegistersInterface,
    register_config: ModuleType
):
    register_dict = {
        k: int(k).to_bytes(register_config.BIT_LENGTH // 8, "big")
        for k in range(register_config.REGISTER_COUNT)
    }

    # Store the values in the register
    for register_index, value in register_dict.items():
        python_register_handler.store_value(value, register_index)

    # Read the values in the register
    for register_index, value in register_dict.items():
        expected = python_register_handler.read_value(register_index)
        assert value == expected

def test_invalid_store_and_read(
        python_register_handler: RegistersInterface,
        register_config: ModuleType
):
    # Test a ValueError is raised when storing an object of invalid size
    with pytest.raises(ValueError):
        value = int(1).to_bytes(int(register_config.BIT_LENGTH * 2) // 8, "big")
        python_register_handler.store_value(value, 0)
    
    with pytest.raises(ValueError):
        value = int(1).to_bytes(int(register_config.BIT_LENGTH / 2) // 8, "big")
        python_register_handler.store_value(value, 0)

    # Test an IndexError is raised when reading an invalid index position
    with pytest.raises(IndexError):
        python_register_handler.read_value(-1)
    
    with pytest.raises(IndexError):
        python_register_handler.read_value(register_config.REGISTER_COUNT)
