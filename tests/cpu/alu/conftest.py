from unittest import mock

import pytest

from computer_emulator.cpu.alu._python_alu_handler import PythonALUHandler


@pytest.fixture()
def signed_alu_config():
    return mock.Mock(
        BIT_ENDIAN="big",
        BIT_LENGTH=16,
        BIT_SIGNED=True
    )


@pytest.fixture()
def unsigned_alu_config():
    return mock.Mock(
        BIT_ENDIAN="big",
        BIT_LENGTH=16,
        BIT_SIGNED=False
    )


@pytest.fixture()
def signed_python_alu_handler(signed_alu_config):
    return PythonALUHandler(signed_alu_config)


@pytest.fixture()
def unsigned_python_alu_handler(unsigned_alu_config):
    return PythonALUHandler(unsigned_alu_config)
