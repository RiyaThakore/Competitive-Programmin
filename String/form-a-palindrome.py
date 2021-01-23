
# 1. check if it's a palindrome
# 2. return (len-1)
# 3. if same letters from the end, stop when different letter is found. 

def check_palindrome(word):
  for i in range(0, int(len(word)/2)):
    if word[i]!=word[len(word)-(i+1)]:
      return False
  return True

def check_same_letter(word):
  for j in range(len(word)):
    if word[len(word)-(j+1)] == word[len(word)-(j+2)]:
      continue
    else:
      idx=word.index(word[len(word)-(j+1)])
      return (idx)
      break

def form_palindrome(word):
  if check_palindrome == True:
    print(0)
  else:
    cnt=check_same_letter(word)
    print(cnt)

word="abcd"
form_palindrome(word)
