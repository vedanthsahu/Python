class Student:
    def __init__(self, name, marks, aadhar):
        self.name = name            # Public attribute
        self._marks = marks         # Protected attribute
        self.__aadhar = aadhar      # Private attribute

    def calculate_grade(self):
        """Return grade based on marks."""
        if self._marks >= 85:
            return "A"
        elif self._marks >= 60:
            return "B"
        else:
            return "C"

    def show_profile(self):
        """Display only safe public information."""
        print(f"Name: {self.name}")
        print(f"Marks: {self._marks}")
        print(f"Grade: {self.calculate_grade()}")
        print("(Aadhar number is private and cannot be displayed.)")
s1 = Student("A", 92, "1234-5678-2222")
s2 = Student("B", 74, "9934-1278-4583")
s3 = Student("C", 58, "5567-2234-8888")

students = [s1, s2, s3]

for st in students:
    print("\nStudent Info:")
    st.show_profile()
print("\n--- Attribute Access Test ---")

# Allowed but not recommended (Python convention says: protect it)
print("Accessing protected _marks:", s1._marks)

# This will fail → AttributeError
try:
    print("Accessing private __aadhar:", s1.__aadhar)
except Exception as e:
    print("Private attribute access failed:", e)

# Access through name-mangled form (discouraged but possible technically)
print("Access private using name-mangling:", s1._Student__aadhar)
