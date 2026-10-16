"""Kiem thu mau chuc nang; sinh vien tu viet them test_nhom.py."""
import unittest
from tree_model import Node,make_tree,walk,validate_tree
from search import solve
class Tests(unittest.TestCase):
    def test_zero_leaf(self):
        r=solve(make_tree([0]));self.assertEqual(r['value'],0);self.assertIsNone(r['action'])
    def test_positive_leaf(self): self.assertEqual(solve(make_tree([8]))['visited'],1)
    def test_negative_max(self): self.assertEqual(solve(make_tree([-9,-4]))['value'],-4)
    def test_min_root(self): self.assertEqual(solve(make_tree([-9,-4],'MIN'))['value'],-9)
    def test_equal_lr(self): self.assertEqual(solve(make_tree([6,6]))['action'],'L01')
    def test_equal_rl(self): self.assertEqual(solve(make_tree([6,6]),order='RL')['action'],'L02')
    def test_nested(self): self.assertEqual(solve(make_tree([7,2,5,9]))['value'],5)
    def test_trace_disabled(self): self.assertEqual(solve(make_tree([1,3]))['trace'],[])
    def test_trace_same(self):
        for algo in ('minimax','alphabeta'):
            a=solve(make_tree([4,7,2,8]),algo);b=solve(make_tree([4,7,2,8]),algo,trace=True)
            for key in ('value','action','visited','expanded','leaves','cutoffs'): self.assertEqual(a[key],b[key])
    def test_input_unchanged(self):
        a=[7,2,5,9];root=make_tree(a);solve(root);self.assertEqual(a,[7,2,5,9])
    def test_counts(self):
        for a in ('minimax','alphabeta'):
            r=solve(make_tree([7,2,5,9]),a);self.assertEqual(r['visited'],r['expanded']+r['leaves'])
    def test_mm_visits_all(self):
        r=solve(make_tree(range_to_list()),'minimax');self.assertEqual((r['visited'],r['leaves']),(15,8))
    def test_mm_has_no_cuts(self):
        r=solve(make_tree([7,2,5,9]),'minimax');self.assertEqual((r['cutoffs'],r['pruned_branches']),(0,0))
    def test_action_with_false_tie(self):
        r=solve(make_tree([7,9,7,1]));self.assertEqual((r['value'],r['action']),(7,'A'))
    def test_bound_direction(self):
        r=solve(make_tree([7,9,7,1]));self.assertEqual(r['returns']['B']['bound'],'UPPER')
    def test_unvisited(self):
        root=make_tree([7,9,7,1]);r=solve(root)
        self.assertEqual(set(r['visited_nodes'])|set(r['unvisited_nodes']),{n.name for n in walk(root)})
    def test_no_fake_prune_on_last(self):
        r=solve(make_tree([7,9,10,1]));self.assertEqual(r['cutoffs'],0)
    def test_mm_pv(self):
        r=solve(make_tree([7,2,5,9]),'minimax');self.assertEqual(r['principal_variation'],['R','B','L03'])
    def test_ab_no_fake_pv(self): self.assertIsNone(solve(make_tree([7,2,5,9]))['principal_variation'])
    def test_invalid_leaf_count(self):
        for v in ([],[1,2,3]):
            with self.assertRaises(ValueError): make_tree(v)
    def test_invalid_values(self):
        for v in ([True,2],[1.5,2],['1',2]):
            with self.assertRaises(ValueError): make_tree(v)
    def test_invalid_options(self):
        for kw in ({'algorithm':'A*'},{'order':'bad'}):
            with self.assertRaises(ValueError): solve(make_tree([1,2]),**kw)
    def test_duplicate_names(self):
        root=Node('R','MAX',(Node('x',None,(),1),Node('x',None,(),2)))
        with self.assertRaises(ValueError): validate_tree(root)
    def test_terminal_with_children(self):
        bad=Node('bad',None,(Node('l',None,(),0),),0)
        with self.assertRaises(ValueError): validate_tree(bad)

def range_to_list(): return list(range(8))
if __name__=='__main__': unittest.main()
