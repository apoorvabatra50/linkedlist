class Node:
    def  __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
    def add(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=Node(data)

    def printll(self):
        curr=self.head
        while(curr.next!=None):
            print(curr.data)
            curr=curr.next
        print(curr.data)
    def findmid(self):
        curr=self.head
        mid= self.head
        while(curr.next!=None):
            mid=mid.next
            if curr.next.next!=None:
                curr=curr.next.next
            else:
                curr=curr.next

        print(mid.data)

ll=LinkedList()
for i in range(1,101):
    ll.add(i)

ll.findmid()
