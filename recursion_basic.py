import sys
sys.setrecursionlimit(50) # sets max number of recursive calls that can be made
n=0
def reload():
    global n
    n=n+1
    print(f'reloading {n}')
    reload()

reload()