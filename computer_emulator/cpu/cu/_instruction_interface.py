from abc import ABC, abstractmethod


class InstructionInterface(ABC):

    @abstractmethod
    def decode() -> None:
        """decode the instruction"""
    
    @abstractmethod
    def encode() -> None:
        """encode the instruction"""
