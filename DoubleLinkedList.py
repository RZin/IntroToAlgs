NIL = '/'
import random
import time

class Node(object):

    def __init__(self, prev, key, next):
        self.prev = prev
        self.key = key
        self.next = next

    def __repr__(self):
        return 'Node ' + str(self.key)

    def next_node(self):
        return self.next

class DoubleLinkedList(object):

    def __init__(self, fst:int):
        node = Node(NIL, fst, NIL)
        self.head = node
        self.tail = node
        self.nodes = set()
        self.nodes.add(node)

    def __repr__(self):
        node = self.head
        result = str(node)
        while node is not NIL:
            result += ' <-> '+str(node)
            node = node.next
        return result

    def get_head(self):
        return self.head
    def get_tail(self):
        return self.tail
    def get_nodes(self):
        return self.nodes

    def insert(self, x:int): #x val
        #self.nodes.add(Node())
        xnext = self.get_head()
        xprev = NIL
        if self.head != NIL:
            c = Node(xprev, x, xnext)
            self.head.prev = c
        self.head = c
        self.nodes.add(c) # add

    def delete(self, x:Node):
        if x.prev != NIL:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != NIL:
            x.next.prev = x.prev

    def search(self, k):
        x = self.head
        while x != NIL and x.key != k:
            x = x.next

def build_list(first_key):
    DLL = DoubleLinkedList(1)
    # print(DLL.nodes)
    return DLL

if __name__ == '__main__':

    def random_setup(tree, upper_bound, nodes_num):
        tree_list = list(random.sample(range(upper_bound), nodes_num))
        random.shuffle(tree_list)
        # tree_list.sort()
        s = time.time()
        while tree_list:
            tree.insert(tree_list.pop())
            # print(tree.check_balanced(tree.root))
        p = time.time()
        print('insertion time', p-s)
        return tree

    DLL = DoubleLinkedList(1)
    DLL = random_setup(DLL, upper_bound=1000, nodes_num=50)
    print('head is ', DLL.head)
    print('tail is ', DLL.tail)
    print('DLL is ',DLL)
