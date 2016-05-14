import math


def vector_movement(current_pos_x, current_pos_y, goal_pos_x, goal_pos_y, movement):

    x_diff = current_pos_x - goal_pos_x
    y_diff = current_pos_y - goal_pos_y

    angle = math.atan2(x_diff, y_diff) # egentligen uppochned hela skiten

    move_x = math.sin(angle) * movement #* t
    move_y = math.cos(angle) * movement #* t då blir det sträckor, går snabbare på snabba datorer

    #current_pos_x -= x_move
    #current_pos_y -= y_move

    return move_x, move_y

def count(start, finish):

    if start < finish:
            start += 1
    else:
        return True