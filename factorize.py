def is_prime(n, *, bases=None):
    if bases is None: bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    if n < 2: return False

    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n == p: return True
        if n%p == 0: return False

    s = 0
    d = n-1
    while d%2 == 0:
        s += 1
        d //= 2

    for b in bases:
        if b%n == 0: continue
        a = pow(b,d,n)
        if a == 1 or a == n-1: continue
        for _ in range(s-1):
            a = a*a % n
            if a == n-1: break

        else: return False

    return True


def factorize(n): pass
