A=[1,3,5,6,2,2,1,4]

def left_elem(A, i):
  sum_left,j=0,0
  while(j<i):
    sum_left+=A[j]
    j+=1
  return sum_left

def right_elem(A, i):
  sum_right,j=0,(i+1)
  while(j<len(A)):
    sum_right+=A[j]
    j+=1
  return sum_right

def equ_pt(A):
  for k in range(len(A)):
    l=left_elem(A, k)
    r=right_elem(A, k)
    if (l == r):
      return A[k]

e=equ_pt(A) 
print(e)
