def long_distinct(string):
  new=''
  dt={}
  j=0
  while j < (len(string)):
    if string[j] in new:
      substr_len=len(new)
      dt[j-substr_len]=substr_len
      new=''
    else:
      new+=string[j]
      j+=1
  keymax = max(dt, key=dt.get)
  return (string[keymax:keymax+dt[keymax]])

string='abababcdefababcdab'
distchar=long_distinct(string)
print(distchar)

