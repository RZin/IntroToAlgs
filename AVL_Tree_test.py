import unittest

from AVL_Tree import AVL, AVLNode

import time

class TestTree(unittest.TestCase):
    '''tests for BST'''
    def setUp(self):
        self.AVL = AVL(NodeType=AVLNode)

    def test_single_insert(self):
        self.AVL.insert(50)
        self.assertEqual(self.AVL.root.key, 50)
        self.assertEqual(self.AVL.root.parent, None)

    def test_structure(self):
        '''    .50.
             /     \
            25      75
            /\     / \
          10  30  60  90
         '''
        def test_structure_for_type(tree_type):
            tree_type.insert(50)
            tree_type.insert(25)
            tree_type.insert(75)
            tree_type.insert(30)
            tree_type.insert(10)
            tree_type.insert(90)
            tree_type.insert(60)
            root = tree_type.root
            self.assertEqual(root.key, 50)
            self.assertEqual(root.parent, None)
            self.assertEqual(root.left.key, 25)
            self.assertEqual(root.left.parent.key, 50)
            self.assertEqual(root.left.left.key, 10)
            self.assertEqual(root.left.left.parent.key, 25)
            self.assertEqual(root.left.right.key, 30)
            self.assertEqual(root.left.right.parent.key, 25)
            self.assertEqual(root.right.key, 75)
            self.assertEqual(root.right.parent.key, 50)
            self.assertEqual(root.right.left.key, 60)
            self.assertEqual(root.right.left.parent.key, 75)
            self.assertEqual(root.right.right.key, 90)
            self.assertEqual(root.right.right.parent.key, 75)

        test_structure_for_type(self.AVL)


class TestTreeAugmented(unittest.TestCase):

    def setUp(self):
        self.AVL = AVL(NodeType=AVLNode)

        '''    .50.
             /     \
            25      75
            /\     / \
          10  30  60  90
         '''
        # setup AVL
        def insertions(tree):
            tree.insert(50)
            tree.insert(25)
            tree.insert(75)
            tree.insert(30)
            tree.insert(10)
            tree.insert(90)
            tree.insert(60)
            return tree

        self.AVL = insertions(self.AVL)


    def test_find(self):

        def test_find_for_type(tree_type):
            a = tree_type.find(30)
            self.assertEqual(a.key, 30)
            b = tree_type.find(50)
            self.assertEqual(b.key, 50)
            c = tree_type.find(75)
            self.assertEqual(c.key, 75)
            d = tree_type.find(90)
            self.assertEqual(d.key, 90)

        test_find_for_type(self.AVL)

    def test_find_min(self):

        def test_find_min_for_type(tree_type):
            a = tree_type.find_min()
            self.assertEqual(a.key, 10)
            tree_type.delete(10)
            b = tree_type.find_min()
            self.assertEqual(b.key, 25)
            tree_type.delete(25)
            c = tree_type.find_min()
            self.assertEqual(c.key, 30)

        test_find_min_for_type(self.AVL)

    def test_find_max(self):
        def test_find_max_for_type(tree_type):
            a = tree_type.find_max()
            self.assertEqual(a.key, 90)
            tree_type.delete(90)
            b = tree_type.find_max()
            self.assertEqual(b.key, 75)
            tree_type.delete(75)
            c = tree_type.find_max()
            self.assertEqual(c.key, 60)

        test_find_max_for_type(self.AVL)


    def test_next_larger(self):
        '''    .50.
             /      \
            25       75
            / \     / \
          10  30  60  90
              /\  /\
             27    65
         '''
        def test_next_larger_for_type(tree_type):
            a = tree_type.next_larger(30)
            self.assertEqual(a.key, 50)
            tree_type.insert(27)
            b = tree_type.next_larger(25)
            self.assertEqual(b.key, 27)
            c = tree_type.next_larger(60)
            self.assertEqual(c.key, 75)
            tree_type.insert(65)
            d = tree_type.next_larger(60)
            self.assertEqual(d.key, 65)

        test_next_larger_for_type(self.AVL)


    def test_next_smaller(self):
        '''    .50.
             /      \
            25       75
            / \     / \
          10  30  60  90
              /\  /\
             27    65
         '''
        def test_next_smaller_for_type(tree_type):
            a = tree_type.next_smaller(50)
            self.assertEqual(a.key, 30)
            tree_type.insert(27)
            b = tree_type.next_smaller(27)
            self.assertEqual(b.key, 25)
            c = tree_type.next_smaller(75)
            self.assertEqual(c.key, 60)
            tree_type.insert(65)
            d = tree_type.next_smaller(75)
            self.assertEqual(d.key, 65)

        test_next_smaller_for_type(self.AVL)

    def test_delete(self):
        '''    .50.
             /      \
            25       75
            / \     / \
          10  30  60  90
         '''
        def test_delete_for_type(tree_type):

            if hasattr(tree_type.root, 'min'):
                self.assertEqual(tree_type.root.min.key, 10)
            else:
                self.assertEqual(tree_type.find_min().key, 10)

            if hasattr(tree_type.root, 'max'):
                self.assertEqual(tree_type.root.max.key, 90)
            else:
                self.assertEqual(tree_type.find_max().key, 90)

            tree_type.delete(10)

            if hasattr(tree_type.root, 'min'):
                self.assertEqual(tree_type.root.min.key, 25)
            else:
                self.assertEqual(tree_type.find_min().key, 25)

            tree_type.delete(25)

            if hasattr(tree_type.root, 'min'):
                self.assertEqual(tree_type.root.min.key, 30)
            else:
                self.assertEqual(tree_type.find_min().key, 30)

        test_delete_for_type(self.AVL)

unittest.main()
