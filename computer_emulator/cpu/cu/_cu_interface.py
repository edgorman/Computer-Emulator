from abc import ABC, abstractmethod



class CUInterface(ABC):

    @abstractmethod
    def run(self) -> None:
        """perform the next operation and execute the required actions"""
