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
        self.nil = NIL
        self.cells = set()
        self.cells.add(self.nil)
        self.cells.add(cell)
        self.head = cell
        self.tail = cell
        self.point = cell

    def get_head(self):
        return self.head
    def get_tail(self):
        return self.tail
    def get_cells(self):
        return self.cells

    def insert_cell(self, x:int): # x val
        #self.cells.add(Cell())
        xnext = self.head
        xprev = self.nil
        if self.head != self.nil:
            c = Cell(xprev, x, xnext)
            self.cells.add(c)  # add to the set
            self.head.prev = c # bound prev to c
        self.head = c
        print('inserting cell {0} '.format(c.key))

    def delete_cell(self, x:Cell): # change to int
        if x.prev != self.nil:
            # its prev's next now its next
            x.prev.next = x.next
        else:
            # just move head
            self.head = x.next
        if x.next != self.nil:
            # its next's prev now its prev
            x.next.prev = x.prev
        # remove cell from set
        self.cells.remove(self.point)
        # unbound spoint from current to head
        self.point = self.head
        print('cell {0} has been deleted'.format(x.key))

    def search(self, k:int):
        x = self.head # Cell
        while x != self.nil and x.key != k:
            x = x.next
        self.point = x
        return self.point

def build_list(first_key):
    DLL = DoubleLinkedList(1)
    print(DLL.cells)
    return DLL

if __name__ is '__main__':
    # make sure insertions are unique
    DLL = build_list(1)
    DLL.insert_cell(4)
    DLL.insert_cell(16)
    DLL.insert_cell(9)
    DLL.insert_cell(25)
    to_delete = DLL.search(9)
    DLL.delete_cell(to_delete)
    print('done')
