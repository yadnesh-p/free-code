if __name__ == '__main__':
    s = input()
    print(s)
    #print (S_list)
    result1 = False
    result2 = False   
    result3 = False
    result4 = False
    result5 = False
    list_boolean_alphanum = []
    list_boolean_alpha = []
    list_boolean_digit = []
    list_boolean_lower = []
    list_boolean_upper = []
    for i in range(len(s)):
        list_boolean_alphanum.append(s[i].isalnum())
        list_boolean_alpha.append(s[i].isalpha())
        list_boolean_digit.append(s[i].isdigit())
        list_boolean_lower.append(s[i].islower())
        list_boolean_upper.append(s[i].isupper())
        result1 = True if[x for x in list_boolean_alphanum if x is True]else False
        result2 = True if[x for x in list_boolean_alpha if x is True]else False
        result3 = True if[x for x in list_boolean_digit if x is True]else False
        result4 = True if[x for x in list_boolean_lower if x is True]else False
        result5 = True if[x for x in list_boolean_upper if x is True]else False

    


    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)



    
         
            