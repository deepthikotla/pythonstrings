# Remove all duplicates from a given string in python
def removeDuplicate (str):
    s= set(str)
    s= "". join(s)
    print("without order :",s)
    t= " "
    for i in str :
        if (i in t):
            pass
        else:
            t= t+i
        print("with order :", t)
str = "milkformilk"
removeDuplicate(str)            