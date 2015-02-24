def hash_them(keys, values):
    hash_table = {}
    for i,key in enumerate(keys):
        if i < len(values):
            hash_table[key] = values[i]
        else:
            hash_table[key] = None
    return hash_table

print(hash_them(["Ivan", "Maria"], [1]))
print(hash_them(["Ivan", "Maria"], [1, 2]))
