import sys


class linkedlist1 :
    class Node :
        data = 0
        next = None
        def __init__(self, data) :
            self.data = data
            self.next = None
    head = None
    tail = None
    size = 0
    
    def addFirst(self, data) :
        newNode = linkedlist1.Node(data)
        linkedlist1.size += 1
        if (linkedlist1.head == None) :
            linkedlist1.head = newNode
            linkedlist1.tail = newNode
            return
        newNode.next = linkedlist1.head
        linkedlist1.head = newNode
        
    def addLast(self, data) :
        newNode = linkedlist1.Node(data)
        linkedlist1.size += 1
        if (linkedlist1.head == None) :
            linkedlist1.head = newNode
            linkedlist1.tail = newNode
            return
        linkedlist1.tail.next = newNode
        linkedlist1.tail = newNode
        
    def atParticular(self, idx,  data) :
        newNode = linkedlist1.Node(data)
        linkedlist1.size += 1
        if (idx == 0) :
            self.addFirst(data)
            return
        temp = linkedlist1.head
        i = 0
        while (i < idx - 1) :
            i += 1
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
        
    def  delFirst(self) :
        if (linkedlist1.size == 0) :
            print("Linked List does not exist")
            return sys.maxsize
        elif(linkedlist1.size == 1) :
            val = linkedlist1.head.data
            linkedlist1.head = None
            linkedlist1.tail = None
            linkedlist1.size = 0
            return val
        val = linkedlist1.head.data
        linkedlist1.head = linkedlist1.head.next
        linkedlist1.size -= 1
        return val
        
    def  delLast(self) :
        if (linkedlist1.size == 0) :
            print("ll is empty")
            return sys.maxsize
        elif(linkedlist1.size == 1) :
            val = linkedlist1.head.data
            linkedlist1.head = None
            linkedlist1.tail = None
            linkedlist1.size = 0
            return val
        temp = linkedlist1.head
        i = 0
        while (i < linkedlist1.size - 2) :
            temp = temp.next
            i += 1
        val = temp.next.data
        temp.next = None
        linkedlist1.tail = temp
        linkedlist1.size -= 1
        return val
        
    def delatPart(self, position) :
        if (linkedlist1.head == None) :
            return
        temp = linkedlist1.head
        if (position == 0) :
            linkedlist1.head = temp.next
            return
        i = 0
        while (temp != None and i < position - 1) :
            temp = temp.next
            i += 1
        if (temp == None or temp.next == None) :
            return
        next = temp.next.next
        temp.next = next
        
    def deleteNthNode(self, n) :
        sz = 0
        temp = linkedlist1.head
        while (temp != None) :
            temp = temp.next
            sz += 1
        if (n == sz) :
            linkedlist1.head = linkedlist1.head.next
            return
        i = 0
        t = sz - n
        prev = linkedlist1.head
        while (i < t) :
            prev = prev.next
            i += 1
        prev.next = prev.next.next
        return
    
    def reverse(self) :
        prev = None
        linkedlist1.curr = linkedlist1.head
        linkedlist1.tail = linkedlist1.head
        next = None
        while (curr != None) :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        linkedlist1.head = prev
        
    def atmiddle1(self) :
        cnt = 0
        temp = linkedlist1.head
        while (temp != None) :
            cnt += 1
            temp = temp.next
        mid = int(cnt / 2)
        if ((cnt & 1) == 0) :
            mid -= 1
        temp = linkedlist1.head
        while (mid > 0) :
            temp = temp.next
            
    def atmiddle2(self) :
        A = linkedlist1.head
        B = linkedlist1.head
        while (B != None and B.next != None and B.next.next != None) :
            A = A.next
            B = B.next.next
        print(A, end ="")
        
    def search(self, key) :
        i = 0
        temp = linkedlist1.head
        while (temp != None) :
            if (key == temp.data) :
                return
            else :
                temp.next = temp
                i += 1
                
    def Print(self) :
        temp = linkedlist1.head
        while (temp != None) :
            print(str(temp.data) + "->", end ="")
            temp = temp.next
        print("null")
    @staticmethod
    def main( args) :
        ll = linkedlist1()
        ll.addFirst(1)
        ll.addFirst(2)
        ll.addLast(6)
        ll.addLast(9)
        ll.atParticular(3, 5)
        ll.atParticular(4, 8)
        ll.Print()
        ll.delatPart(4)
        ll.Print()
        print(ll.size)
        ll.delFirst()
        ll.Print()
        print(ll.size)
        ll.delLast()
        ll.Print()
        print(ll.size)
        ll.search(6)
        ll.reverse()
        ll.Print()
        ll.deleteNthNode(3)
        ll.Print()
        ll.atmiddle1()
        ll.atmiddle2()
    

if __name__=="__main__":
    linkedlist1.main([])
