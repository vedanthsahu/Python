#Error pooling so that we can log all errors and raise as one.



class InvalidQuantityError(Exception):
    pass

class OutOfStockError(Exception):
    pass

class ProductValidationError(Exception):
    """Raised when multiple validation errors must be pooled together."""
    pass

class Product:
    def __init__(self, name, price, stock):
        errors = []
        if not name or not name.strip():
            errors.append("Name cannot be empty")

        if price <=0:
            errors.append("Price cannot be negative")

        if stock <=0:
            errors.append("Stock cannot be negative")

        if errors:
            raise ProductValidationError(" | ".join(errors))
        self.name = name
        self.__price = price
        self.__stock = stock

    def show_product(self):
        print(f"Product: {self.name} Price: {self.__price}")

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def purchase(self, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0")

        if quantity > self.__stock:
            raise OutOfStockError(
                f"Requested {quantity}, but only {self.__stock} left"
            )

        self.__stock -= quantity
        print(f"Purchased quantity: {quantity}")



try:
    item = Product("", 0, 00) #triggering many errors
  

except ProductValidationError as e:
    print("Product setup failed:", e)

except InvalidQuantityError as e:
    print("Quantity error:", e)

except OutOfStockError as e:
    print("Stock error:", e)

finally:
    print("Current stock:", item.get_stock())
    print("Price:", item.get_price())


 