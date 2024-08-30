class Order:
    def __init__(self, package, shipping_method):
        self.package = package
        self.shipping_method = shipping_method
    
    def calculate_shipping(self):
        if self.shipping_method == "SEDEX":
            return self.package['weight'] * 12.00 + 5.00
        elif self.shipping_method == "PAC":
            return self.package['weight'] * 8.00 + 7.00
        elif self.shipping_method == "Express":
            return self.package['weight'] * 20.00 + 10.00
        else:
            raise ValueError("Método de envio desconhecido")