"""Hai vi du de hoc cach viet test. Khong tinh thay 8 test RIENG cua nhom."""
import unittest
from tree_model import make_tree
from search import solve
class Examples(unittest.TestCase):
    def test_tinh_tay_doc_lap(self):
        # min(7,2)=2; min(5,9)=5; max(2,5)=5.
        for algo in ('minimax','alphabeta'):
            r=solve(make_tree([7,2,5,9]),algo)
            self.assertEqual((r['value'],r['action']),(5,'B'))
    def test_zero_is_leaf(self):
        r=solve(make_tree([0]))
        self.assertEqual((r['value'],r['action'],r['leaves'],r['expanded']),(0,None,1,0))
if __name__=='__main__': unittest.main()
