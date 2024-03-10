import copy

a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112]

b = copy.copy(a)  # Shallow Copy
b[2] = 133
print("A ->", a, id(a))
print("B ->", b, id(b))

# b = copy.deepcopy(a)  # Deep Copy
# print("A ->", a, id(a))
# print("B ->", b, id(b))
#
#
# print("B ->", b, id(b))
# this is passing of reference memory to another variable
# ex-1
# print("A ->", a, id(a))
# b = a
# ex-2
# b = a
# b[3][1] = 1000
# print("A ->", a, id(a))
# print("B ->", b, id(b))
