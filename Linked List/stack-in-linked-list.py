class Node:
  def __init__(self, data):
    self.data=data
    self.next=None

class Stack:
  def __init__(self):
    self.front=self.rear=None

  def isEmpty(self):
    return self.front == None

  def Push(self, item):
    temp=Node(item)
    if self.front == None:
      self.front=self.rear=temp
      return
    temp.next=self.front
    self.front=temp
  
  def Pop(self):
    if self.isEmpty():
      return
    temp=self.front
    self.front=temp.next
    if self.front == None:
      self.rear=None

# Driver Code 
if __name__== '__main__': 
    q = Stack() 
    q.Push(10) 
    q.Push(20) 
    q.Push(30) 
    q.Pop()   
    print("Queue Front " + str(q.front.data)) 
    print("Queue Rear " + str(q.rear.data))
