#!/usr/bin/env python
import prompt
from brain_games import cli
from random import randint


def is_even():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    k = 0
    for i in range(0, 3):
        number = randint(1, 101)
        print(f'Question: {number}')
        unswer = prompt.string('Your answer:')
        even = (number % 2 == 0)
        if even:
            un = 'yes'
        else:
            un = 'no'

        if unswer == un:
            print('Correct!')
            k += 1
        else:
            if even:
                print(f"{unswer} is wrong answer ;(. Correct answer was {un}.")
            else:
                print(f"{unswer} is wrong answer ;(. Correct answer was {un}.")
            exit()
    if k == 3:
        print(f"Congratulations, {name}!")


def main():
    is_even()

    if __name__ == '__main__':
        main()
