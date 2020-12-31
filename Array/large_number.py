
arr=[61, 9, 98, 76, 1126]
max_len = len(str((max(arr))))

def repeat_digit(num, max_len):
  a,b=str(num),''
  for j in range(0, max_len):
    b=b+a
  return b[0:max_len+1]

def repeat_dig_array(arr1, max_len):
  arr2=[]
  arr2 = [arr2.append(repeat_digit(arr1[i], max_len)) for i in range(0, len(arr1))]
  return arr2

def printLargest(arr1, max_len):
  fin=repeat_dig_array(arr1, max_len)
  final=''
  print(fin)
  while(fin.count('0')!=len(arr1)):
    j=max(fin)
    print(j)
    i=fin.index(j)
    final=final+str(arr1[i])
    fin[i]='0'
    print(fin)
  return final

final = printLargest(arr, max_len)
print(final)