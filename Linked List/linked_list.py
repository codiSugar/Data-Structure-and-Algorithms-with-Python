class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def inser_at_begning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        itr = self.head
        llstr = ''
        
        while itr:
            suffix = ''
            if itr.next:
                suffix += ' ---> '
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def inser_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)    
    def insert_at_middle(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.inser_at_begning()
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
            
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.next
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
            
    def insert_bulk_values(self,data_list):
        self.head = None
        for data in data_list:
            self.inser_at_end(data)
            
            
            
            
            
            
root = LinkedList()

# root.inser_at_begning(5)
# root.inser_at_begning(15) 
root.inser_at_end(10)
root.inser_at_end(5)
root.inser_at_end(100)
root.insert_at_middle(1,500)
root.remove_at(2)
root.insert_bulk_values(['madhu','anushka','Sagar','manisha','valentina'])
root.print() 
print(root.get_length())       
        