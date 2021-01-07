# Flattens a list of values and nested lists with limited depth


def flatten_list(list):
    for value in list:
        try:
            yield from flatten_list(value)
        except TypeError:
            yield value


print(list(flatten_list([1])))
print(list(flatten_list([[1,2,[3]],4])))
print(list(flatten_list([[5,6,[7]],8])))


