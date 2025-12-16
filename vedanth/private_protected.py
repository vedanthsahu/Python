"""
There is no actually protected or private in Python. Just name change
"""
class Student:
    def __init__(self, name: str, marks: int, aadhar: str):
        self.name = name            # Public
        self._marks = marks         # Protected (convention)
        self.__aadhar = aadhar      # Private (name-mangled)

    def show_profile(self):
        print(f"Name   : {self.name}")
        print(f"Marks  : {self._marks}")
        print("(Aadhar is private and hidden)")



s1 = Student("vedanth", 92, "1234-5678-2222")



print("\n--- Normal Access ---")
print("Public name        :", s1.name)
print("Protected _marks   :", s1._marks)

try:
    print("Private __aadhar  :", s1.__aadhar)
except AttributeError as e:
    print("Private access failed:", e)


print("\n--- __dict__ (Actual Storage) ---")
print(s1.__dict__)

# Observe:
# '__aadhar' does NOT exist
# '_Student__aadhar' DOES exist


print("\n--- Name-Mangled Private Access ---")
print("Access via _Student__aadhar :", s1._Student__aadhar)

print("\n--- dir(s1) ---")
print(dir(s1))


print("\n--- Detecting Private Attributes Dynamically ---")
for attr in dir(s1):
    if attr.startswith("_Student__"):
        print(f"{attr} → {getattr(s1, attr)}")


print("\n--- Modifying Private Attribute From Outside ---")
s1._Student__aadhar = "9999-8888-7777"
print("Modified private aadhar:", s1._Student__aadhar)

print("\n--- Final Student Profile ---")
s1.show_profile()
