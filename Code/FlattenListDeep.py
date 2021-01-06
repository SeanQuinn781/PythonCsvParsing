from collections.abc import Iterable

# Flattens a list of values and nested lists with depth

def flatten_deep(list):
    for value in list:
        if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
            yield from flatten_deep(value)
        else:
            yield value

def flatten_deep_no_module(list):
    if isinstance(list, Iterable):
        return [a for i in list for a in flatten_deep_no_module(i)]
    else:
        return [list]

# debug
# print(list(flatten_deep([[1,2,[3],[5,6,[7,8],9]],10])))
# print(list(flatten_deep_no_module([[1,2,[3],[5,6,[7,8],9]],10])))

list(flatten_deep([[1,2,[3],[5,6,[7,8],9]],10]))
list(flatten_deep_no_module([[1,2,[3],[5,6,[7,8],9]],10]))
