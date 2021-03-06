def myAtoi(str: str) -> int:
    str = str.strip()

    result = 0

    if len(str) < 1 or str is None:
        return result

    is_positive = True
    start_index = 0

    if str[0] == '-':
        is_positive = False
        start_index = 1
    elif str[0] == '+':
        start_index = 1

    if start_index >= len(str) or str[start_index].isdigit() is False:
        return result

    end_index = 0
    for i in range(start_index, len(str)):
        if str[i].isdigit() is False:
            break
        end_index = i

    result = float(str[start_index: end_index + 1])

    if not is_positive:
        result = -result

    if result > 2 ** 31 - 1:
        return 2 ** 31 - 1
    elif result < -2 ** 31:
        return -2 ** 31

    return int(result)
print(myAtoi("0-1"))