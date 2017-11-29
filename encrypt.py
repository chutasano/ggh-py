#!/usr/bin/env

import sys
import numpy as np

np.set_printoptions(threshold=np.inf)

e_min = -1
e_max = 1

UB = np.load("pub/UB.npy")
dim = len(UB)
m = range(dim)
print m
e = np.random.choice([x for x in range(e_min, e_max)], dim)
print e
c = np.dot(m, UB) + e
print c

B = np.load("priv/B.npy")
U = np.load("priv/U.npy")
Uinv = np.linalg.inv(U) # U det=1... normal inverse does not lose precision
Binv = np.linalg.inv(B) # not good, may be losing precision here
dec = np.dot(c, Binv)
print dec
dec = np.floor(dec+0.5)
print dec
dec = np.dot(dec, Uinv)
dec = dec.astype(int)
print dec


print "asdf"
print np.dot(e, Binv)
print np.dot(np.dot(c, Binv) - np.dot(e, Binv), Uinv).astype(int)


if np.array_equal(m, dec):
    print "Recovered"
