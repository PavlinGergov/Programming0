def forecast(info):
    result = {
                "rain": 0,
                "snow": 0,
                "sunshine": 0,
             }

    for day in info:
        result[day] += 1

    days = []
    weather = []
    for item in result:
        weather.append(item)
        days.append(result[item])

    equal = 0
    current = -1
    
    for element in result:
        if current != -1:
            if current == result[element]:
                equal += 1
            else:
                the_day = element
        else:
            current = result[element]

    if equal == 1:
        return the_day
    elif equal == 2:
        return info[len(info) - 1]
    else:
        return weather[days.index(max(days))]

print(forecast(["snow", "snow", "rain", "sunshine"]))
print(forecast(["rain", "rain", "snow", "snow", "sunshine", "sunshine"]))
print(forecast(["rain", "rain", "sunshine", "sunshine"]))