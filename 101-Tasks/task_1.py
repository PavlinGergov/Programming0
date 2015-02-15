def fill_tetrahedron(num):
    import math
    
    V = ((num**3)/(6*math.sqrt(2)))/1000
    
    return V

num = input("Enter the edge length: ")
num = int(num)

print("You can fill Regular tetrahedron with edge of " + str(num) + " cm with " + str("%.2f" % fill_tetrahedron(num)) + " liters of water.")


