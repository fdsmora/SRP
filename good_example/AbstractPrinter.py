from abc import ABC, abstractmethod

class AbstractPrinter(ABC):
    
    @abstractmethod
    def print(self):
        pass