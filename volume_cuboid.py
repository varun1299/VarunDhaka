def cuboid_volume(l):
    if type(l) not in [int, float]:
        raise TypeError("The length of cuboid can only be a valid integer or a float")
    return(l*l*l)

length = [2,1.1, -2.5, 2j, 'two']

for i in range(len(length)):
    print ("The volume of cuboid:",cuboid_volume(length[i]))
