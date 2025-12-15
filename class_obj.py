#class_obj.py
""""
This is demo py file which intends to make use of all the inheritances and class obj related things in py
"""
class NagativeSalaryError(Exception):  
    pass
 
class NullNameError(Exception):  
    pass
 
 
class Employee:
    def __init__(self, name, salary):

        if name is None or name.strip() == "":
            raise NullNameError("Name cannot be null or empty")

        if salary < 0:
            raise NagativeSalaryError("Salary cannot be negative")
 
        self.name = name
        self.salary = salary
 
    def yearly_salary(self):
        return self.salary * 12
 
try:
    emp = Employee("", -205464)
    print("Emp created successfully")

except (NullNameError, NagativeSalaryError) as e:
    print("Error:", e)

















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

        if price < 0:
            errors.append("Price cannot be negative")

        if stock < 0:
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
    item = Product("Pan", 10, 500)
    item.show_product()
    item.purchase(20)
    item.purchase(-10)
    item.purchase(200000)

except ProductValidationError as e:
    print("Product setup failed:", e)

except InvalidQuantityError as e:
    print("Quantity error:", e)

except OutOfStockError as e:
    print("Stock error:", e)

finally:
    print("Current stock:", item.get_stock())
    print("Price:", item.get_price())
