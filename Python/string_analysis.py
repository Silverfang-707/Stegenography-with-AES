import sys
def doSomething(inval):
    upper=0
    lower=0
    digit=0
    symbol=0
    for i in inval:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
        if i.isdigit():
            digit+=1
        if i in "!@#$%^&*()_+-=.<>?/`~:":
            symbol +=1
    return float((upper/len(inval))*100), float((lower/len(inval))*100), float((digit/len(inval))*100), float((symbol/len(inval))*100)
inputVal = input()
outputVal = doSomething(inputVal)
print("{0:.3f}".format(outputVal[0]))
print("{0:.3f}".format(outputVal[1]))
print("{0:.3f}".format(outputVal[2]))
print("{0:.3f}".format(outputVal[3]))