diet = ['tomato', 'broccoli', 'cucumber', 'steak', 'shrimp']
for x in range(0,5):
    for y in range(0,5):
        if not(x == y) :
            print("{} {}".format(diet[x], diet[y]))
