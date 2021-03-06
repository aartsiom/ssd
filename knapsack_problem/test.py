import argparse
import re
import subprocess

from random import randint
from collections import namedtuple

Item = namedtuple('Item', ['w', 'p'])


def generate_random_object(w):
    return '{} {}'.format(randint(1, w), randint(1, 1000000000))


def generate_test(n, w):
    test_input = [str(n) + ' ' + str(w)]
    for _ in range(n):
        test_input.append(generate_random_object(w))
    with open('input.txt', 'w') as f:
        f.write('\n'.join(test_input))


def get_price(items, mask):
    price, weight = 0, 0
    for i in range(len(items)):
        if mask % 2:
            price += items[i].p
            weight += items[i].w
        mask //= 2
    return price, weight


def parse_file(filename='input.txt'):
    with open(filename, 'r') as f:
        n, w = [int(x) for x in next(f).split()]
        items = []
        for line in f:
            items.append(Item(*[int(x) for x in line.split()]))
    return n, w, items


def naive_solution(n, w, items):
    best_price = 0
    best_solution = 0
    for mask in range(0, 2 ** n):
        current_price, current_weight = get_price(items, mask)
        if current_weight <= w and current_price > best_price:
            best_price = current_price
            best_solution = mask
    return best_price, best_solution


def is_eq_solution():
    res = subprocess.check_output(["./a.out < input.txt"], shell=True).split()
    res = [int(x) for x in res[1:]]
    n, w, items = parse_file()
    best_price, best_solution = naive_solution(n, w, items)
    current_price = sum([items[i-1].p for i in res])
    current_weight = sum([items[i-1].w for i in res])
    print('*' * 10)
    print('best solution: {}'.format(' '.join([str(i+1) for i in range(n) if best_solution & 1 << i])))
    print('my solution: {}'.format(' '.join(str(x) for x in res)))
    print('current_price: {}'.format(current_price))
    print('best_price: {}'.format(best_price))
    print('*' * 10)
    return current_price == best_price and current_weight <= w


def test(n, w):
    generate_test(n, w)
    while is_eq_solution():
        generate_test(n, w)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', dest='n', type=int, default=10)
    parser.add_argument('--w', dest='w', type=int, default=1000000)

    args = parser.parse_args()
    test(args.n, args.w)
