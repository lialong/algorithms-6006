class Node:
    def __init__(self, name: str):
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self, head: Node):
        self.head = head
    
def get_list(num):
    head = Node(0)
    pre = head
    for i in range(1, num):
        node = Node(i)        
        pre.next = node
        pre = node
    list = LinkedList(head)
    list.size = num
    return list

def print_list(L):
    node = L.head
    for _ in range(0, L.size):
        print(node.name)
        node = node.next        
    
def reorder_students(L):
    n = L.size//2
    a = L.head
    for _ in range(1, n):
        a = a.next
    b = a.next
    x_p,x = a,b
    for _ in range(0, n):
        x_n = x.next
        x.next = x_p
        x_p, x = x, x_n        
    a.next = x_p
    b.next = None
        

if __name__ == "__main__":
    list = get_list(10);
    print_list(list)
    print("---------------------------")
    reorder_students(list)
    print_list(list)
