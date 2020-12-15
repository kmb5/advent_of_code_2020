from tqdm import tqdm

def main():

    numbers = [12,20,0,6, 1, 17, 7]

    for i in tqdm(range(7, 30000000)):

        prev_num = numbers[i - 1]

        if prev_num not in numbers[:-1]:
            numbers.append(0)
        else:
            indices = [n for n, x in enumerate(numbers) if x == prev_num]
            num_to_append = (indices[-1] + 1) - (indices[-2] + 1)
            numbers.append(num_to_append)

    
    print(numbers[-1])



if __name__ == "__main__":
    main()