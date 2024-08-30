from shipping_strategy import ShippingStrategy

class Order:
    def __init__(self, package, shipping_strategy: ShippingStrategy):
        self.package = package
        self.shipping_strategy = shipping_strategy
    
    def calculate_shipping(self):
        return self.shipping_strategy.calculate(self.package)

#classe Order que usando strategy