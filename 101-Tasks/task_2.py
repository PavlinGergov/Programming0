def fill(n):
    import math
    V = ((n**3)/(6*math.sqrt(2)))/1000
    return V

def tetrahedron_filled(tetrahedrons, water):
    volume = []
    
    for edge in tetrahedrons:
        volume += [fill(edge)]

    counter = 0
    volumes = sorted(volume)
    
    for vol in volumes:
        water -= vol
        if water > 0:
            counter += 1
    
    return counter

tetrahedrons = a = [int(x) for x in input("Enter the edges (using spaces): ").split()]

water = input("Enter the water (in liters): ")
water = int(water)

print("Only " + str(tetrahedron_filled(tetrahedrons, water)) + " of these tetrahedrons can be filled with " + str(water) + " liters of water.")
