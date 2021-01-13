dicts={0:0,1:0,2:0}
arr=[0, 2, 1, 2, 0, 0, 1, 2, 2]
keys=range(0,2)
for u in range(len(arr)):
  for z in range(len(keys)+1):
    if z == arr[u]:
      dicts[z]=dicts[z]+1
print(dicts)
sort_arr=[]
for m in range(0,3):
  for n in range(dicts[m]):
    sort_arr.append(m)
print(sort_arr)
