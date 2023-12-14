def add(numbers: str) -> int:
    res: int = 0
    splittedString = numbers.split(",")
    print(len(splittedString))
    if len(splittedString) < 1:
        return 0
    for num in splittedString:
        res = res + int(num)
    return res 



# if __name__ == '__main__':
#     numbers = input("Inserire una stringa di numeri")
#     add(numbers)
    