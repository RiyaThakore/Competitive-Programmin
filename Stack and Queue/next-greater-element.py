def push(stack, x):
    stack.append(x)
 
def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()

def printNGE(arr):
    s = []
    element, next = 0, 0
    push(s, arr[0])
    for i in range(1, len(arr), 1):
        next = arr[i]
        if isEmpty(s) == False:
            element = pop(s)
            while element < next:
                print(str(element) + " -- " + str(next))
                if isEmpty(s) == True:
                    break
                element = pop(s)
            if element > next:
                push(s, element)
        push(s, next)
    while isEmpty(s) == False:
        element = pop(s)
        next = -1
        print(str(element) + " -- " + str(next))
 
arr = [1,3,2,4]
printNGE(arr)
