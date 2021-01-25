
def longest_prefix(lst):
  pfx=" "
  short=min(lst, key=len)
  for i in range(len(short)):
    cnt=0
    for j in range(len(lst)-1):
      if lst[j][i] == lst[j+1][i]:
        cnt+=1
    else:
        pfx=-1
        break
    if cnt==len(lst)-1:
      pfx+=lst[j][i]
  return (pfx)
  
#lst=["geeksforgeeks", "geeks", "geekss", "geekkzer"]
#lst=['keedd','keep','keewed','ker']
lst=['rr','ge']

prefix=longest_prefix(lst)
print(prefix)
