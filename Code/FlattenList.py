# Flattens a list of values and nested lists with limited depth

def flatten_recursively(list):
  for value in list:
    try:
      yield from flatten_recursively(value)
    except TypeError:
      yield value

# debug
print(list(flatten_recursively([[1,2,[3]],4])))
