from functools import reduce
from helpers import readlines

def main():

    data = readlines('inputs/day13_input.txt')

    print(part1(data))
    print(part2(data))


def part1(data):

    original_timestamp = int(data[0])
    current_timestamp = original_timestamp
    bus_numbers = [int(el) for el in data[1].split(',') if el != 'x']

    while True:

        for bus in bus_numbers:
            if current_timestamp % bus == 0:
                return (current_timestamp - original_timestamp) * bus
        
        current_timestamp += 1

def part2(data):

    '''Prepare chinese remainder such as:
    In the given example: 7,13,x,x,59,x,31,19 we're basically trying to find a time t where:
    t % 7 == 0 
    t % 13 == 12 (the remainder we're looking for is 12 because we want bus 13 to depart at t+1, so essentially we want (t+1) % 13 == 0) 
    t % 59 == 55 (we want bus 59 to depart at t+4) 
    ...
    ....
    etc.
    '''

    bus_numbers = [int(el) if el != 'x' else el for el in data[1].split(',')]
    timestamps = [i for i in range(len(bus_numbers)) if bus_numbers[i] != 'x']
    timestamps = [i if i == 0 else bus_numbers[i] - i for i in timestamps]

    bus_numbers = [i for i in bus_numbers if i != 'x']

    return chinese_remainder(bus_numbers, timestamps)

def visualise():

    inp = [939, [7,13,59,31,19]]
    timestamp = inp[0]
    bus_numbers = inp[1]

    r = range(timestamp, timestamp + 100)

    buses = ['bus ' + str(i) for i in bus_numbers]
    print('time\t' + ('\t').join(buses))

    for second in r:
        departures = []
        for bus in bus_numbers:
            if second % bus == 0:
                departures.append('D')
            else:
                departures.append('.')

        print(str(second) + '\t' + ('\t').join(departures))


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

if __name__ == "__main__":
    main()
