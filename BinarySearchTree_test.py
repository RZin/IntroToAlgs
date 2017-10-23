import unittest

from BinarySearchTree import BST, BSTNode, MinBSTNode,MaxBSTNode, MinMaxBSTNode

import time
class TestBST(unittest.TestCase):
    '''tests for BST'''
    def setUp(self):
        self.BST = BST(NodeType=BSTNode)
        self.BSTmin = BST(NodeType=MinBSTNode)
        self.BSTmax = BST(NodeType=MaxBSTNode)
        self.BSTminmax = BST(NodeType=MinMaxBSTNode)

    def test_single_insert(self):
        self.BST.insert(50)
        self.assertEqual(self.BST.root.key, 50)
        self.assertEqual(self.BST.root.parent, None)

    def test_structure(self):
        '''    .50.
             /     \
            25      75
            /\     / \
          10  30  60  90
         '''
        def test_structure_for_type(BST_type):
            BST_type.insert(50)
            BST_type.insert(25)
            BST_type.insert(75)
            BST_type.insert(30)
            BST_type.insert(10)
            BST_type.insert(90)
            BST_type.insert(60)
            root = BST_type.root
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

        test_structure_for_type(self.BST)
        test_structure_for_type(self.BSTmin)
        test_structure_for_type(self.BSTmax)
        test_structure_for_type(self.BSTminmax)

class TestBSTAugmented(unittest.TestCase):

    def setUp(self):
        self.BST = BST(NodeType=BSTNode)
        self.BSTmin = BST(NodeType=MinBSTNode)
        self.BSTmax = BST(NodeType=MaxBSTNode)
        self.BSTminmax = BST(NodeType=MinMaxBSTNode)
        '''    .50.
             /     \
            25      75
            /\     / \
          10  30  60  90
         '''
        # setup BST
        def insertions(BST):
            BST.insert(50)
            BST.insert(25)
            BST.insert(75)
            BST.insert(30)
            BST.insert(10)
            BST.insert(90)
            BST.insert(60)
            return BST

        self.BST = insertions(self.BST)
        self.BSTmin = insertions(self.BSTmin)
        self.BSTmax = insertions(self.BSTmax)
        self.BSTminmax = insertions(self.BSTminmax)

    def test_find(self):

        def test_find_for_type(BST_type):
            a = BST_type.find(30)
            self.assertEqual(a.key, 30)
            b = BST_type.find(50)
            self.assertEqual(b.key, 50)
            c = BST_type.find(75)
            self.assertEqual(c.key, 75)
            d = BST_type.find(90)
            self.assertEqual(d.key, 90)

        test_find_for_type(self.BST)
        test_find_for_type(self.BSTmin)
        test_find_for_type(self.BSTmax)
        test_find_for_type(self.BSTminmax)

    def test_find_min(self):

        def test_find_min_for_type(BST_type):
            a = BST_type.find_min()
            self.assertEqual(a.key, 10)
            BST_type.delete(10)
            b = BST_type.find_min()
            self.assertEqual(b.key, 25)
            BST_type.delete(25)
            c = BST_type.find_min()
            self.assertEqual(c.key, 30)

        test_find_min_for_type(self.BST)
        test_find_min_for_type(self.BSTmin)
        test_find_min_for_type(self.BSTmax)
        test_find_min_for_type(self.BSTminmax)

    def test_find_max(self):
        def test_find_max_for_type(BST_type):
            a = BST_type.find_max()
            self.assertEqual(a.key, 90)
            BST_type.delete(90)
            b = BST_type.find_max()
            self.assertEqual(b.key, 75)
            BST_type.delete(75)
            c = BST_type.find_max()
            self.assertEqual(c.key, 60)

        test_find_max_for_type(self.BST)
        test_find_max_for_type(self.BSTmin)
        test_find_max_for_type(self.BSTmax)
        test_find_max_for_type(self.BSTminmax)

    def test_next_larger(self):
        '''    .50.
             /      \
            25       75
            / \     / \
          10  30  60  90
              /\  /\
             27    65
         '''
        def test_next_larger_for_type(BST_type):
            a = BST_type.next_larger(30)
            self.assertEqual(a.key, 50)
            BST_type.insert(27)
            b = BST_type.next_larger(25)
            self.assertEqual(b.key, 27)
            c = BST_type.next_larger(60)
            self.assertEqual(c.key, 75)
            BST_type.insert(65)
            d = BST_type.next_larger(60)
            self.assertEqual(d.key, 65)

        test_next_larger_for_type(self.BST)
        test_next_larger_for_type(self.BSTmin)
        test_next_larger_for_type(self.BSTmax)
        test_next_larger_for_type(self.BSTminmax)

    def test_next_smaller(self):
        '''    .50.
             /      \
            25       75
            / \     / \
          10  30  60  90
              /\  /\
             27    65
         '''
        def test_next_smaller_for_type(BST_type):
            a = BST_type.next_smaller(50)
            self.assertEqual(a.key, 30)
            BST_type.insert(27)
            b = BST_type.next_smaller(27)
            self.assertEqual(b.key, 25)
            c = BST_type.next_smaller(75)
            self.assertEqual(c.key, 60)
            BST_type.insert(65)
            d = BST_type.next_smaller(75)
            self.assertEqual(d.key, 65)

        test_next_smaller_for_type(self.BST)
        test_next_smaller_for_type(self.BSTmin)
        test_next_smaller_for_type(self.BSTmax)
        test_next_smaller_for_type(self.BSTminmax)


    def test_delete(self):
        '''    .50.
             /      \
            25       75
            / \     / \
          10  30  60  90
         '''
        def test_delete_for_type(BST_type):

            if hasattr(BST_type.root, 'min'):
                self.assertEqual(BST_type.root.min.key, 10)
            else:
                self.assertEqual(BST_type.find_min().key, 10)

            if hasattr(BST_type.root, 'max'):
                self.assertEqual(BST_type.root.max.key, 90)
            else:
                self.assertEqual(BST_type.find_max().key, 90)

            BST_type.delete(10)

            if hasattr(BST_type.root, 'min'):
                self.assertEqual(BST_type.root.min.key, 25)
            else:
                self.assertEqual(BST_type.find_min().key, 25)

            BST_type.delete(25)

            if hasattr(BST_type.root, 'min'):
                self.assertEqual(BST_type.root.min.key, 30)
            else:
                self.assertEqual(BST_type.find_min().key, 30)

        test_delete_for_type(self.BST)
        test_delete_for_type(self.BSTmin)
        test_delete_for_type(self.BSTmax)
        test_delete_for_type(self.BSTminmax)

unittest.main()
