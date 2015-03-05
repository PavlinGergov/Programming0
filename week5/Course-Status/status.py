def status_count(students):
    result = {
              "finalized": [],
              "not_finalized": [],
              }
    for dictionary in students:
            result[dictionary["status"]] += [dictionary["name"]]
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
            
