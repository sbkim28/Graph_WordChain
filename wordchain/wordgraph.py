import wordchain.stdictread as std
from wordchain.kutil import ruleofthumb


class CVertex:
    def __init__(self, c):
        self.c = c
        self.tv = 0
        self.sub = None
        self.conn = []
        self.kill = 0

    def get_od(self):
        return len(self.conn)

    def set(self, v):
        ret = self.tv != v
        self.tv = v
        return ret


class WEdge:
    def __init__(self, w, to):
        self.w = w
        self.tv = 0
        self.to = to
        self.checked = False
        self.r = False

    def update(self):
        self.tv = self.to.tv


def initialize(ws):
    vertex = []
    for w in ws:
        cf = w[0]
        cl = w[-1]
        sn = find(cf, vertex)
        if not sn:
            sn = CVertex(cf)
            insert(sn, vertex)
        en = find(cl, vertex)
        if not en:
            en = CVertex(cl)
            insert(en, vertex)
        sn.conn.append(WEdge(w, en))

    for cn in vertex:
        c = cn.c
        rot = ruleofthumb(c)
        if rot != c:
            cn.sub = find(rot, vertex)
    return vertex


def insert(cn, vertex):
    for i in range(len(vertex)):
        if vertex[i].c > cn.c:
            vertex.insert(i, cn)
            return
    vertex.append(cn)


def find(c, vertex):
    for v in vertex:
        if v.c == c:
            return v
    return None


def create_simple(ws):
    flag = True
    vertex = initialize(ws)
    while flag:
        flag = False
        for cn in vertex:
            changed = set_tv(cn)
            flag = changed or flag

    return vertex


def set_tv(cn):
    if cn.get_od() == 0:
        if cn.sub:
            return cn.set(cn.sub.tv)
        else:
            return cn.set(1)
    mv = 2
    for wc in cn.conn:
        wc.update()
        if tv(mv) < tv(wc.tv):
            mv = wc.tv
    mv = dv(mv)
    if cn.sub and tv(mv) > tv(cn.sub.tv):
        mv = cn.sub.tv

    return cn.set(mv)


def create_bool(ws):
    flag = True
    vertex = initialize(ws)
    while flag:
        flag = False
        for cn in vertex:
            if cn.kill != 0:
                continue
            changed = set_bool(cn)
            flag = changed or flag

    for cn1 in vertex:
        if cn1.kill != 0:
            continue
        for wc1 in cn1.conn:
            if wc1.to.kill == 0 and not wc1.r and wc1.to is not cn1:
                for wc2 in wc1.to.conn:
                    if not wc2.r and wc2.to is cn1:
                        wc1.r = True
                        wc2.r = True
                        break
    flag = True
    while flag:
        flag = False
        for cn in vertex:
            if cn.kill != 0:
                continue
            changed = set_bool(cn)
            flag = changed or flag
    return vertex


def set_bool(cn):
    flag = True
    count = 0
    ret = False

    if cn.sub and cn.sub.kill == -1:
        cn.kill = -1
        return True

    for wc in cn.conn:
        if wc.checked or wc.r:
            continue
        if wc.to.kill == -1:
            wc.checked = True
            ret = True
            continue
        if wc.to.kill == 1:
            cn.kill = -1
            return True
        count += 1
        if wc.to.c != cn.c:
            flag = False

    if count == 0:
        if cn.sub:
            if cn.sub.kill == 0:
                return False
            else:
                cn.kill = cn.sub.kill
                return True
        else:
            cn.kill = 1
            return True
    if flag:
        if count % 2 == 0:
            cn.kill = 1
        else:
            cn.kill = -1
        return True
    return ret


def dv(x):
    if x == 0:
        return 0
    return x + 1


def tv(x):
    ret = 0
    if x % 2 == 1:
        ret = 1000 // x
    elif x != 0:
        ret = -1000 // x
    return ret


m = create_bool(std.read_all('D://768198'))

cnt = 0
print("ready")

for c in m:
    if c.kill == 0:
        print(c.c, end=':')
        flag = False
        for conn in c.conn:
            if conn.to.kill == 0:
                if not flag:
                    flag = True
                else:
                    print(', ', end='')
                print(conn.w, end='')
        print()
