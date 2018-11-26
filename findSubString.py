def count_substring(string, sub_string):
    size = len(sub_string);
    result = 0;
    #ABCDCDC
    #CDC
    for i in range(0, len(string) - (size-1)):
        count = 0;
        if(string[i] == sub_string[0]):
            count += 1;
            x = i + 1;
            for j in range(1, size):     
                if(string[x] == sub_string[j]):
                    count += 1;
                    x+=1;   
            if (count == size):
                result += 1;
    return result;

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
