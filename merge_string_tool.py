def merge_the_tools(string, k):
    # your code goes here
    n = len(string)//k
    start = 0
    for i in range(n):
        end = start + k
        a=string[start:end]
        start = end
        b = [char for i, char in enumerate(a) if char not in a[:i]]
        print (''.join(b))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)