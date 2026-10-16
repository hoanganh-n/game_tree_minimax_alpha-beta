"""Du lieu chung. Moi list la 16, 4 hoac 8 utility tu trai sang phai."""
from tree_model import make_tree
T0 = [9,12,11,10, 8,15,14,13, 4,5,3,6, 100,101,90,95]
T1 = [10,12,10,2]
T2 = [-8,-4,-7,-2,-6,-3,-9,-5]
CASES={'T0':T0,'T1':T1,'T2':T2}
PARAMETERS=[8,10,11,12,14]

def case(name):
    if name not in CASES: raise ValueError('Chi nhan T0, T1, T2')
    return make_tree(CASES[name])

def parameter_tree(t):
    values=T0.copy(); values[0]=t
    return make_tree(values)

def affine_tree():
    return make_tree([2*x-7 for x in T0])

def required_configs():
    # 12 dong co ban + 10 dong tham so + 2 dong affine = 24.
    for name in CASES:
        for order in ('LR','RL'):
            for algo in ('minimax','alphabeta'):
                yield 'base',name,case(name),algo,order,None
    for t in PARAMETERS:
        for algo in ('minimax','alphabeta'):
            yield 'parameter',f'T0_t{t}',parameter_tree(t),algo,'LR',t
    for algo in ('minimax','alphabeta'):
        yield 'affine','T0_affine',affine_tree(),algo,'LR',None
