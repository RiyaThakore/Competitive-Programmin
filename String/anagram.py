#a = 'geeksforgeeks'
#b = 'forgeeksgeeks'
a='bd'
b='bd'
def letter_count(s):
    d = {}
    for i in s:
        d[i] = d.get(i,0)+1
    return d

def isAnagram(a,b):
    a1=letter_count(a)
    b1=letter_count(b)
    print(a1)
    print(b1)
    if a1 == b1:
      return True #true-false  due to the boolean function
    else:
      return False
isAnagram(a,b)
