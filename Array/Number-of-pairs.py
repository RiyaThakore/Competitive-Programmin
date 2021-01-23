X=[2,1,6]
Y=[1,5]
#res = [((X[x], Y[y])) for x in range(len(X)) for y in range(len(Y)) if (pow(X[x],Y[y]) > pow(Y[y],X[x]))]
#print(res)

cnt=0
for x in range(len(X)):
  for y in range(len(Y)):
    if (pow(X[x],Y[y]) > pow(Y[y],X[x])):
      cnt+=1
print(cnt)
