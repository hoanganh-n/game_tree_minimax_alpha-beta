"""Luu log THAT; test_nhom.py do nhom viet, khong tu tao ket qua PASS."""
import argparse,subprocess,sys
from pathlib import Path
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--module',default='test_nhom')
    a=p.parse_args();root=Path(__file__).resolve().parent
    if not (root/(a.module+'.py')).is_file(): p.error('Chua co '+a.module+'.py')
    q=subprocess.run([sys.executable,'-m','unittest','-v',a.module],cwd=root,
                     text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,encoding='utf-8',errors='replace')
    out=root/'output';out.mkdir(exist_ok=True)
    (out/'ket_qua_test.txt').write_text(q.stdout+'\nEXIT_CODE='+str(q.returncode)+'\n',encoding='utf-8')
    print(q.stdout);raise SystemExit(q.returncode)
