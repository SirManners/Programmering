import math


def vector_movement(current_pos_x, current_pos_y, goal_pos_x, goal_pos_y, movement):

    x_diff = current_pos_x - goal_pos_x
    y_diff = current_pos_y - goal_pos_y

    angle = math.atan2(x_diff, y_diff) # trigonometrin är uppochned men det fungerar

    move_x = math.sin(angle) * movement
    move_y = math.cos(angle) * movement


    return move_x, move_y
