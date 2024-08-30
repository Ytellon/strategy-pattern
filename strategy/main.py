from order import Order
from shipping_strategy import SEDEXStrategy, PACStrategy, ExpressStrategy

if __name__ == "__main__":
    package = {'weight': 2.5}

    sedex = Order(package, SEDEXStrategy())
    print(f"Frete SEDEX: R$ {sedex.calculate_shipping():.2f}")

    pac = Order(package, PACStrategy())
    print(f"Frete PAC: R$ {pac.calculate_shipping():.2f}")

    express = Order(package, ExpressStrategy())
    print(f"Frete Express: R$ {express.calculate_shipping():.2f}")
