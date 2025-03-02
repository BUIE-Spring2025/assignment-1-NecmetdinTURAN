def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    lengthofnum = 0
    if num <= 9:
        lengthofnum=1
    elif num<= 99:
        lengthofnum=2
    elif num <= 999:
        lengthofnum=3
    elif num <= 3999:
        lengthofnum=4
    
