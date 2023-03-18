from abc import abstractmethod, ABC
from typing import List


class StateInterface(ABC):

    @abstractmethod
    def add(self, doc: dict):
        ...

    @abstractmethod
    def get(self, fields: List) -> dict:
        ...

    @abstractmethod
    def set(self, doc):
        ...

    @abstractmethod
    def delete(self, fields: List):
        ...
