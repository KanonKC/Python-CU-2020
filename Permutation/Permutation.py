# Prog-09: Permutation
# Fill in your ID & Name
# ...
# Declare that you do this by yourself

import math

def order_of(permutation):
    pass
    # return ???
#---------------------------------
def permutation_at(order, n):
    pass
    # return ???
#---------------------------------
def next_permutation(permutation):
    pass
    # return ???
#---------------------------------
def prev_permutation(permutation):
    pass
    # return ???
#---------------------------------
def longest_cycles(permutation):
    pass
    # return ???
#---------------------------------
def main():
    while True:
        x = input().split()
        cmd = x[0]
        p = [int(e) for e in x[1:]]
        if cmd == 'O':
            print(order_of(p))
        elif cmd == 'A':
            print(permutation_at(p[0], p[1]))
        elif cmd == 'N':
            print(next_permutation(p))
        elif cmd == 'P':
            print(prev_permutation(p))
        elif cmd == 'C':
            print(longest_cycles(p))
        elif cmd == 'Q':
            return
#-------------------------------------
# main()