import math
a=[3, 2, 4, 6, 5]
a.sort()
a_square=[]
for j in range(len(a)):
  a_square.append(a[j]*a[j])

def find_triplet(a_square,a):
  for m in range(len(a_square)):
    for n in range(m+1,len(a_square)):
      sum_no=a_square[m]+a_square[n]
      if sum_no in a_square:
        aw=math.sqrt(a_square[m])
        bw=math.sqrt(a_square[n])
        if aw in a and bw in a:
          cw=math.sqrt(sum_no)
          return aw, bw, cw

x,y,z=find_triplet(a_square,a)
print(x,y,z)
