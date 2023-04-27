class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, data):
        # we will create a node
        node = Node(data)
        if(self.head == None):
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return node
    def printList(self):
        copy = self.head
        while copy is not None:
            print(copy.data,end='->')
            copy = copy.next
    
    def InsertAtEnd(self, ref):
        copy = self.head
        while copy.next is not None:
            copy = copy.next
        copy.next = ref 
    
    def FindCyclePresentOrNot(self):
        ptr1 = self.head
        ptr2 = self.head
        while ptr2.next.next is not None:
            ptr2 = ptr2.next.next
            ptr1 = ptr1.next
            # print("ptr2=",ptr2.data,"  ptr1=",ptr1.data)
            if(ptr2 == ptr1):
                print("Cycle found at", ptr1.data)
                return ptr1
        return None
    
    def findMeetingPoint(self, ptr):
        if(ptr == None):
            print("No cycle Found!")
            return
        start = self.head
        while start!=ptr:
            ptr = ptr.next
            start = start.next
        print("Cycle started At", ptr.data)
        
    def removeCycle(self, ptr):
        if(ptr == None):
            print("No cycle Found!")
            return
        start = self.head
        while start.next!=ptr.next:
            ptr = ptr.next
            start = start.next
        ptr.next = None
        print("Cycle Removed!")
x = LinkedList()
x.insertAtBeginning(6)
x.insertAtBeginning(7)
x.insertAtBeginning(8)
x.insertAtBeginning(5)
x.insertAtBeginning(4)

copyNode = x.insertAtBeginning(3)

x.insertAtBeginning(2)
x.insertAtBeginning(1)

x.InsertAtEnd(copyNode)
# x.printList()
ptr = x.FindCyclePresentOrNot()
x.findMeetingPoint(ptr)
print()
x.removeCycle(ptr)
print()
x.printList()