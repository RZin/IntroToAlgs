import time
import random

class BSTNode(object):

    """A node in the vanilla BST tree."""

    def __init__(self, parent, key):
        """Creates a node.
        Args:
            parent: The node's parent,
            k: The key of the node.
        """
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node ' + str(self.key)

    def find(self, key):
        """Finds and returns the --node-- with key from the subtree rooted at this node.
        Args:
            key: The key of the node we want to find.
        """
        if key == self.key:
            return self

        elif key < self.key:
            # go left
            if self.left is None:
                return None
            else:
                return self.left.find(key)
        else:
            # go right
            if self.right is None:
                return None
            else:
                return self.right.find(key)

    def find_min(self):
        """
        Returns:
            The node with the minimum key."""
        current = self
        # go left until it's None
        while current.left is not None:
            current = current.left
        return current

    def find_max(self):
        """
        Returns:
            The node with the maximum key."""
        current = self
        # go right until it's None
        while current.right is not None:
            current = current.right
        return current

    def next_larger(self) :
        """Returns the node with the next larger key
        (the successor) in the BST.
        """
        if self.right is not None:
            # min of right's child
            return self.right.find_min()
        current = self
        # elif None: go up
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def next_smaller(self) :
        """Returns the node with the next smaller key
        (the predecessor) in the BST.
        """
        if self.left is not None:
            # max of min's child
            return self.left.find_max()
        current = self
        # elif None: go up
        while current.parent is not None and current is current.parent.left:
            current = current.parent
        return current.parent

    def insert(self, node):
        '''inserts node into the tree, and restructures'''
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                # insert left
                node.parent = self
                self.left = node
            else: # go left
                self.left.insert(node)
        else:
            if self.right is None:
                # insert right
                node.parent = self
                self.right = node
            else: # go right
                self.right.insert(node)

    def delete (self):
        '''removes node from the tree, and restructures'''
        if self.left is None or self.right is None:
            # Case 1,2: had no child or one
            if self is self.parent.left:
                # from parent left
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    # Case: 1 had one child
                    self.parent.left.parent = self.parent
            else: # Case: 3 self is self.parent.right
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            # finally
            return self
        else:
            # Case 4: had both
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()

    '''
    Case1  
      .55..   
     /     \  
    *X*    83
    /\     / \
     34   82  
     /\  /  \ 
        56    
        /\   
    Case2  
      .55..   
     /     \  
    *X*    83
    /\     / \ 
        
    Case3
      .55..   
     /     \  
    26     *X*    
    /\     / \
     34   82  
     /\  /  \ 
     
    Case4
      .55..   
     /     \  
    26      *X*  
    /\     / \
     34   82  96  
     /\  / \ / \ 
             
         '''

