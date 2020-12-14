from helpers import readlines

def main():

    instructions = '''F10
N3
F7
R90
F11'''

    data = readlines('inputs/day12_input.txt')

    part1(data)

def part1(data):

    ship_pos = {
        'N': 0,
        'S': 0,
        'E': 0,
        'W': 0,
        'facing': 'E'
    }

    for row in data:

        action = row[0]
        value = int(row[1:])

        if action in ('NSEW'):
            ship_pos[action] += value
        elif action == 'F':
            ship_pos[ship_pos['facing']] += value
        elif action in ('LR'):
            ship_pos['facing'] = _handle_turn(action, value, ship_pos['facing'])

    s_minus_n = ship_pos['S'] - ship_pos['N']
    s_or_n = 'S' if s_minus_n > 0 else 'N'
    not_s_or_n = 'S' if s_or_n == 'N' else 'N'

    e_minus_w = ship_pos['E'] - ship_pos['W']
    e_or_w = 'E' if e_minus_w > 0 else 'W'
    not_e_or_w = 'E' if e_or_w == 'W' else 'W'

    final_pos = e_or_w + str(ship_pos[e_or_w] - ship_pos[not_e_or_w]) + s_or_n + str(ship_pos[s_or_n] - ship_pos[not_s_or_n])

    print((ship_pos[e_or_w] - ship_pos[not_e_or_w]) + (ship_pos[s_or_n] - ship_pos[not_s_or_n]))




def _handle_turn(action, value, currently_facing):

    circle = ['N', 'E', 'S', 'W']

    if action == 'R':
        new_dir_pos = int((circle.index(currently_facing) + (value / 90)) % len(circle))
        return circle[new_dir_pos]
    elif action == 'L':
        new_dir_pos = int((circle.index(currently_facing) - (value / 90)) % len(circle))
        return circle[new_dir_pos]





if __name__ == "__main__":
    main()