from abc import ABC, abstractmethod
from typing import Union


class Formula(ABC):
    """Represents a mathematical formula"""

    @abstractmethod
    def _calculate(self, value: Union[int, float]) -> Union[int, float]: pass

    def calculate(self, value: Union[int, float]) -> Union[int, float]:
        return self._calculate(value=value)

    @abstractmethod
    def _to_string(self) -> str: pass

    def to_string(self) -> str:
        return self._to_string()

    def represent(self, value: Union[int, float, str]) -> str:
        return self.to_string().replace("{value}", value)
