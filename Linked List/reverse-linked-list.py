class Node:
  def __init__(self, value):
    self.data=value
    self.next=None

class LinkedList:
  def __init__(self):
    self.head=None
  
  def push(self, value):
    new=Node(value)
    new.next=self.head
    self.head=new

  def printlist(self):
    temp=self.head
    while(temp):
      print(temp.data)
      temp=temp.next

  def reverse(self):
    prev=None
    curr=self.head
    next=None
    while(curr != None):
      next=curr.next
      curr.next=prev
      prev=curr
      curr=next
    self.head=prev

llist=LinkedList()
for i in range(60,0,-10):
  llist.push(i)
print("Original list")
llist.printlist()
llist.reverse()
print("New list")
llist.printlist()
