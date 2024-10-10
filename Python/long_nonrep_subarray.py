def long_str(string):
    if len(set(string)) == len(string):
        return len(string)
    else:
        return max(long_str(string[1:]), long_str(string[:-1]))
    
string=input()
print(long_str(string))