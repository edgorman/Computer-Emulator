from __future__ import annotations
from threading import Thread

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from types import ModuleType
    from typing import List, Union
    from computer_emulator.cpu.alu._alu_interface import ALUInterface
    from computer_emulator.cpu.registers._registers_interface import RegistersInterface
    from computer_emulator.memory._memory_interface import MemoryInterface

from ._cu_interface import CUInterface, AddressingModeEnum


class PythonCUHandler(CUInterface):

    def __init__(self,
        config: ModuleType,
        alu: ALUInterface,
        memory: MemoryInterface,
        registers: RegistersInterface
    ) -> None:
        self.__mode_length = config.INSTRUCTION_MODE_LENGTH
        self.__opcode_length = config.INSTRUCTION_OPCODE_LENGTH
        self.__operand_length = config.INSTRUCTION_OPERAND_LENGTH

        self.__alu = alu
        self.__memory = memory
        self.__registers = registers

        self.__thread = Thread(target=self._execute_instructions)

    def _decode_instruction(self, instruction: bytes) -> Union[AddressingModeEnum, function, List[bytes]]:
        # Separate the instruction into the mode, opcode and operands
        bin_mode = instruction[:self.__mode_length]
        bin_opcode = instruction[self.__mode_length:self.__mode_length+self.__opcode_length]
        bin_operand = instruction[self.__mode_length+self.__opcode_length:]

        # Decode the mode type, opcode function and list of operands
        enum_mode = AddressingModeEnum(int.from_bytes(bin_mode))
        operation = self.__alu.get_operation(bin_opcode)
        operands = [
            bin_operand[n:n+self.__operand_length] 
            for n in range(0, len(bin_operand), self.__operand_length)
        ]

        return enum_mode, operation, operands

    def _read_register(self, address: bytes) -> bytes:
        self.__registers.read_index(int.from_bytes(address))
    
    def _read_memory(self, address: bytes) -> bytes:
        self.__memory.read_address(address)

    def _update_register(self, address: bytes, change: int) -> bytes:
        value = self.__registers.read_index(int.from_bytes(address))
        self.__registers.store_address(self.__alu.add(value, change))
        return self._read_register(address)

    def _evaluate_operands(self, mode: AddressingModeEnum, operands: List[bytes]) -> List[bytes]:
        # Extract the operand values depending on the addressing mode
        if mode == AddressingModeEnum.IMPLIED:
            read_func = lambda o: None
        elif mode == AddressingModeEnum.IMMEDIATE:
            read_func = lambda o: o
        elif mode == AddressingModeEnum.REGISTER:
            read_func = lambda o: self._read_register(o)
        elif mode == AddressingModeEnum.REGISTER_INDIRECT:
            read_func = lambda o: self._read_register(self._read_register(o))
        elif mode == AddressingModeEnum.AUTO_INCREMENT:
            read_func = lambda o: self._update_register(o, 1)
        elif mode == AddressingModeEnum.AUTO_DECREMENT:
            read_func = lambda o: self._update_register(o, -1)
        elif mode == AddressingModeEnum.MEMORY_DIRECT:
            read_func = lambda o: self._read_memory(o)
        elif mode == AddressingModeEnum.MEMORY_INDIRECT:
            read_func = lambda o: self._read_memory(self._read_memory(o))
        else:
            raise ValueError(f"The CU does not recognise the addressing mode '{mode}'")

        # Read each operand based off the mode read function
        operands = [read_func(o) for o in operands]
        return operands

    def _execute_operation(self, operation: function, operands: List[bytes]) -> None:
        operation(*operands)

    def _execute_instructions(self) -> None:
        program_counter_address = self.__registers.PROGRAM_COUNTER_ADDRESS

        # Iterate until the there are no instructions or the CPU raises an exception
        while True:
            # Fetch the next instruction from memory
            instruction_address = self.__registers.read_index(program_counter_address)
            instruction_data = self.__memory.read_address(instruction_address)

            # Decode the instruction
            mode, operation, operands = self._decode_instruction(instruction_data)
            operands = self._evaluate_operands(mode, operands)

            # Execute the instruction and increment pc
            self.__registers.store_address(self.__alu.increment(program_counter_address), program_counter_address)
            self._execute_operation(operation, operands)

    def run(self) -> None:
        # Run the thread and wait to finish
        self.__thread.start()
        self.__thread.join()
