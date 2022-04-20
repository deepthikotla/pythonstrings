# ways to remove i'th character from string in python 
def remove (string, n):
    a = string [:n]
    b = string [n+1:]
    return a + b
if __name__ == '__main__':
    string = "deepthiFORdeepthi"
    n= 5
print (remove (string, n))