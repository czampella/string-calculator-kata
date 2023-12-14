def add(numbers: str) -> int:
    res: int = 0
    splittedString = numbers.split(",")
    for num in splittedString:
        try:
            res = res + int(num)
        except Exception as e:
            return res
    return res 



# if __name__ == '__main__':
#     numbers = input("Inserire una stringa di numeri")
#     add(numbers)
    