from helpers import readlines

def main():

    """I HATE RECURSION SO MUCH BECAUSE I CAN'T UNDERSTAND IT :("""

    # TODO: 1. Learn how to solve recursive problems
    # TODO: 2. Refactor this whole mess below

    data = readlines('inputs/day7_input.txt')

    print(part1(data))
    print(part2(data))

def part1(data):
    
    """I kinda get how this works but my solution
    which was similar didn't work so I took some help here... """

    counter = 0

    all_bag_types = _prepare_data(data)
    
    for bag_type in all_bag_types:
        trail = []
        if check_bag(bag_type, all_bag_types, trail):
            counter += 1
        
    return counter

def part2(data):
    """I have no idea how this works and 
    I admit that I found it on reddit :( """

    all_bag_types = _prepare_data(data, add_counts=True)
    
    return count_bags('shiny gold', all_bag_types)


def count_bags(outer_bag, all_bag_types):

    count = 0

    if len(all_bag_types[outer_bag]):
        for bag in all_bag_types[outer_bag]:
            count += all_bag_types[outer_bag][bag]
            count += all_bag_types[outer_bag][bag] * count_bags(bag, all_bag_types)
        return count
    else:
        return 0


def check_bag(bag, all_bag_types, trail):

    if 'shiny gold' in all_bag_types[bag]:
        return True
    else:
        for inner_bag in all_bag_types[bag]:
            if inner_bag not in trail:
                trail.append(inner_bag)
                if check_bag(inner_bag, all_bag_types, trail):
                    return True
        return False

def _prepare_data(data, add_counts=False):

    """First part doesn't need counts
    At least this is my implementation"""


    rules = [x.split('contain') for x in data]
    all_bag_types = {}

    for rule in rules:
        

        bag_type = rule[0].replace(' bags ', '')
        required_contents = [x.split(',') for x in rule[1:]][0]
        num_bags_required = [x.split(' ')[1] for x in required_contents]
        required_contents = [x.split(' ')[2:4] for x in required_contents]
        required_contents = [(' ').join(x) for x in required_contents]


        if bag_type not in all_bag_types.keys():
            if add_counts:
                all_bag_types[bag_type] = {}
            else:
                all_bag_types[bag_type] = []

        if required_contents == ['other bags.']:
            continue

        if add_counts:
            all_bag_types[bag_type] = {}
            for i, content in enumerate(required_contents):

                all_bag_types[bag_type][content] = int(num_bags_required[i])

        else:
            for content in required_contents:
                all_bag_types[bag_type].append(content)
    
    return all_bag_types


if __name__ == "__main__":
    main()