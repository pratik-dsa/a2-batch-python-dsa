def change(a: list):
    a = 1000
    print(id(a))
    print(a)


# pass_by_reference
a: int = 50
print(id(a))
change(a)
print(a)


def display(lst: list):
    lst[0] = 100
    print(id(lst))
    print(lst)


my_list = [45, 33, 22, 11, 91]
print(id(my_list))
display(my_list)
print(my_list)
