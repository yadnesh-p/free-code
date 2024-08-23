def split_and_join(line):
    # write your code here
    s = line.split(" ")
    a = "-".join(s)
    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)