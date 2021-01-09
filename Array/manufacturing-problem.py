city_nodes=[5]
city_from=[1,1,2,3,1]
city_to=[2,3,4,5,5]
company=[1]

visited=[]
new_to=[]
indx=[]

def find_new_to(numbr):
  for i,val in enumerate(city_from):
    if val==numbr:
      new_to.append(city_to[i])
      if numbr in new_to:
        new_to.remove(numbr)
      visited.append(numbr)
  return new_to.sort()

n=find_new_to(company[0])
m=find_new_to(new_to[0])
print("New to: ", n)
print("New from: ", m)
print(new_to)
