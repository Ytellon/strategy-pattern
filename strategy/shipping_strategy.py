from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, package):
        pass

class SEDEXStrategy(ShippingStrategy):
    def calculate(self, package):
        return package['weight'] * 12.00 + 5.00

class PACStrategy(ShippingStrategy):
    def calculate(self, package):
        return package['weight'] * 8.00 + 7.00

class ExpressStrategy(ShippingStrategy):
    def calculate(self, package):
        return package['weight'] * 20.00 + 10.00
