
def greatest_element(q, m):
  flag=0
  for i in range(m,len(q)):
    if q[m] >= q[i]:
      flag+=1
      continue
  if flag == len(q)-m:
    return q[m]

def leaders(q):
  leaders=[]
  for j in range(len(q)):
    l=greatest_element(q,j)
    if l != None:
      leaders.append(l)
  print(leaders)

q=[16,17,4,3,5,2]
leaders(q)
