def max_score(beers, fries):
    beers = sorted(beers)
    fries = sorted(fries)
    s = 0
    for i in range(len(beers) - 1, -1, -1):
        s += beers[i]*fries[i]
    return s
print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))
