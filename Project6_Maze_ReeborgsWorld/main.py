def turn_right(steps):
    for step in range(steps):
        turn_left()

while not at_goal():
    while not right_is_clear():
        turn_left()
    if right_is_clear():
        turn_right(steps = 3)
        move()
        while front_is_clear() and not right_is_clear():
            move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
