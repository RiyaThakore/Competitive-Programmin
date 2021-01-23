S = "zvvo"
S = S.lower()
d={}
occ=[]
dup=''
for i in range(len(S)):
  if S[i] in d.keys():
    continue
  else:
    d[S[i]]=S.find(S[i])
for key in d.items() :
    occ.append(key)
for j in range(len(occ)):
  dup+=occ[j][0]
print(dup)
