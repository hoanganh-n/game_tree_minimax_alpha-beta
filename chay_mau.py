"""Chi sua LEAVES, ROOT_PLAYER, ALGORITHM, ORDER. Giu cac tep cung thu muc."""
from tree_model import make_tree
from search import solve

LEAVES=[7,2,5,9]  # Vi du lam quen, khac T0/T1/T2.
ROOT_PLAYER='MAX'
ALGORITHM='alphabeta'
ORDER='LR'

if __name__=='__main__':
    result=solve(make_tree(LEAVES,ROOT_PLAYER),ALGORITHM,ORDER,trace=True)
    for key in ('value','action','visited','expanded','leaves','cutoffs','leaf_order'):
        print(f'{key}: {result[key]}')
    print('Cac su kien cat:')
    for event in result['trace']:
        if event['event']=='PRUNE': print(event)
