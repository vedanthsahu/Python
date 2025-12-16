from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    Base class representing a generic vehicle.

    Design goals:
    - Enforce invariants on speed
    - Expose intent clearly
    - Prevent unsafe external mutation
    """

    MAX_ALLOWED_SPEED = 400  # Global business constraint

    def __init__(self, brand: str, max_speed: int):
        self.brand = brand
        self._max_speed = None          # Protected, internally controlled
        self._set_max_speed(max_speed) # Centralized validation

    def _set_max_speed(self, speed: int) -> None:
        if not isinstance(speed, int):
            raise TypeError("Max speed must be an integer")

        if speed <= 0:
            raise ValueError("Max speed must be positive")

        if speed > self.MAX_ALLOWED_SPEED:
            raise ValueError(
                f"Max speed cannot exceed {self.MAX_ALLOWED_SPEED}"
            )

        self._max_speed = speed

    @property
    def max_speed(self) -> int:
        return self._max_speed

    @abstractmethod
    def is_speed_exceeding_limit(self, speed: int) -> bool:
        """Each vehicle defines how speed checks behave"""
        pass

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(brand={self.brand!r}, max_speed={self._max_speed})"
        )

class Car(Vehicle):
  

    def is_speed_exceeding_limit(self, speed: int) -> bool:
        return speed > self._max_speed

    # Optional controlled mutation (explicitly allowed)
    def update_max_speed(self, new_speed: int) -> None:
        self._set_max_speed(new_speed)



class SportsCar(Car):

    SPEED_TOLERANCE = 10  # km/h grace buffer

    def is_speed_exceeding_limit(self, speed: int) -> bool:
        return speed > (self._max_speed + self.SPEED_TOLERANCE)


vehicles = [
    Car("Contoso Auto", 220),
    SportsCar("Velocity Motors", 300),
]

test_speed = 310

for v in vehicles:
    print("\nVehicle:", v)
    print(f"Testing speed {test_speed} km/h")
    print("Exceeds limit?", v.is_speed_exceeding_limit(test_speed))


car = vehicles[0]

print("\n--- Direct protected access (Dont use) ---")
print("Before:", car._max_speed)

# This bypasses all validation and invariants
car._max_speed = 999

print("After :", car._max_speed)
print("Business rules are now violated.")



print("\n--- Restoring via controlled update ---")
car.update_max_speed(240)
print("Fixed max speed:", car.max_speed)

print(
    "Re-test:",
    car.is_speed_exceeding_limit(test_speed)
)


print("\n--- __dict__ inspection ---")
print(car.__dict__)

print("\n--- dir() inspection (filtered) ---")
for attr in dir(car):
    if "speed" in attr:
        print(attr)
