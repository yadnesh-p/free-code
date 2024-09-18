def minion_game(string):
    # your code goes here
    list_S = []
    count = 0
    count1 = 0
    for i in s:
        list_S.append(i)

    for j in range(len(list_S)):
        if list_S[j] in 'AEIOU':
            count = count + len(list_S) - j
        else:
            count1 = count1 +len(list_S) - j
    print (count,count1)
    if count > count1:
        print (f'Kevin {count}')
    elif count1 > count:
        print (f'Stuart {count1}')
    else:
        print ('Draw')
            
    


if __name__ == '__main__':
    s = input()
    minion_game(s)