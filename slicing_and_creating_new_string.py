def mutate_string(string, position, character):
    s_modify = s[:(int(i))] + str(c) + s[(int(i)+1):]
    return s_modify

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)