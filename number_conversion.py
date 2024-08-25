import math
def print_formatted(number):
    # your code goes here
    width = len(format(n,'b'))
    for i in range(1,n+1):
        octal = format(i,'o')
        hexa = hex(i)[2:].upper()
        binary = format(i,'b')
        
        print(str(i).rjust(width),octal.rjust(width),hexa.rjust(width),binary.rjust(width)) 
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)