class MinBSTNode(BSTNode):
    '''A node implemented to keep track of the minimum node from current'''
    def __init__(self, parent, key):
        super(MinBSTNode, self).__init__(parent, key)
        self.min = self

    def find_min(self):
        """
        Returns:
            The node with the minimum key."""
        return self.min

    def insert(self, node):
        if node is None:
            return
        if node.key < self.key:
            # Updates the min of this node if the inserted node has a smaller key.
            if node.key < self.min.key:
                self.min = node
            if self.left is None:
                # insert left
                node.parent = self
                self.left = node
            else: # go right
                self.left.insert(node)
        else:
            if self.right is None:
                # insert right
                node.parent = self
                self.right = node
            else: # go right
                self.right.insert(node)

    def delete (self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                # from parent left
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    # Case: 1 had one child
                    self.parent.left.parent = self.parent
                    self.parent.min = self.parent.left.min
                else:# Case: 2 had no children
                    self.parent.min = self.parent
                # Propagates the changes upwards.
                current = self.parent
                while current.parent is not None and current is current.parent.left:
                    current.parent.min = current.min
                    current = current.parent
            else: # Case: 3 self is self.parent.right
                self.parent.right = self.left or self.right
                if self.parent.right is not None: # mb this check isn't needed
                    self.parent.right.parent = self.parent
                    return self
        else:
            # Case 4: had both
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()

# class MinBSTNode(BSTNode):
#     '''A node implemented to keep track of the minimum node from current'''
#
#     def __init__(self, parent, key):
#         super(MinBSTNode, self).__init__(parent, key)
#         self.min = self

class MaxBSTNode(BSTNode):
    '''A node implemented to keep track of the minimum node from current'''
    def __init__(self, parent, key):
        super(MaxBSTNode, self).__init__(parent, key)
        self.max = self

    def find_max(self):
        """
        Returns:
            The node with the maximum key."""
        return self.max

    def insert(self, node):
        if node is None:
            return
        if node.key < self.key:
            # Updates the min of this node
            # if the inserted node has a smaller key.
            if self.left is None:
                # insert left
                node.parent = self
                self.left = node
            else: # go right
                self.left.insert(node)
        else: # if node.key >= self.key
            # Updates the max of this node
            # if the inserted node has a larger key.
            if node.key > self.max.key:
                self.max = node
            if self.right is None:
                # insert right
                node.parent = self
                self.right = node
            else: # go right
                self.right.insert(node)

    def delete (self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                # from parent left
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    # Case: 1 had one child
                    self.parent.left.parent = self.parent
            else: # Case: 3 from parent right
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
                    self.parent.max = self.parent.right.max
                else: # self.parent.right is None
                    self.parent.max = self.parent
                # Propagates the changes upwards.
                current = self.parent
                while current.parent is not None and current is current.parent.right:
                    current.parent.max = current.max
                    current = current.parent
            return self
        else:
            # Case 4: had both
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()

class MinMaxBSTNode(BSTNode):
    '''A node stores minimum and maximum node from current'''
    def __init__(self, parent, key):
        super(MinMaxBSTNode, self).__init__(parent, key)
        self.min = self
        self.max = self

    def find_min(self):
        """
        Returns:
            The node with the minimum key."""
        return self.min

    def find_max(self):
        """
        Returns:
            The node with the maximum key."""
        return self.max

    def insert(self, node):
        if node is None:
            return
        if node.key < self.key:
            # Updates the min of this node
            # if the inserted node has a smaller key.
            if node.key < self.min.key:
                self.min = node
            if self.left is None:
                # insert left
                node.parent = self
                self.left = node
            else: # go right
                self.left.insert(node)
        else: # if node.key >= self.key
            # Updates the max of this node
            # if the inserted node has a larger key.
            if node.key > self.max.key:
                self.max = node
            if self.right is None:
                # insert right
                node.parent = self
                self.right = node
            else: # go right
                self.right.insert(node)

    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                # from parent left
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    # Case: 1 had one child
                    self.parent.left.parent = self.parent
                    self.parent.min = self.parent.left.min
                else:  # Case: 2 had no children
                    self.parent.min = self.parent
                # Propagates the changes upwards.
                current = self.parent
                while current.parent is not None and current is current.parent.left:
                    current.parent.min = current.min
                    current = current.parent
            else: # Case: 3 from parent right
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
                    self.parent.max = self.parent.right.max
                else: # self.parent.right is None
                    self.parent.max = self.parent
                # Propagates the changes upwards.
                current = self.parent
                while current.parent is not None and current is current.parent.right:
                    current.parent.max = current.max
                    current = current.parent
            return self
        else:
            # Case 4: had both
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()


class BST(object):

    def __init__(self, NodeType=BSTNode) :
        self.root = None
        self.NodeType = NodeType

    def __repr__(self):
        return 'BST of type ' + str(self.NodeType)

    def find(self, k) :
        ''':returns node with key:k'''
        return self.root and self.root.find(k)

    def find_min(self) :
        """Returns the minimum node of this BST."""
        return self.root and self.root.find_min()

    def find_max(self) :
        """Returns the maximum node of this BST."""
        return self.root and self.root.find_max()

    def insert(self, k):
        node = self.NodeType(None, k)
        if self.root is None:
            # The root's parent Is None.
            self.root = node
        else:
            self.root.insert(node)

    def delete(self, k):
        """Deletes and returns a node with key k if it exists from the BST.
        Args:
            k: The key of the node that we want to delete.
        """
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            pseudoroot = self.NodeType(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()

    def next_larger(self, k) :

        """Returns the node that contains the next larger key in
        the BST in relation to the node with key k.
        Args:
            k: The key of the node of which the successor is to be found.
        Returns:
            The successor node.
        """
        node = self.find(k)
        if node is not None:
            return node.next_larger()

    def next_smaller(self, k) :
        """
        Args:
            k: The key of the node
            of which the predecessor is to be found.
        Returns:
            The predecessor node.
        """
        node = self.find(k)
        if node is not None:
            return node.next_smaller()

    def DFS_traverse(self, node, visited):
        ''':returns all the nodes in tree'''
        # it is tree, so we know that node is never encountered twice
        visited.append(node)
        if node.left is not None:
            visited = self.DFS_traverse(node.left, visited)
        if node.right is not None:
            visited = self.DFS_traverse(node.right, visited)
        return visited

    def BFS_traverse(self, node, visited):
        ''':returns all the nodes in tree'''
        # it is tree, so we know that node is never encountered twice
        queue = [node]
        while queue:
            current = queue.pop(0)
            visited.append(current)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return visited

    def __str__(self):

        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
                            node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle - 2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
                    [left_line + ' ' * (width - left_width - right_width) +
                     right_line
                     for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width

        return '\n'.join(recurse(self.root)[0])+'\n'

    def __repr__(self):
        return 'TreeObject, root:' + str(self.root) + ' NodeType: '+str(self.NodeType)

if __name__ == '__main__':
    '''    .50.
         /     \
        25      75
        /\     / \
      10  30  60  90
     '''
    BST = BST(NodeType=BSTNode)

    def random_setup(tree, upper_bound, nodes_num):
        tree_list = list(random.sample(range(upper_bound), nodes_num))
        random.shuffle(tree_list)
        # tree_list.sort()

        s = time.time()
        while tree_list:
            tree.insert(tree_list.pop())
        p = time.time()
        print('insertion time', p - s)

        return tree

    BST = random_setup(BST, upper_bound=1000, nodes_num=50)
    print(BST)
    # visited = BST.DFS_traverse(BST.root, [])
    # visited = BST.BFS_traverse(BST.root, [])
    def test_find_min_time(tree):
        s = time.time()
        for i in range(100000):
            node = tree.find_min()
        p = time.time()
        print('find min time', p-s)
        return p-s

    # test_find_min_time(BST)
