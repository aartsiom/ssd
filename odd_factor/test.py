from collections import defaultdict
from datetime import datetime
from itertools import combinations
from random import random

import matplotlib.pyplot as plt
import networkx as nx

import string
import subprocess


def read_graph():
    with open('oddfactor.in', 'r') as f:
        n, m = [int(x) for x in next(f).split()]
        E = set()
        for line in f:
            tokens = line.split()
            E.add((int(tokens[0]), int(tokens[1])))
    g = nx.Graph()
    g.add_nodes_from(set([v + 1 for v in range(n)]))
    g.add_edges_from(E)
    return g


def draw_graph():
    g = read_graph()
    pos = nx.spring_layout(g)
    nx.draw_networkx(g, pos)
    plt.title("FailedExample")
    plt.show()


def is_odd_factor(n, g):
    if len(list(g.keys())) != n:
        return False
    for k, v in g.items():
        if len(list(v)) % 2 == 0:
            return False
    return True


def naive_solution(n, E):
    e_list = list(E)
    for i in range(1, 2**len(e_list)):
        graph = defaultdict(list)
        for idx, element in enumerate(e_list):
            if 1 << idx & i:
                graph[element[0]].append(element[1])
                graph[element[1]].append(element[0])
        if is_odd_factor(n, graph):
            return True, graph
    return False, None


def gen_graph(n=4, p=0.4):
    V = set([v for v in range(n)])
    E = set()
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.add(combination)
    return V, E


def gen_test(n=6, p=0.4):
    V, E = gen_graph(n, p)

    with open('oddfactor.in', 'w') as f:
        f.write(str(n) + ' ' + str(len(E)) + '\n')
        for a, b in E:
           f.write(str(a + 1) + ' ' + str(b + 1) + '\n')
    return V, E


def build_graph(res):
    tokens = res.split()[1:]
    g = defaultdict(set)
    for i in range(len(tokens) // 2):
       g[tokens[2*i]].add(tokens[2*i + 1]) 
       g[tokens[2*i+1]].add(tokens[2*i]) 
    return g

def test(n=6, p=0.4):
    while True:
        V, E = gen_test(n=n, p=p)
        print('*' * 20)
        start_time = datetime.now()
        has_solution, solution = naive_solution(n, E)
        code = subprocess.call(["./a.out"])
        end_time = datetime.now()
        if code != 0:
            print('Opps')
            draw_graph()
            return

        with open('oddfactor.out', 'r') as f:
            res = f.read()
        print(res)
        print('*' * 20)

        if has_solution and '-1' in res:
            draw_graph()
            return

        if ('-1' not in res) and (not is_odd_factor(n, build_graph(res))):
            draw_graph()
            return

if __name__ == '__main__':
    test(n=6)
