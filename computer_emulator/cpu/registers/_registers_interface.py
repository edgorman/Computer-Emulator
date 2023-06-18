from abc import ABC, abstractmethod


class RegistersInterface(ABC):

    @abstractmethod
    def store_value(self, value: bytes, register_index: int) -> None:

        ...

    @abstractmethod
    def read_value(self, register_index: int) -> bytes:
        ...
