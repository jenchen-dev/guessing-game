import sys
from random import randint


start_num = int(sys.argv[1])
end_num = int(sys.argv[2])

answer = randint(start_num, end_num)


while True:
    try:
        guess = int(input(f'guess a number from {start_num} to {end_num}: '))
        if start_num <= guess <= end_num:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print(f'only number {start_num} to {end_num}')
    except ValueError:
        print('please enter a number')
        continue
