from unittest import mock

import pytest

from computer_emulator.cpu.registers._python_register_handler import PythonRegisterHandler


@pytest.fixture()
def register_config():
    return mock.Mock(
        REGISTER_COUNT=16,
        BIT_LENGTH=16
    )


@pytest.fixture()
def python_register_handler(register_config):
    return PythonRegisterHandler(register_config)
