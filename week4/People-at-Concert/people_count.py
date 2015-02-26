def get_people_count(activity):
    people = []
    for person in activity:
        if person not in people:
            people.append(person)
    return len(people)

print(get_people_count(["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]))
