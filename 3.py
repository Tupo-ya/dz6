def get_max(a: int, b: int, c = float('-inf')):
    max_val = float('-inf')

    if a > b:
        max_val = a
    else:
        max_val = b
    if c > max_val:
        max_val = c

    return max_val

print(get_max(1,2,1))
print(get_max(23,2))
print(get_max(23,42))
print(get_max(23, 2, 123))