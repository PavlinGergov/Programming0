def on_budget(books, budget):
    books = sorted(books)
    result = {
              "books_on_budget": 0,
              "loan": 0,
              }
    for book in books:
        if budget - book > 0:
            result["books_on_budget"] += 1
            budget -= book
        else:
            result["loan"] += book
    return result
print(on_budget([0, 10, 100, 5, 3, 8, 25], 35))
            
            
