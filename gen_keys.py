#!/usr/bin/env

import sys
import numpy as np

np.set_printoptions(threshold=np.inf)

# adapted from https://nathanbrixius.wordpress.com/2013/09/13/generating-random-unimodular-matrices-with-a-column-of-ones/
def rand_unimod(n):
    l = np.tril(np.random.randint(-5, 5, size=(n,n))).astype('int64')
    u = np.triu(np.random.randint(-5, 5, size=(n,n))).astype('int64')
    for i in range(0, n):
        l[i, i] = u[i, i] = 1
    return np.dot(l,u)

with open("lll.txt") as f:
    lines = [line.lstrip('[').rstrip("\n]") for line in f]

l = []
for i in range(len(lines)-1):
    l.append([int(n) for n in lines[i].split()])
dim = len(l)

# generate private basis B and transformation U
B = np.array(l)
U = rand_unimod(dim)

print B
print U
print np.dot(U,B)

np.save("priv/B.npy", B)
np.save("priv/U.npy", U)
np.save("pub/UB.npy", np.dot(U, B))

