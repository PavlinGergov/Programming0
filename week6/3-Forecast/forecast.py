def forecast(info):
    weather = ["sunshine", "rain", "snow"]
    days = [0,0,0]
    for element in info:
        if element == "sunshine": days[0] += 1
        elif element == "rain": days[1] += 1
        elif element == "snow": days[2] += 1
    if days[0] == max(days) and days[0] == days[1]:
        if days[0] == days[2]: return info[len(info) - 1]
        else: return weather[2]
    elif days[0] == max(days) and days[0] == days[2]: return weather[1]
    elif days[1] == max(days) and days[1] == days[2]: return weather[0]
    else: return weather[days.index(max(days))]

print(forecast(["snow", "snow", "rain", "sunshine"]))
print(forecast(["rain", "rain", "snow", "snow", "sunshine", "sunshine"]))
print(forecast(["rain", "rain", "sunshine", "sunshine"]))