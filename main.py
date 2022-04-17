def create_set(r, cond=lambda x: True):
    """
    :param r: range
    :param cond: condition
    :return: integer set
    """
    return [x for x in range(r[0], r[1] + 1) if cond(x)]


def cross(A, B):
    lst = []
    for x in A:
        for y in B:
            lst.append((x, y))
    return lst


def relation(A, B, cond):
    c = cross(A, B)
    return [e for e in c if cond(e[0], e[1])]


def isfunction(A, B, F):
    F_domain = domain(F)

    for (x, y) in F:
        if x not in A:
            return False
        else:
            if y not in B:
                return False

    if hasduplicates(domain(set(F))) or not same(set(F_domain), A):
        return False

    return True


def same(A, B):
    return sorted(A) == sorted(B)


def domain(A):
    return [x for (x, y) in A]


def codomain(A):
    return [y for (x, y) in A]


def hasduplicates(A):
    return not same(set(A), A)


A = [-2, 0, 2]
B = [4, 6, 8 ]
rel = lambda x, y: ((x - y)/ 4).is_integer()
print(relation(A, B, rel))
