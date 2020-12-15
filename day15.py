from tqdm import tqdm

def main():

    numbers = [12,20,0,6, 1, 17, 7]

    numbers_seen = {n: [i+1] for i, n in enumerate(numbers[:-1])}

    for i in tqdm(range(7, 30000000)):

        #print(f'TURN {i}')

        prev_num = numbers[i - 1] # 6

        if prev_num not in numbers_seen.keys():
            numbers.append(0)
            numbers_seen[prev_num] = [i]
        else:
            numbers_seen[prev_num].append(i)
            #print(numbers_seen)
            indices = numbers_seen[prev_num]
            num_to_append = (indices[-1]) - (indices[-2])
            numbers.append(num_to_append)
        
        #print(numbers)
        #print()

    
    print(numbers[-1])



if __name__ == "__main__":
    main()