import numpy as np
import string
import random
from random import randint
from datetime import datetime
import subprocess


def get_random_string(length):
    letters = ['A', 'B', 'C', 'D']
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def naive_solution(a, b):
    best_shift = 0
    best_count = 0
    count = 0
    for a_x, c_x in zip(a, b):
        count += 1 if a_x == c_x else 0
    if count > best_count:
        best_count = count
        best_shift = 0
    for i in range(1, len(b)):
        c = b[-i:] + b[:len(b) - i]
        count = 0
        for a_x, c_x in zip(a, c):
            count += 1 if a_x == c_x else 0
        if count > best_count:
            best_count = count
            best_shift = i
    return best_shift, best_count


def gen_test(m=4):
    a = get_random_string(m)
    b = get_random_string(m)
    with open('input.txt', 'w') as f:
        f.write(str(m) + '\n')
        f.write(a + '\n')
        f.write(b + '\n')
    return a, b


def test(m):
    res, answ = '', ''
    while res == answ:
        a, b = gen_test(m)
        print('*' * 20)
        start_time = datetime.now()
        currest_count, currest_shift =\
            subprocess.check_output(["./a.out < input.txt"], shell=True).split()
        end_time = datetime.now()
        best_shift, best_count = naive_solution(a, b)
        print(currest_shift, best_shift)
        print(currest_count, best_count)
        if (int(currest_shift) != best_shift) and (int(currest_count) != best_count):
            print('oops', a, b)
            return
        print('Duration: {}'.format(end_time - start_time))
        print('*' * 20)


if __name__ == '__main__':
    test(8)
