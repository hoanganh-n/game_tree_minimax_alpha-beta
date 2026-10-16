"""Chi kiem du thanh phan. Khong xac nhan diem hay tinh dung noi dung bao cao."""
import argparse,json,re,zipfile
from pathlib import Path
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--name',default='Nhom10_CayTroChoi_GiuaKy')
    a=p.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]+',a.name): p.error('Ten ZIP chi gom chu/so/_/-')
    root=Path(__file__).resolve().parent
    req=['BaoCao.pdf','TinhTay.pdf','ThuyetTrinh.pptx','test_nhom.py','README_NOP.md','DongGop.md',
         'du_lieu_nhom.json','output/bat_buoc.json','output/bat_buoc.csv',
         'output/tu_tao.json','output/tu_tao.csv','output/ket_qua_test.txt']
    missing=[s for s in req if not (root/s).is_file()]
    if missing: p.error('Con thieu: '+', '.join(missing))
    for f,n in [('bat_buoc',24),('tu_tao',8)]:
        data=json.loads((root/'output'/(f+'.json')).read_text(encoding='utf-8'))
        if not isinstance(data,list) or len(data)!=n: p.error(f+' phai co '+str(n)+' dong JSON')
    paths={root/s for s in req}
    paths.update(root.glob('*.py'))
    paths.update(root.glob('*.json'))
    # Kem cac mo-dun phu duoi thu muc python/, neu nhom tu tach tep.
    if (root/'python').is_dir(): paths.update((root/'python').rglob('*.py'))
    paths.update((root/'output').glob('*.json'));paths.update((root/'output').glob('*.csv'))
    dest=root/(a.name+'.zip')
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted(paths): z.write(f,a.name+'/'+f.relative_to(root).as_posix())
    print('Da tao',dest)
    print('Chua danh gia bao cao. Hay giai nen va tai chay README tren may khac.')
