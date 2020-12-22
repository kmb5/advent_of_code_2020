from helpers import readfile

def main():

    ''' Test deck:
    p1_deck = [9,2,6,3,1]
    p2_deck = [5,8,4,7,10]
    '''

    data = readfile('inputs/day22_input.txt')

    p1, p2 = data.split('\n\n')

    p1_deck = [int(x) for x in p1.split('\n')[1:]]
    p2_deck = [int(x) for x in p2.split('\n')[1:]]

    round_num = 1

    while len(p1_deck) > 0 and len(p2_deck) > 0:

        print(f'-- Round {round_num} --')
        print(f'Player 1 deck: {(", ").join([str(x) for x in p1_deck])}')
        print(f'Player 2 deck: {(", ").join([str(x) for x in p2_deck])}')
        turn_p1 = p1_deck.pop(0)
        turn_p2 = p2_deck.pop(0)

        print(f'Player 1 plays: {str(turn_p1)}')
        print(f'Player 2 plays: {str(turn_p2)}')

        if turn_p1 > turn_p2:
            p1_deck.extend([turn_p1, turn_p2])
            print(f'Player 1 wins the round!')
        else:
            p2_deck.extend([turn_p2, turn_p1])
            print(f'Player 2 wins the round!')

        round_num += 1
        print()

    print('== Post-game results ==')
    print(f'Player 1 deck: {(", ").join([str(x) for x in p1_deck])}')
    print(f'Player 2 deck: {(", ").join([str(x) for x in p2_deck])}')

    winning_deck = p1_deck if len(p1_deck) > 0 else p2_deck
    winner_score = 0
    for i, item in enumerate(winning_deck[::-1]):
        winner_score += item * (i + 1)
        
    
    print()
    print(f'The winners score is: {str(winner_score)}')






if __name__ == "__main__":
    main()