from helpers import readlines

def main():

    data = readlines('inputs/day13_input.txt')

    print(part1(data))


def part1(data):

    original_timestamp = int(data[0])
    current_timestamp = original_timestamp
    bus_numbers = [int(el) for el in data[1].split(',') if el != 'x']

    while True:

        for bus in bus_numbers:
            if current_timestamp % bus == 0:
                return (current_timestamp - original_timestamp) * bus
        
        current_timestamp += 1
        




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


if __name__ == "__main__":
    main()

