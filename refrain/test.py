import argparse
import string
import subprocess
import random
from datetime import datetime

from random import randint

def get_random_string(length, alphabet_size=2):
    letters = string.ascii_lowercase
    alphabet_size = min(alphabet_size, len(letters))
    result_str = ''.join(random.choice(letters[:alphabet_size]) for i in range(length))
    return result_str


def generate_test(length, alphabet_size):
    with open('input.txt', 'w') as f:
        f.write(get_random_string(length, alphabet_size) + '\n')

def compare_res():
    print('*' * 20)
    start_time = datetime.now()
    res1 = subprocess.check_output(["./main.out < input.txt"], shell=True).split()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    start_time = datetime.now()
    res2 = subprocess.check_output(["./naive.out < input.txt"], shell=True).split()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    
    print("best_cout: {} vs {}".format(res1[0], res2[0]))
    print("best_len: {} vs {}".format(res1[1], res2[1]))
    print('*' * 20)
    return int(res1[0]) * int(res1[1]) == int(res2[0]) * int(res2[1])

def test(length, alphabet_size):
    generate_test(length, alphabet_size)
    while compare_res():
        generate_test(length, alphabet_size)
    print("Oooops")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--l', dest='l', type=int, default=5)
    parser.add_argument('--s', dest='s', type=int, default=2)

    args = parser.parse_args()
    test(args.l, args.s)