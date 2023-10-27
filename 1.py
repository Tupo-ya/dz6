def is_palind(string: str):
    string = string.lower()

    result = True
    for i in range(len(string)//2):
        if string[i] != string[-i-1]:
            result = False
    return result


print(is_palind('onono'))
print(is_palind('Hello'))