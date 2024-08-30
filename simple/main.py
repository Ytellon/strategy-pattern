from order import Order

if __name__ == "__main__":
    package = {'weight': 2.5}

    sedex = Order(package, "SEDEX")
    print(f"Frete SEDEX: R$ {sedex.calculate_shipping():.2f}")

    pac = Order(package, "PAC")
    print(f"Frete PAC: R$ {pac.calculate_shipping():.2f}")

    express = Order(package, "Express")
    print(f"Frete Express: R$ {express.calculate_shipping():.2f}")
