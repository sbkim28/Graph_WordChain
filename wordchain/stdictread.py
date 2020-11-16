import xlrd
import os
import re


def read_all(dirname):
    wset = set()
    filenames = os.listdir(dirname)
    for filename in filenames:
        read(os.path.join(dirname, filename), wset)
    return wset


def read(f, wset):
    wb = xlrd.open_workbook(f)
    ws = wb.sheet_by_index(0)

    cat = ws.row_values(0)
    inw = cat.index('어휘')
    inp = cat.index('품사')
    ind = cat.index('뜻풀이')

    for i in range(1, ws.nrows):
        r = ws.row_values(i)
        w = extract(r[inw])
        if len(w) < 2 or w in wset:
            continue
        if not validate(w):
            continue
        if available(r[inp], r[ind]):
            wset.add(w)


def validate(rw):
    return re.match(r'^[ㄱ-ㅎㅏ-ㅣ가-힣]*$', rw)


def extract(rw):
    rw = re.sub(r'[-^ㆍ]', '', rw)
    i = rw.find('(')
    if i != -1:
        rw = rw[:i]
    return rw


def available(pos, d):
    poss = pos.rstrip().split('\n')
    defs = d.rstrip().split('\n')

    ret = False
    for pcur in poss:
        pm = re.match(r'\[[Ⅰ-Ⅹ]]', pcur)
        piv = ''
        if pm:
            pcur = pcur[pm.end():]
            piv = pm.group()

        if pcur != '「명사」':
            continue

        for df in defs:
            if piv in df:
                rd = df[len(piv):]
                rd = re.sub(r'^\[[0-9]]', '', rd)
                rd = re.sub(r'^「[0-9]{1,2}」', '', rd)
                if rd[0] != '→' and rd != '고시례':  # Exception...
                    ret = True
                    break
    return ret


