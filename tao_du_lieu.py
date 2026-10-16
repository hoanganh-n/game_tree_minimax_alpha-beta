"""Tao hai cay rieng N1/N2. Co the sua cac utility sau khi tao."""
import argparse,json,random
from pathlib import Path
from data_cases import CASES

def create(seed):
    r=random.Random(seed);trees=[]
    for name,n,player in [('N1',16,'MAX'),('N2',8,'MIN')]:
        while True:
            a=[r.randint(-20,30) for _ in range(n)]
            if a not in list(CASES.values()) and len(set(a))>3: break
        trees.append(dict(name=name,root_player=player,leaves=a))
    return dict(seed=seed,trees=trees)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--seed',type=int,required=True)
    p.add_argument('--out',default='du_lieu_nhom.json');p.add_argument('--overwrite',action='store_true')
    a=p.parse_args();out=Path(__file__).resolve().parent/a.out
    if out.exists() and not a.overwrite: p.error('Tep da ton tai. Doi ten hoac them --overwrite')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(create(a.seed),ensure_ascii=False,indent=2),encoding='utf-8')
    print('Da tao',out)
