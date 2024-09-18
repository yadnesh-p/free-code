def swap(num1,num2):
    print (f"this is original {num1} and {num2}")
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print (f"this is swapped {num1} and {num2}")

swap(-8,-3)