from random import randrange


def to_b4(n):
    return [n / 4 ** k % 4 for k in range(5)]


def fr_b4(li):
    return sum([li[k] * 4 ** k for k in range(5)])


def drink(p1, p2):
    li1, li2 = to_b4(p1), to_b4(p2)
    g0 = [li1[k] == 0 or li2[k] == 0 for k in range(5)]
    g1 = [li1[k] == 1 or li2[k] == 1 for k in range(5)]
    g2 = [li1[k] == 2 or li2[k] == 2 for k in range(5)]
    g3 = [li1[k] == 3 or li2[k] == 3 for k in range(5)]
    gc, gf = {}, {}
    for i in range(4):
        for j in range(i + 1, 5):
            diff1 = abs(li1[i] - li1[j])
            diff2 = abs(li2[i] - li2[j])
            gc[i, j] = diff1 == 1 or diff2 == 1
            gf[i, j] = diff1 > 1 or diff2 > 1
    return g0, g1, g2, g3, gc, gf


def check(u, v, d1, d2, c, f):
    a = [[0, 1, 2, 2], [1, 0, 1, 2], [2, 1, 0, 1], [2, 2, 1, 0]]
    a11 = a[u][d1]
    a22 = a[v][d2]
    c1 = a11 == 1 or a22 == 1
    f1 = a11 == 2 or a22 == 2
    if c == c1 and f == f1:
        return u, v
    else:
        return v, u


def test(g0, g1, g2, g3, gc, gf):
    diff = 5
    t1, t2 = list(range(5)), list(range(5))
    for k in list(range(4, -1, -1)):
        li = [g0[k], g1[k], g2[k], g3[k]]
        # print(li)
        u = li.index(True) if True in li else -1
        if li.count(True) == 1:
            t1[k], t2[k] = u, u
        else:
            li[u] = False
            v = li.index(True) if True in li else -1
            if diff == 5:
                diff = k
                t1[k], t2[k] = u, v
            else:
                t1[k], t2[k] = check(u, v, t1[diff], t2[diff], gc[k, diff], gf[k, diff])
    return fr_b4(t1), fr_b4(t2)


poison1 = randrange(1024)
poison2 = (poison1 + randrange(1, 1024)) % 1024
g0, g1, g2, g3, gc, gf = drink(poison1, poison2)
target1, target2 = test(g0, g1, g2, g3, gc, gf)

print(poison1, poison2)
print(to_b4(poison1))
print(to_b4(poison2))
print("0:", g0)
print("1:", g1)
print("2:", g2)
print("3:", g3)
print("c:", gc)
print("f:", gf)
print(target1, target2)
