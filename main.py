def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    outcomestring = ""
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
    if 90<=num<=99:
        outcomestring +="XC"
        num -= 90
    while 50<=num<=89:
        outcomestring += "L"
        num -= 50
    if 40<= num<= 49:
        outcomestring += "XL"
        num -= 40
    while 10<=num<=39:
        outcomestring +="X"
        num -=10
    if num == 9:
        outcomestring += "IX"
        num -=9
    elif 5<=num<=8:
        outcomestring += "V"
        num -=5
    if num ==4:
        outcomestring +="IV"
        num -=4
    while 1<=num<=3:
        outcomestring += "I"
        num -=1
    return outcomestring
