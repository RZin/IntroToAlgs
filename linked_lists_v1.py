NIL = '/'

class Cell(object):

    def __init__(self, prev, key, next):
        self.prev = prev
        self.key = key
        self.next = next

    def __repr__(self):
        l = [str(self.prev), \
                 str(self.key), \
                 str(self.next)]
        return str(l)

    def __str__(self):
        l = list(str(self.prev), \
                 str(self.key), \
                 str(self.next))
        return str(l)


class DoubleLinkedList(object):

    def __init__(self, fst:int):
        cell = Cell(NIL, fst, NIL)
        self.head = cell
        self.tail = cell
        self.cells = set()
        self.cells.add(cell)

    def get_head(self):
        return self.head
    def get_tail(self):
        return self.tail
    def get_cells(self):
        return self.cells

    def insert_cell(self, x:int): #x val
        #self.cells.add(Cell())
        xnext = self.get_head()
        xprev = NIL
        if self.head != NIL:
            c = Cell(xprev, x, xnext)
            self.head.prev = Cell(xprev, x, xnext) # to change

        self.head = c
        self.cells.add(c) # add

    def delete_cell(self, x:Cell):
        if x.prev != NIL:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != NIL:
            x.next.prev = x.prev

    def search(self, k):
        x = self.head
        while x != NIL and x.key != k:
            x = x.next_cell

def build_list(first_key):
    DLL = DoubleLinkedList(1)
    print(DLL.cells)
    return DLL

if __name__ is '__main__':
    DLL = build_list(1)
    DLL.insert_cell(4)
    print(DLL)

    new_branch = True