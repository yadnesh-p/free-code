def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    #Defining swap function
    
    def swap(char):
        if char.islower():
            return char.upper()
        elif char.isupper():
            return char.lower()
        else :
            return char
    
    words = sentence.split()
    print (words)
    reverse = words[::-1]
    print (reverse)
    swappeds = []
    for word in reverse:
        swapped = ''.join(swap(char) for char in reverse.split())
        print(swapped)
        swappeds.append(swapped)
        print (swappeds)
        output = ''.join(swapped)
        print (output)
        return output  
if __name__ == '__main__' :
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    sentence = input('Take input')

    result = reverse_words_order_and_swap_cases(sentence)
    print (result)
    #fptr.write(result + '\n')

    #fptr.close()
    
    #Codeikn kndkm KLNS