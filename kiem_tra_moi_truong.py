import sys
from pathlib import Path
if __name__=='__main__':
    root=Path(__file__).resolve().parent
    print('Python:',sys.version.split()[0]);print('Thu muc:',root)
    if sys.version_info<(3,10): raise SystemExit('Can Python 3.10 tro len')
    required=['tree_model.py','data_cases.py','search.py','run.py','test_mau.py']
    missing=[p for p in required if not (root/p).is_file()]
    if missing: raise SystemExit('Thieu tep: '+', '.join(missing))
    print('Du tep. Chi dung thu vien chuan. Chay: python chay_mau.py')
