string='baaabbbaaaaaa'

def longest_palindrome(string):
  l=0
  for j in range(0,13):
    print("j:", j)
    for k in range(j,13):
      x=j
      y=12-k
      #print("A:",string[x:y])
      #print("B:",string[y-1:x-1:-1])
      if string[x:y] == string[y-1:x-1:-1] and len(string[x:y])>l:
        l=len(string[x:y])
        print(string[x:y])

longest_palindrome(string)
      
