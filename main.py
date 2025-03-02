def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    lengthofnum = 0
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
    while lengthofnum==4:
        if 1000<=num<=3999:
            outcomestring += "M"
            num -= 1000
            if num <= 9:
                lengthofnum=1
            elif num<= 99:
                lengthofnum=2
            elif num <= 999:
                lengthofnum=3
            elif num <= 3999:
                lengthofnum=4