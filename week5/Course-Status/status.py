def status_count(students):
    result = {
              "finalized": [],
              "not_finalized": [],
              }
    for dictionary in students:
        if dictionary["status"] == "finalized":
            result["finalized"] += [dictionary["name"]]
        elif dictionary["status"] == "not_finalized":
            result["not_finalized"] += [dictionary["name"]]
    return result
print(status_count([{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]))
            
