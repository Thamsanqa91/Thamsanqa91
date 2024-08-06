def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# You can test the function with some sample inputs
if __name__ == "__main__":
    print(is_leap(1990))  # Expected output: False
    print(is_leap(2000))  # Expected output: True
    print(is_leap(1900))  # Expected output: False
    print(is_leap(2400))  # Expected output: True
