s='geeksforgeek'
new=[]
new_str=''
for i in range(len(s)-1):
  if s[i]==s[i+1]:
    new.append(i)
    new.append(i+1)
print(list(set(new)))
arr1=range(0,len(s))
arr2=list(set(new))
new_arr=[]
for j in range(0,len(arr1)):
  if arr1[j] not in arr2:
    new_arr.append(arr1[j])
print(new_arr)
for j in range(len(new_arr)):
  k=new_arr[j]
  print(k)
  new_str+=s[k]
  print(new_str)
print(new_str)
