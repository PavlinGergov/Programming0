def travel_cost(travels):
    s = 0
    cena = 0
    for item in travels:
        s += item
    if s >= 50:
        cena += 50
        return cena
    elif s < 50:
        for line in travels:
            if line >= 23:
                cena += 23
            else:
                cena += line
        return cena

print(travel_cost([23, 24, 2]))
