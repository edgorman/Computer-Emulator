from unittest import mock

import pytest

from computer_emulator.cpu.alu._alu_interface import ALUInterface
from computer_emulator.cpu.cu._python_cu_handler import PythonCUHandler
from computer_emulator.cpu.registers._registers_interface import RegistersInterface
from computer_emulator.memory._memory_interface import MemoryInterface


@pytest.fixture()
def cu_config():
    return mock.Mock(
        MODE_LENGTH=3,
        OPCODE_LENGTH=4,
        OPERAND_LENGTH=9
    )


@pytest.fixture()
def alu_mock():
    return mock.Mock(spec=ALUInterface)


@pytest.fixture()
def memory_mock():
    return mock.Mock(spec=MemoryInterface)


@pytest.fixture()
def registers_mock():
    return mock.Mock(spec=RegistersInterface)


@pytest.fixture()
def python_register_handler(cu_config, alu_mock, memory_mock, registers_mock):
    return PythonCUHandler(cu_config, alu_mock, memory_mock, registers_mock)
