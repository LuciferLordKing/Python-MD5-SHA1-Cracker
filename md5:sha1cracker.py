#!/usr/bin/env python

from hashlib import md5, sha1
from sys import argv

def choosealgorithm(o):
    if argv[1] == '-m':
        return md5
    elif argv[1] == '-s':
        return sha1
    else:
        print('No such option')
        input()
        exit()

def readfile(f1, f2):
    with open(f1, 'r') as hashfile:
        hashes = hashfile.readlines()
    with open(f2, 'r') as dictionary:
        wordlist = dictionary.readlines()
    return [x.strip() for x in hashes], [x.strip() for x in wordlist]

def attack(algorithm, hashes, wordlist):
    for h in hashes:
        cracked = False
        for w in wordlist:
            print(w)
            if algorithm(w.encode('utf8')).hexdigest() == h.lower():
                cracked = True
                print('\033[92mCracked!\033[0m\n')
                break
        if cracked == False:
            print('\033[91mNot in dictionary.\033[0m\n')

if len(argv) != 4:
    print('Usage: sha1crack.py [-m|s] [hashfile] [dictionary]')
else:
    algorithm = choosealgorithm(argv[1])
    hashes, wordlist = readfile(argv[2], argv[3])
    attack(algorithm, hashes, wordlist)
    input()
    exit()