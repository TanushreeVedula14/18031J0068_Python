# make_bricks(small bricks no., big bricks number, n) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_bricks(small,big,goal):
    if(small * 1 + big * 5) > goal:
        return 'True'
    else:
        return 'False'
    
small = int(input("Small Bricks = "))
big = int(input("Big Bricks = "))
goal = int(input("Goal = "))

print(make_bricks(small,big,goal))


