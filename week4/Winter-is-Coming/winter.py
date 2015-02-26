def winter_is_coming(seasons):
    count = 0
    is_true  = False
    for i,season in enumerate(seasons):
        if season != "winter":
            count += 1
        else:
            if count == 5:
                is_true = True
            count = 0

        if i == len(seasons) - 1:
            if count == 5:
                is_true = True
    return is_true

print(winter_is_coming(["winter", "summer", "summer", "summer", "spring", "srping"]))


            
