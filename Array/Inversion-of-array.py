W=[2, 4, 1, 3, 5]
new_list=[]
'''
for i in range(len(W)):
  for j in range(i,len(W)):
    if W[i]>W[j]:
      new_list.append((W[i], W[j]))
print(new_list)
'''
res = [((W[i], W[j])) for i in range(len(W)) for j in range(i,len(W)) if W[i]>W[j]]
print(res)
