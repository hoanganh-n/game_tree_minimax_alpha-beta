"""Minimax / Alpha-Beta fail-soft: cung mot API, thong ke minh bach.
trace va step dien ra TRONG loi goi de quy, khong phat lai ket qua.
"""
from __future__ import annotations
from time import perf_counter
import math
from tree_model import Node, validate_tree, walk


def solve(root: Node, algorithm='alphabeta', order='LR', trace=False, step=False):
    validate_tree(root)
    if algorithm not in ('minimax','alphabeta'): raise ValueError('Sai algorithm')
    if order not in ('LR','RL'): raise ValueError('order phai la LR hoac RL')
    stats=dict(visited=0,expanded=0,leaves=0,cutoffs=0,pruned_branches=0,max_depth=0)
    visited_nodes=[];leaf_order=[];pruned_roots=[];returns={};events=[]
    start=perf_counter()

    def emit(event, **kw):
        if not (trace or step): return
        # list con/bo dem duoc sao chep; khong giu list se bi sua ve sau.
        record=dict(event=event, **kw)
        if trace: events.append(record)
        if step:
            print(record)
            input('Enter: buoc tiep theo; Ctrl+C: dung. ')

    def visit(node, alpha, beta, depth):
        stats['visited']+=1;stats['max_depth']=max(stats['max_depth'],depth)
        visited_nodes.append(node.name)
        ain,bin_=alpha,beta
        emit('ENTER',node=node.name,depth=depth,alpha=alpha,beta=beta)
        if node.utility is not None:  # Utility 0 cung la LA, khong phai False.
            stats['leaves']+=1;leaf_order.append(node.name)
            returns[node.name]=dict(value=node.utility,bound='EXACT',action=None)
            emit('LEAF',node=node.name,value=node.utility)
            return node.utility,None
        stats['expanded']+=1
        is_max=node.player=='MAX'
        best=-math.inf if is_max else math.inf
        action=None
        children=node.children if order=='LR' else node.children[::-1]
        for index,child in enumerate(children):
            score,_=visit(child,alpha,beta,depth+1)
            better=score>best if is_max else score<best
            if better: best,action=score,child.name
            emit('UPDATE',node=node.name,child=child.name,score=score,best=best,
                 action=action,alpha=alpha,beta=beta)
            if algorithm=='alphabeta':
                stop=best>=beta if is_max else best<=alpha
                if stop:
                    skipped=[c.name for c in children[index+1:]]
                    if skipped:  # Vuot nguong o con cuoi KHONG tinh la cat nhanh.
                        stats['cutoffs']+=1
                        stats['pruned_branches']+=len(skipped)
                        pruned_roots.extend(skipped)
                        emit('PRUNE',node=node.name,alpha=alpha,beta=beta,
                             value=best,skipped=skipped.copy())
                    break
                if is_max: alpha=max(alpha,best)
                else: beta=min(beta,best)
        # Phan loai bao thu theo CUA SO LUC VAO, khong phai sau cap nhat.
        bound='EXACT'
        if algorithm=='alphabeta':
            if best<=ain: bound='UPPER'
            elif best>=bin_: bound='LOWER'
        returns[node.name]=dict(value=int(best),bound=bound,action=action)
        emit('RETURN',node=node.name,value=int(best),bound=bound,action=action,
             alpha_in=ain,beta_in=bin_)
        return int(best),action

    value,action=visit(root,-math.inf,math.inf,0)
    elapsed_ms=1000*(perf_counter()-start)
    all_nodes=list(walk(root));seen=set(visited_nodes)
    unvisited=[n.name for n in all_nodes if n.name not in seen]
    # Chi dung cac action noi bo de dung duong neu la Minimax day du.
    line=None
    if algorithm=='minimax':
        node=root;line=[root.name]
        while node.children:
            selected=returns[node.name]['action']
            node=next(c for c in node.children if c.name==selected)
            line.append(node.name)
    assert stats['visited']==stats['expanded']+stats['leaves']
    return dict(algorithm=algorithm,order=order,value=value,action=action,**stats,
                leaf_order=leaf_order,visited_nodes=visited_nodes,
                pruned_roots=pruned_roots,unvisited_nodes=unvisited,returns=returns,
                principal_variation=line,trace=events,elapsed_ms=elapsed_ms)
