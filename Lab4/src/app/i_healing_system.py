from abc import ABC, abstractmethod


class IHealingSystem(ABC):
    @abstractmethod
    def can_heal(self, target):
        pass

    @abstractmethod
    def calculate_heal_amount(self, target):
        pass
