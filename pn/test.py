import subprocess
import random

t = 'QWERTYUIOPASDFGHJKLZXCVBNM0123456789'
codes = [2, 2, 2, 3, 3, 3, 4, 4, 1, 1, 5, 5, 6, 6, 0, 7, 0, 7, 7, 8, 8, 8, 9, 9, 9, 0]

def generate_text(text_len):
    return ''.join([t[random.randint(0, len(t) - 1)] for _ in range(text_len)])

def generate_test(number_len, max_text_len, lines_count):
    with open('./input.txt', 'w') as file:
        number = ''.join([str(random.randint(0, 9)) for _ in range(number_len)])
        file.write(number + '\n')
        file.write(str(lines_count) + '\n')
        for _ in range(lines_count):
            file.write(generate_text(random.randint(1, max_text_len)) + '\n')


def decode(symbol):
    if symbol == ' ':
        return ''
    if symbol == '\n':
        return ''
    if symbol >= '0' and symbol <= '9':
        return symbol
    return str(codes[ord(symbol) - ord('A')])


def run_test(old_sol_path, new_sol_path):
    old_output, new_output = [subprocess.check_output([sol]).strip() for sol in (old_sol_path, new_sol_path)]
    print(old_output, new_output)
    if 'No solution' in old_output or 'No solution' in new_output:
        if old_output != new_output:
            print("Correct answ {}".format(old_output))
            print("Current answ {}".format(new_output))
            raise Exception('ooops...')
        else:
            return

    decoded_o1 = ''.join([decode(s) for s in old_output])
    decoded_o2 = ''.join([decode(s) for s in new_output])
    if decoded_o1 != decoded_o2:
        print("Correct answ {}".format(old_output))
        print("Current answ {}".format(new_output))
        raise Exception('ooops...')

if __name__ == '__main__':
    test_cout = 0
    while(True):
        generate_test(5, 3, 10)
        run_test('./old', './new')      
        print('{} : PASS'.format(test_cout))
        test_cout += 1