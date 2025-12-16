def total_marks(*marks):
    return sum(marks)
def calculate_grade(percentage):
    grade_rules = {
        80: "A",
        60: "B",
        0:  "C"
    }

    for limit in grade_rules:
        if percentage >= limit:
            return grade_rules[limit]
        
print(total_marks(20,20,30,40))
print(calculate_grade(70))