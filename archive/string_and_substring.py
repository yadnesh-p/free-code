def count_substring(string, sub_string):
        l_s = len(string)
        l_ss = len(sub_string)
        output = 0
        for i in range(l_s):
              S=string[i:l_ss+i].strip()
              if S == sub_string:
                    output += 1      
        return output

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)