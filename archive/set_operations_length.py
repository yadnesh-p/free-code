if __name__ == '__main__' :
    n = int(input())
    roll_num_E = set(map(int,input().split()))
    b = int(input())
    roll_num_F = set(map(int,input().split()))
    print (len(roll_num_E.union(roll_num_F)))
    print (len(roll_num_E.intersection(roll_num_F)))
    print (len(roll_num_E.intersection(roll_num_F)))
    print (len(roll_num_E.difference(roll_num_F)))
    print (len(roll_num_E.symmetric_difference(roll_num_F)))

