from random import randrange


def to_b2(n):
    return [n / 2 ** k % 2 for k in list(range(10))]


def fr_b2(li):
    return sum([li[k] * 2 ** k for k in list(range(10))])


def drink(p1, p2):
    li1, li2 = to_b2(p1), to_b2(p2)
    g0 = [li1[k] == 0 or li2[k] == 0 for k in range(10)]
    g1 = [li1[k] == 1 or li2[k] == 1 for k in range(10)]
    gd = {}
    for i in range(9):
        for j in range(i + 1, 10):
            gd[i, j] = li1[i] != li1[j] or li2[i] != li2[j]
    return g0, g1, gd


def test(g0, g1, gd):
    diff = 10
    t1, t2 = list(range(10)), list(range(10))
    for k in list(range(9, -1, -1)):
        if not g0[k]:
            t1[k], t2[k] = 1, 1
        elif not g1[k]:
            t1[k], t2[k] = 0, 0
        elif diff == 10:
            diff = k
            t1[k], t2[k] = 0, 1
        elif gd[k, diff]:
            t1[k], t2[k] = 1, 0
        else:
            t1[k], t2[k] = 0, 1
    return fr_b2(t1), fr_b2(t2)


if __name__ == "__main__":
    poison1 = randrange(1024)
    poison2 = (poison1 + randrange(1, 1024)) % 1024
    g0, g1, gd = drink(poison1, poison2)
    target1, target2 = test(g0, g1, gd)

    print(poison1, poison2)
    print(to_b2(poison1))
    print(to_b2(poison2))
    print("0:", g0)
    print("1:", g1)
    print("d:", gd)
    print(target1, target2)
