# -*- coding: utf-8 -*-

#By passing the delimeter the function will remain the same even if the request changes
def add_formatted(numbers: str, delimiter: str) -> int:
    res: int = 0
    negatives = []
    splittedString = numbers.split(delimiter)
    print(splittedString)
    for num in splittedString:
        if num == '':
            return res
        try:
            a = int(num)
            if(a<0):
                negatives.append(num)
            elif a > 1000:
                a = 0
        except Exception as e:
            return 'Error, string not correctly formatted'
        res = res + a
    if len(negatives) > 0:
        msg = ', '.join(negatives)
        return 'Negatives not allowed : ' + msg
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
    
    return add_formatted(string, delimiter)

    