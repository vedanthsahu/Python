#GetItemsIndex
res=dict()
if_input = input("please enter names seperated by ',' : ").split(",")
items = ["ram", "sam", "tom", "ram", "sam", "ram"]
for i in range(len(items)):
    res.setdefault(items[i],[]).append(i)
print(res)


"""Module to compare two sets of employee IDs."""
def compare_employees(set_a, set_b):
    """Return missing, extra, and common employees between two sets."""
    unique_a = set_a - set_b
    unique_b = set_b - set_a
    common = set_a & set_b
    return (f"Unique in Set A {unique_a}, Unique in Set B {unique_b}, Common in Set A and Set B : {common}")


SET_A = {101, 102, 103, 104}
SET_B =           {103, 104, 105}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

print(compare_employees(SET_A, SET_B))
