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
    # print('length: {}'.format(length))
    result_str = ''.join(random.choice(letters[:alphabet_size]) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str


def gen_test(s_length, alphabet_size=3):
    s = get_random_string(s_length, alphabet_size=alphabet_size)
    suffixes, suf_array = get_suf_array(s + ' ')
    alpha2 = ''.join(suffixes[i][-1] for i in suf_array)
    with open('input.txt', 'w') as f:
        f.write(alpha2.replace(' ', '$', 1) + '\n')
    print(alpha2.replace(' ', '$', 1), s + '$')
    return s

def test(s_length, alphabet_size):
    res, s = '', ''
    while res == s:
        start_time = datetime.now()
        s = gen_test(s_length, alphabet_size=alphabet_size)
        end_time = datetime.now()
        print('*' * 20)
        
        res = subprocess.check_output(["./a.out < input.txt"], shell=True).split()[0]
        s += '$'
        print(res, s)
        print('Duration: {}'.format(end_time - start_time))
        print('*' * 20)



if __name__ == '__main__':
    test(7, 3)

    # print(get_suf_array('abacaba'))