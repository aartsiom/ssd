import argparse
import subprocess

from random import randint


def generate_random_request(n):
    req_id = randint(1, 4)
    if req_id == 1:
        return '{} {} {}'.format(req_id, randint(1, n), randint(0, 1000000000))

    a, b = randint(1, n), randint(1, n)
    return '{} {} {}'.format(req_id, min(a, b), max(a, b))


def generate_test(n, q):
    test_input = [str(n) + ' ' + str(q)]
    test_input.append(' '.join([str(randint(0, 1000000000)) for _ in range(n)]))
    for _ in range(q):
        test_input.append(generate_random_request(n))
    with open('input.txt', 'w') as f:
        f.write('\n'.join(test_input))


def test(n, q):
    res1 = ''
    res2 = ''
    while res1 == res2:
        generate_test(n, q)
        res1 = subprocess.check_output(["./naive.out < input.txt"], shell=True)
        res2 = subprocess.check_output(["./main.out < input.txt"], shell=True)
        # print(res1, res2)
    print(res1, res2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', dest='n', type=int, default=8)
    parser.add_argument('--q', dest='q', type=int, default=5)

    args = parser.parse_args()
    # print(args.n, args.q)
    test(args.n, args.q)
