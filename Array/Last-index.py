def last_index(a):
    rev=''
    if str(1) in a:
        for i in range(len(a), 0, -1):
            rev += a[i-1]
            if str(1) in rev:
                b=rev.index('1')
                print(len(a)-(b+1))
                break
    else:
        print(-1)

input_list=[]
for _ in range(int(input())):
    a=input() 
    input_list.append(a)
for j in range(len(input_list)):
    last_index(input_list[j])
