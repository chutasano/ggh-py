#!/usr/bin/env

import sys
import numpy as np

np.set_printoptions(threshold=np.inf)

if len(sys.argv) < 2:
    print "Usage: gen_keys.py <# dimension> <rand_min> <rand_max>"
if len(sys.argv) == 4:
    rand_min = int(sys.argv[2])
    rand_max = int(sys.argv[3])
else:
    rand_min = -4
    rand_max = 3
dim = int(sys.argv[1])

# generate private basis B pre-lll
B = np.random.choice([x for x in range(rand_min, rand_max)], dim*dim)
B.resize(dim, dim)

print (B)


