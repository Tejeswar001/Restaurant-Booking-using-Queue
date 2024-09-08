class NODE():
    def __init__(self,name,people):
        self.name = name
        self.people = people
        self.next = None
    
class QUEUE():
    def __init__(self):
        self.head = None
    
    def Enqueue(self,name,people):
        new = NODE(name,people)
        if self.head is None:
            self.head = new
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new
    
    def Dequeue(self):
        if self.head is None:
            print("Queue is Empty")
        else:
            node = self.head
            self.head = node.next
    
    def Print_test(self):
        queue:list = []
        if self.head is None:
            return "Empty"
        else:
            node = self.head
            while node:
                print(node.name,node.people)
                queue.append(f"{node.name} booking for {node.people}")
                node = node.next
            return queue
    
    def is_empty(self):
        if self.head is None:
            return True
        return False