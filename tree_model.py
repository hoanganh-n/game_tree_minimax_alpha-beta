"""Mo hinh cay nhi phan day du, alternating MAX/MIN. Khong can thu vien ngoai."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import json
from pathlib import Path

@dataclass(frozen=True)
class Node:
    name: str
    player: Optional[str]
    children: tuple['Node', ...] = ()
    utility: Optional[int] = None


def make_tree(leaves, root_player='MAX') -> Node:
    """leaves theo trai -> phai. So la la 1,2,4,...,256; diem nguyen."""
    if root_player not in ('MAX', 'MIN'):
        raise ValueError('root_player phai la MAX hoac MIN')
    if not isinstance(leaves, (list, tuple)):
        raise ValueError('leaves phai la list/tuple')
    size = len(leaves)
    if size < 1 or size > 256 or size & (size - 1):
        raise ValueError('So la phai la luy thua cua 2, tu 1 den 256')
    if any(type(v) is not int or abs(v)>1000000 for v in leaves):
        raise ValueError('Diem la phai la so nguyen, tri tuyet doi <= 1000000')
    data = tuple(leaves)  # Luu ban sao; khong sua list cua nguoi goi.
    counter = 0
    def build(part, name, player):
        nonlocal counter
        if len(part)==1:
            counter += 1
            return Node(f'L{counter:02d}', None, (), part[0])
        names = ('A','B') if name=='R' else (name+'1',name+'2')
        other = 'MIN' if player=='MAX' else 'MAX'
        mid=len(part)//2
        return Node(name, player, (build(part[:mid], names[0], other),
                                  build(part[mid:], names[1], other)))
    return build(data, 'R', root_player)


def walk(node):
    yield node
    for child in node.children:
        yield from walk(child)


def validate_tree(root):
    """Kiem du lieu truoc do thoi gian; 0 la utility hop le."""
    names=set()
    def check(n, expected=None, depth=0):
        if not isinstance(n, Node) or depth>8:
            raise ValueError('Node khong hop le hoac cay qua sau')
        if not isinstance(n.name,str) or not n.name or n.name in names:
            raise ValueError('Ten nut rong hoac trung')
        names.add(n.name)
        if n.utility is not None:
            if type(n.utility) is not int or n.children or n.player is not None:
                raise ValueError('La phai co utility nguyen, khong co con/player')
            return
        if n.player not in ('MAX','MIN') or len(n.children)!=2:
            raise ValueError('Nut trong phai co MAX/MIN va hai con')
        if expected is not None and n.player != expected:
            raise ValueError('Cay phai luan phien MAX/MIN')
        other='MIN' if n.player=='MAX' else 'MAX'
        for child in n.children: check(child, other, depth+1)
    check(root)


def load_cases(path):
    data=json.loads(Path(path).read_text(encoding='utf-8-sig'))
    if not isinstance(data,dict) or not isinstance(data.get('trees'),list):
        raise ValueError('JSON phai co trees la danh sach')
    seen=set();result=[]
    for c in data['trees']:
        if not isinstance(c,dict): raise ValueError('Moi cay phai la object')
        name=c.get('name')
        if not isinstance(name,str) or not name or name in seen:
            raise ValueError('Ten cay rong hoac trung')
        seen.add(name)
        root=make_tree(c.get('leaves'),c.get('root_player','MAX'))
        result.append((name,root))
    if not result: raise ValueError('Danh sach cay rong')
    return result
