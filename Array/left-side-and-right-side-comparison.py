arr=[4,3,2,7,8,9]

def left_right(a,idx):
  left_arr,right_arr=[],[]
  for j in range(0, idx):
    left_arr.append(a[j])
  for k in range(idx+1, len(a)):
    right_arr.append(a[k])
  #print('left_arr',left_arr)
  #print('right_arr',right_arr)
  return left_arr, right_arr

def compare(left_arr, right_arr, idx):
  left_cnt,right_cnt=0,0
  for j in range(len(left_arr)):
    if left_arr[j]<arr[idx]:
      left_cnt+=1
  for j in range(len(right_arr)):
    if right_arr[j]>arr[idx]:
      right_cnt+=1
  #print('left_cnt',left_cnt)
  #print('right_cnt',right_cnt)
  if left_cnt==len(left_arr) and right_cnt==len(right_arr):
    return idx

def main(arr):
  m=1
  while m != (len(arr)-1):
    #print('m, ', m)
    #print('element, ', arr[m])
    l,r=left_right(arr,m)
    index=compare(l,r,m)
    #print(l)
    #print(r)
    print('index',index)

    if index==m:
      print("Final:",arr[m])
      break
    if m == (len(arr)-2) and index is None:
      print("Final:,",-1)
    m+=1
print(arr) 
main(arr)
