from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    """Abstract Base Class for all database types."""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def query(self, query_params):
        pass
    