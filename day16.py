from helpers import readfile

def main():

    data = readfile('inputs/day16_input.txt')
    split_data = data.split('\n\n')

    rules = split_data[0].split('\n')
    my_ticket = split_data[1].split('\n')[1].split(',')
    nearby_tickets = split_data[2].split('\n')[1:]
    
    rules = _prepare_rules(rules)
    my_ticket = [int(x) for x in my_ticket]
    nearby_tickets = [[int(x) for x in line.split(',')] for line in nearby_tickets]

    ''' Test data:
    nearby_tickets = [
        [7,37,47],
        [40,4,50],
        [55,2,20],
        [38,6,12]
    ]
    
    rules = {
        'class': [[1,3], [5,7]],
        'row': [[6,11], [33,44]],
        'seat': [[13,40], [45,50]]
    }
    '''

    invalid_values = []

    valid_tickets = []

    for ticket in nearby_tickets:
        valid_ticket = False
        for value in ticket:

            not_valid_for_any = False

            for rule in rules.values():
                if value in rule[0] or value in rule[1]:
                    not_valid_for_any = False
                    break
                else:
                    not_valid_for_any = True
            
            if not_valid_for_any:
                invalid_values.append(value)
                valid_ticket = False
                break
            else:
                valid_ticket = True
        if valid_ticket:
            valid_tickets.append(ticket)

    print(sum(invalid_values))
    
    part2(valid_tickets)

def part2(valid_tickets):

    #Test data:
    nearby_tickets = [
        [3,9,18],
        [15,1,5],
        [5,14,9],
        [11,12,13]
    ]
    
    rules = {
        'class': [range(0,2), range(4,20)],
        'row': [range(0,6), range(8,20)],
        'seat': [range(0,14), range(16,20)]
    }

    nearby_tickets_transformed = [list(x) for x in zip(*nearby_tickets)]

    rule_indices = []

    for rule in rules:

        all_conditions_met = False

        for i, tickets in enumerate(nearby_tickets_transformed):
            pass
            
        


    


def _prepare_rules(rules):
    rules_dict = {}

    for i in rules:
        k = i.split(': ')[0]
        v = i.split(': ')[1].split(' or ')
        v = [[int(j) for j in x.split('-')] for x in v]
        rules_dict[k] = [range(x[0], x[1] + 1) for x in v]

    return rules_dict

if __name__ == "__main__":
    main()