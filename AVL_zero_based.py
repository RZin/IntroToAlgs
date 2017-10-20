#import random, math
# todo make parent attr
outputdebug = False

def debug(msg):

    if outputdebug:
        print(msg)

class Node():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    def __repr__(self):
        return 'Node:'+str(self.key)

class AVLTree():

    def __init__(self, *args):
        self.node = None
        self.height = 0
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def __repr__(self):
        return 'AVLsubtree of:'+str(self.node.key)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 1)

    def insert(self, key):
        tree = self.node
        # newnode = Node(key)
        if tree == None:
            self.node = Node(key) # Node(key)
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        else:
            debug("Key [" + str(key) + "] already in tree.")

        self.rebalance()

    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate right pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right')
        # before
        A = self.node
        B = self.node.left.node
        T = B.right.node
        # after
        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left')
        # before
        A = self.node
        B = self.node.right.node
        T = B.left.node
        # after
        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                               self.node.right.height) + 1
            pass
        else:
            self.height = 0

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                     self.node.left.update_balances()
                if self.node.right != None:
                     self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
            pass
        else:
            self.balance = 0

    def pop_min(self):
        # if left is not leaf
        if self.node.left.node != None:
            key = self.node.left.pop_min() # pull from leaf
        # if left is leaf
        else:
            debug("popping ... " + str(self.node.key))
            # if leaf
            if self.node.left.node == None and self.node.right.node == None:
                key = self.node.key
                self.node = None
            # if has leaf on the right
            elif self.node.left.node == None:
                key = self.node.key
                self.node = self.node.right.node
            elif self.node.right.node == None:
                raise ValueError('self.node.right.node == None, shouldn"t be here')
        self.rebalance()
        return key

    def find_min(self):
        '''returns key of the minimum element'''
        # if left is not leaf
        if self.node.left.node != None:
            key = self.node.left.find_min() # pull from leaf
        # if left is leaf
        else:
            debug("popping ... " + str(self.node.key))
            # if nothing on the left
            if self.node.key:
                key = self.node.key
            else:
                print('no key at node', self.node)
                raise ValueError('no key at node ', self.node)
        return key

    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None:
            if self.node.key == key:
                debug("Deleting ... " + str(key))
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # sanity check
                        debug("Found replacement for " + str(key) + " -> " + str(replacement.key))
                        self.node.key = replacement.key

                        # replaced. Now delete the key from right child
                        self.node.right.delete(replacement.key)

                self.rebalance()
                return
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        '''
        Find the biggest valued node in LEFT child
        '''
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        '''
        Find the smallest valued node in RIGHT child
        '''
        node = node.right.node
        if node != None: # just a sanity check

            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if(self.node != None):
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')

# todo add def min() to tree

# Usage example
if __name__ == "__main__":
    a = AVLTree()
    print("----- Inserting -------")
    #inlist = [5, 2, 12, -4, 3, 21, 19, 25]
    # inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
    inlist = [1, 2, 3, 4, 5, 6]
    for i in inlist:
         a.insert(i)

    # a.display()

    print("----- Deleting -------")
    # print("Inorder traversal:", a.inorder_traverse())

    a.pop_min()
    a.pop_min()
    a.pop_min()
    # a.delete(1)
    # a.delete(2)
    # a.delete(3)
    a.display()

    print()
    # print("Input            :", inlist)
    # print("deleting ...       ", 3)
    # print("deleting ...       ", 4)
    print("Inorder traversal:", a.inorder_traverse())

'''
----- Inserting -------
  4 [3:0]
-- < 2 [2:0]
---- < 1 [1:0]
---- > 3 [1:0]
-- > 5 [2:-1]
---- > 6 [1:0]
----- Deleting -------
  5 [2:0]
-- < 4 [1:0]
-- > 6 [1:0]

Input            : [1, 2, 3, 4, 5, 6]
deleting ...        3
deleting ...        4
Inorder traversal: [4, 5, 6]


----- Inserting -------
  4 [2:0]
-- < 2 [1:0]
---- < 1 [0:0] L
---- > 3 [0:0] L
-- > 5 [1:-1]
---- > 6 [0:0] L
----- Deleting -------
  5 [1:0]
-- < 4 [0:0] L
-- > 6 [0:0] L

Input            : [1, 2, 3, 4, 5, 6]
deleting ...        3
deleting ...        4
Inorder traversal: [4, 5, 6]'''