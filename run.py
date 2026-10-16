"""Chay 1 cau hinh hoac batch; luu du lieu can doi chieu vao output/."""
from __future__ import annotations
import argparse,csv,json,math,re,statistics
from pathlib import Path
from search import solve
from tree_model import load_cases
from data_cases import case,parameter_tree,required_configs
ROOT=Path(__file__).resolve().parent

def clean(x):
    if isinstance(x,float) and not math.isfinite(x):
        return '+inf' if x>0 else '-inf'
    if isinstance(x,dict): return {k:clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [clean(v) for v in x]
    return x

def execute(configs, repeat=1,trace=False,step=False):
    results=[]
    for exp,name,tree,algo,order,t in configs:
        runs=[solve(tree,algo,order,trace,step) for _ in range(repeat)]
        r=runs[0];r['elapsed_ms']=statistics.median(v['elapsed_ms'] for v in runs)
        r.update(experiment=exp,case=name,parameter=t,repeat=repeat)
        results.append(r)
    return results

def save(results,tag):
    out=ROOT/'output';out.mkdir(exist_ok=True)
    (out/(tag+'.json')).write_text(json.dumps(clean(results),ensure_ascii=False,indent=2),encoding='utf-8')
    fields=['experiment','case','parameter','algorithm','order','value','action',
            'visited','expanded','leaves','cutoffs','pruned_branches','max_depth','repeat','elapsed_ms']
    with (out/(tag+'.csv')).open('w',newline='',encoding='utf-8-sig') as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
        writer.writerows({k:r[k] for k in fields} for r in results)
    print(f'Da luu {len(results)} cau hinh: {out/(tag+".csv")} va JSON')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--case',default='T0',choices=['T0','T1','T2'])
    p.add_argument('--algo',default='alphabeta',choices=['minimax','alphabeta'])
    p.add_argument('--order',default='LR',choices=['LR','RL'])
    p.add_argument('--t',type=int)
    p.add_argument('--batch',action='store_true')
    p.add_argument('--data',type=Path)
    p.add_argument('--trace',action='store_true')
    p.add_argument('--step',action='store_true')
    p.add_argument('--repeat',type=int,default=1)
    p.add_argument('--tag',default='mau')
    a=p.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]+',a.tag): p.error('tag chi gom chu, so, _ va -')
    if not 1<=a.repeat<=10: p.error('repeat tu 1 den 10')
    if (a.batch or a.data) and (a.trace or a.step or a.t is not None):
        p.error('Batch/data khong dung trace, step hoac t; chay rieng de xem vet')
    if a.batch and a.data: p.error('Dung batch HOAC data')
    if (a.trace or a.step) and a.repeat!=1: p.error('Trace/step chi repeat=1')
    if a.batch: configs=list(required_configs())
    elif a.data:
        path=a.data if a.data.is_absolute() else ROOT/a.data
        configs=[('custom',name,tree,algo,order,None)
                 for name,tree in load_cases(path) for order in ('LR','RL')
                 for algo in ('minimax','alphabeta')]
    else:
        tree=case(a.case) if a.t is None else parameter_tree(a.t)
        name=a.case if a.t is None else f'T0_t{a.t}'
        configs=[('single',name,tree,a.algo,a.order,a.t)]
    try: results=execute(configs,a.repeat,a.trace,a.step)
    except (ValueError,OSError) as e: p.error(str(e))
    save(results,a.tag)
    if len(results)==1:
        r=results[0]
        print({k:r[k] for k in ('value','action','visited','leaves','cutoffs','leaf_order','unvisited_nodes')})
        if r['principal_variation'] is not None:
            print('Mot duong choi toi uu:',r['principal_variation'])
        else:
            print('Chi root value/action duoc bao dam exact. Dung Minimax de lap bang that/duong day du.')

if __name__=='__main__':
    try: main()
    except KeyboardInterrupt: print('\nDa dung theo yeu cau; khong ghi ket qua dang do.')
    except (ValueError, OSError, KeyError, TypeError) as exc:
        raise SystemExit('Loi du lieu: ' + str(exc))
