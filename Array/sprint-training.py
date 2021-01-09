#************FINAL CODE************

def sprint_training():
  matrix,occ,o,a=[],[],[],[]
  for i in range(m-1):        
    a =[] 
    for j in range(n):       
      a.append(j+1) 
  matrix.append(a) 
  for i in range(m-1): 
    for j in range(n): 
      print(matrix[i][j], end = " ") 
    print()
  i=0
  while (i<m-1):
    start=sprint[i]
    end=sprint[i+1]
    if (i<m-1):
      for k in range(end, start+1):
        id=matrix[i].index(k)
        matrix[i][id]="#"
      i+=1
  for x in range(m-1):
    o=[]
    for y in range(n):
      if matrix[x][y] == '#':
        o.append(y)
      occ.append(o)]
  dicts={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
  keys=range(0,n)
  for u in range(m-1):
    for z in keys:
      if z in occ[u]:
        dicts[z]=dicts[z]+1
  minimum=min(dicts.values())
  print(minimum)

if __name__=="__main__":
  n,m=9,4
  sprints=[9,7,3,1]
  sprint_training(n,m,sprints)
