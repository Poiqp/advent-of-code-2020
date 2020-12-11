def is_collision(start, goal):
    if goal-start <= 1.0:
        print('Collision occurred')
        return True
    return False


def extend_until(start, goal):
    print("Start is: "+str(start))
    if is_collision(start, goal):
        # if YES all recursion should stop and return.
        return goal-start
    else:
        #midpoint = (start+goal)/2
        #extend_until(start, midpoint)
        start = start + 1
        return extend_until(start, goal)


if __name__ == '__main__':
    p1 = 0
    p2 = 4
    new_configuration = extend_until(p1, p2)
    print('New Configuration is: ' + str(new_configuration))
