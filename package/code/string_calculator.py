import re

#By passing the delimeter the function will remain the same even if the request changes
def add_formatted(numbers: str, delimiter: str) -> int:
    res: int = 0
    splittedString = numbers.split(delimiter)
    for num in splittedString:
        if num == '':
            return res
        try:
            res = res + int(num)
        except Exception as e:
            return 'Error'
    return res 

#In a scenario in which requirements change fast, the only function that will need to be changed is this
#Delimiters are returned in a format compatible with the split function
def calculate_delimiter(string: str):
    if('//' in string):
        splitted = string.split('\n')
        delimiter = splitted[0][-1]
        numbers = splitted[1]
        return numbers, delimiter
    else:
        for s in string:
            try:
                int(s)
            except Exception:
                return string, s

#First calculates the delimiter, gets the string without the delimiter instructions
#and the delimeter in split compatible form and then calls the add function

def add(numbers: str):
    string, delimiter = calculate_delimiter(numbers)
    print(string, delimiter)
    return add_formatted(string, delimiter)

if __name__ == '__main__':
    numbers = input("Inserire una stringa di numeri")
    add(numbers)
    