# python program to print even length words in a string
def printwords (s):
    s= s.split (' ')
    for word in s:
        if len (word)%2== 0:
            print (word)
s= " i am artist "
printwords(s)            