def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    outcomestring=""
    if num <= 9:
        lengthofnum=1
    elif num<= 99:
        lengthofnum=2
    elif num <= 999:
        lengthofnum=3
    elif num <= 3999:
        lengthofnum=4
    # 4 and 9 are special occasions otherwise numbers can be stacked side by side
    while 1000<=num<=3999:
        outcomestring += "M"
        num -= 1000
    if 900 <= num <= 999:
        outcomestring += "CM"
        num -= 900
    elif  600<= num <= 899:
        outcomestring += "D"
        num -= 500
    elif 400<=num<=499:
        outcomestring +="CD"
        num -= 400
    while 100<= num <= 399:
        outcomestring +="C"
        num -= 100
    

    

