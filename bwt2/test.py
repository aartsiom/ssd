import numpy as np
import string 
import random
from random import randint
from datetime import datetime
import subprocess

def get_suf_array(s):
    suffixes = [s[i:] + s[:i] for i in range(len(s))]
    return suffixes, np.argsort(suffixes)

def get_random_string(length, alphabet_size=2):
    letters = string.ascii_lowercase
    alphabet_size = min(alphabet_size, len(letters))
    result_str = ''.join(random.choice(letters[:alphabet_size]) for i in range(length))
    return result_str


def gen_test(s_length, alphabet_size=3):
    s = get_random_string(s_length, alphabet_size=alphabet_size)
    suffixes, suf_array = get_suf_array(s + ' ')
    alpha2 = ''.join(suffixes[i][-1] for i in suf_array)
    with open('input.txt', 'w') as f:
        f.write(alpha2.replace(' ', '$', 1) + '\n')
        a, b = randint(0, len(s) - 2), randint(0, len(s) - 2)
        l, r = min(a, b), max(a, b)
        r = r + 1 if l == r or l + 1 == r else r
        f.write(s[l:r] + '\n')
    return s, s[l:r] 

def find_all(test_str, test_sub):
    return [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)] 


def test(s_length, alphabet_size):
    res, answ = '', ''
    while res == answ:
        start_time = datetime.now()
        s, p = gen_test(randint(3, s_length), alphabet_size=alphabet_size)
        end_time = datetime.now()
        print('*' * 20)
        res = subprocess.check_output(["./a.out < input.txt"], shell=True).split()[0]
        answ = str(len(list(find_all(s, p))))
        print(res, answ)
        print('Duration: {}'.format(end_time - start_time))
        print('*' * 20)


if __name__ == '__main__':
    test(10, 3)
