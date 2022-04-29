import time
from functools import lru_cache


# @lru_cache(maxsize=30)
@lru_cache(maxsize=int(input("No.Of Cache you want")))
def work(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    # inp=int(input("Number of catch you want"))
    print("Now Running Work")
    work(3)
    work(5)
    work(4)
    work(2)
    print("Work Done")
    input("Check")
    work(3)
    print("Again Done")
    print("MAxSize Running")
    work(5)
    print("DOne Done")
    work(4)
    print("OOOOHHHHOOOo")
