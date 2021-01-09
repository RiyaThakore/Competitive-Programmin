
def min_diff(a,n,m):
  if (m==0 or n==0):
    return 0
  if (n<m):
    return -1
  a.sort()
  key_list, diff_list, new=[],[],[]
  for i in range(len(a)-m+1):
    key_list.append(i)
    diff_list.append(a[i+m-1]-a[i])
  k=diff_list.index(min(diff_list))
  p=key_list[k]
  for j in range(p,p+m):
    new.append(a[j])
  print(new)

if __name__=="__main__":
  a=[9,1,12,56,7,9,3,4]
  m=int(input())
  n=int(input())
  min_diff(a,n,m)
