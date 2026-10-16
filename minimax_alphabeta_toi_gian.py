"""Ban ngan: moi list la mot nut, moi int la utility. Du lieu vi du khac bai nop."""
from math import inf

def minimax(tree, is_max=True):
    if type(tree) is int: return tree
    scores=[minimax(child,not is_max) for child in tree]
    return max(scores) if is_max else min(scores)

def alphabeta(tree,is_max=True,alpha=-inf,beta=inf):
    if type(tree) is int: return tree
    best=-inf if is_max else inf
    for child in tree:
        score=alphabeta(child,not is_max,alpha,beta)
        best=max(best,score) if is_max else min(best,score)
        if is_max: alpha=max(alpha,best)
        else: beta=min(beta,best)
        if alpha>=beta: break
    return best

if __name__=='__main__':
    TREE=[[7,2],[5,9]]
    print('Minimax:',minimax(TREE))
    print('Alpha-Beta:',alphabeta(TREE))
    print('Doi TREE de thu vi du khac; ban nay chi tra value, chua thong ke.')
