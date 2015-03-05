def sublist(list1, list2):
    is_true = False
    for i in range(0, len(list2)):
        if list2[i] == list1[0] and i + len(list1) - 1 <= len(list2) - 1:
            k = i
            for j in range(0, len(list1)):
                if list2[k] != list1[j]:
                    is_true = False
                    break
                else:
                    is_true = True
                k += 1
            if is_true:
                return True
    return is_true

print(sublist([1,2,3], [0,0,1,2,1,2,3,5,6]))
print(sublist([1,2,3,4], [0,0,1,2,3,5,6]))
print(sublist(["Python"], ["Python", "Django"]))
print(sublist(["Python", "Django"], ["Django", "Python"]))
