class Node:
  def __init__(self, value):
    self.data = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def printlist(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next

  def rotate(self, k, l):
    if k != 0 and k < l:
      curr = self.head
      cnt = 1
      while (cnt < k and curr is not None):
        curr = curr.next
        cnt+=1
      kthnode=curr
      while (curr.next is not None):
        curr=curr.next
      curr.next=self.head
      self.head=kthnode.next
      kthnode.next=None

llist=LinkedList()
for i in range(60,0,-10):
  llist.push(i)
print("Original list")
llist.printlist()
llist.rotate(4, 6)
print("New list")
llist.printlist()
